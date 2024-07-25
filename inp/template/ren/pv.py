############################
# REN - PV
############################

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_ren_pv = prm_tech()
pt_ren_pv.set_isPvar({y: True for y in years})
pt_ren_pv.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})

#--------------------------
# Get 52 weeks of data
#--------------------------

pv_lf = np.loadtxt(arg).tolist()[:int(7*24*52)]
# Build dataframe with matrix form
pv_lf_reshape = pd.DataFrame(np.array(pv_lf).reshape(-1, 7 * 24))

#--------------------------
# Weeks managment
#--------------------------

if profil_weeks == 'average' or  profil_weeks == "M4" :
    # Select a random index from the filtered indices
    pv_lf_new = pd.DataFrame()
    dict_pv_lf={}
    for y in years :
        pv_lf_new = pd.DataFrame()
        for w in range(number_of_mean_weeks):

            # A random week inside each groups of the representative weeks is used
            if loadfactor_pv == 'random':
                pv_lf_new = pd.concat([pv_lf_new, pd.DataFrame([pv_lf_reshape.iloc[random.choice(np.where(group == w)[0])]])], ignore_index=True)
            
            # The maximum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_pv == 'high':
                # Find the index of the max load factor
                index_sol = pv_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmax()
                # Concat with the new line
                pv_lf_new = pd.concat([pv_lf_new, pd.DataFrame([pv_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The minimum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_pv == 'low':
                # Find the index of the min load factor
                index_sol = pv_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmin()
                # Concat with the new line
                pv_lf_new = pd.concat([pv_lf_new, pd.DataFrame([pv_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The "most medium" Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_pv == 'medium':
                # Average of the serie
                avg = pv_lf_reshape.sum(axis=1).iloc[np.where(group == w)].mean()
                # Calculate abs difference with the average
                absd = (pv_lf_reshape.sum(axis=1).iloc[np.where(group == w)] - avg).abs()
                # Find the index of the minimum difference
                index_sol = absd.idxmin()
                # Concat with the new line
                pv_lf_new = pd.concat([pv_lf_new, pd.DataFrame([pv_lf_reshape.iloc[index_sol]])], ignore_index=True)
                            
            else:
                print('Choice to make for loadfactor_pv in [random,high,medium,low]... EXIT...')

        # Iterate over the DataFrame and populate the dictionary demand
        dict_pv_lf_local = {(y,w,h): pv_lf_new.iloc[w-1,h-1]for w in weeks for h in hours}
        dict_pv_lf={**dict_pv_lf,**dict_pv_lf_local}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

# Build the dict
pt_ren_pv.set_LF(copy.deepcopy(dict_pv_lf))

#--------------------------
# Economical parameters
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 937 - Pv au sol - hypothèse : Référence
pe_ren_pv = prm_eco()
pe_ren_pv.set_r(r)
lt = 30
ct = 1 # construction time
pe_ren_pv.set_lt(lt)
pe_ren_pv.set_deco_cost(3e5) # web

# FIX CAPEX
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data => PV "au sol" !!
if occ_pv == 'medium':
    data_occ = [747e3, 597e3, 517e3, 477e3, 477e3] # CAPEX en €/MW sans intercalaire
elif occ_pv == 'high':
    data_occ = [747e3, 612e3, 562e3, 527e3, 527e3] # CAPEX en €/MW sans intercalaire
elif occ_pv == 'low':
    data_occ = [747e3, 597e3, 517e3, 477e3, 477e3] # CAPEX en €/MW sans intercalaire
pe_ren_pv.calculate_capex_dict(data_occ,ct,lt,pe_ren_pv.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None
pe_ren_pv.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om_years = [2020,2030,2040,2050,2060] # Available data for data
data_fix_om   =  [11e3,10e3,9e3,8e3,8e3] # €/MW/an
pe_ren_pv.set_fix_om(data_fix_om,data_fix_om_years)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_ren_pv.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_ren_pv.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_ren_pv.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_ren_pv.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_ren_pv.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_pv = prm_fatal()

#--------------------------
# Historical Capacities
#--------------------------

#--------------------------
# Historical Capacities
#--------------------------
# Investment defined until 2018
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity
hist_data_capa = {}
# Source Chiffres clés des Energie renouvelables 2023 - SDES - https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-energies-renouvelables-2023/
hist_data_inv.update({2005: 3.52, 2006: 7.10, 2007: 16.40, 2008: 64.96, 2009: 254.95, 2010: 856.00, 2011: 1762.31, 2012: 1117.23, 2013: 660.30, 2014: 958.73, 2015: 911.59, 2016: 583.27, 2017: 916.98, 2018: 907.28, 2019: 982.87, 2020: 1201.83, 2021: 2834.73, 2022: 2384.50}) # En MW
# Source CINEASTE/data/source/Solaire_Evolution_puissance_inst - reférence : SDES
hist_data_capa.update({2009: 70, 2010: 276, 2011: 1015, 2012: 2612, 2013: 3642, 2014: 4285, 2015: 5185, 2016: 6056, 2017: 6679, 2018: 7567, 2019: 8466, 2020: 9399, 2021: 10551, 2022: 13343, 2023: 15870 }) 

# Set data
pt_ren_pv.set_historic_data('CAPA',hist_data_capa)
pt_ren_pv.set_historic_data('INV',hist_data_inv)
pt_ren_pv.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_ren_pv.set_InvMax({y: pv_invest_max for y in range(years.start-1, years.stop-1)})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','pv', pe_ren_pv, pt_ren_pv, ps_ren_pv)
index = index + 1
