############################
# REN - Wind Off Shore
############################

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_ren_wof = prm_tech()
pt_ren_wof.set_isPvar({y: True for y in years})
pt_ren_wof.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})

#--------------------------
# Get 52 weeks of data
#--------------------------
wof_lf = np.loadtxt(arg).tolist()[:int(7*24*52)]
# Build dataframe with matrix form
wof_lf_reshape = pd.DataFrame(np.array(wof_lf).reshape(-1, 7 * 24))

#--------------------------
# Weeks managment
#--------------------------

if profil_weeks == 'average' or  profil_weeks == "M4" :
    # Select a random index from the filtered indices
    wof_lf_new = pd.DataFrame()
    dict_wof_lf={}
    for y in years :
        wof_lf_new = pd.DataFrame()
        for w in range(number_of_mean_weeks):

            # A random week inside each groups of the representative weeks is used
            if loadfactor_wof == 'random':
                wof_lf_new = pd.concat([wof_lf_new, pd.DataFrame([wof_lf_reshape.iloc[random.choice(np.where(group == w)[0])]])], ignore_index=True)
            
            # The maximum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_wof == 'high':
                # Find the index of the max load factor
                index_sol = wof_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmax()
                # Concat with the new line
                wof_lf_new = pd.concat([wof_lf_new, pd.DataFrame([wof_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The minimum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_wof == 'low':
                # Find the index of the min load factor
                index_sol = wof_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmin()
                # Concat with the new line
                wof_lf_new = pd.concat([wof_lf_new, pd.DataFrame([wof_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The "most medium" Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_wof == 'medium':
                # Average of the serie
                avg = wof_lf_reshape.sum(axis=1).iloc[np.where(group == w)].mean()
                # Calculate abs difference with the average
                absd = (wof_lf_reshape.sum(axis=1).iloc[np.where(group == w)] - avg).abs()
                # Find the index of the minimum difference
                index_sol = absd.idxmin()
                # Concat with the new line
                wof_lf_new = pd.concat([wof_lf_new, pd.DataFrame([wof_lf_reshape.iloc[index_sol]])], ignore_index=True)
                
            else:
                print('Choice to make for loadfactor_wof in [random,high,medium,low]... EXIT...')

        # Iterate over the DataFrame and populate the dictionary demand
        dict_wof_lf_local = {(y,w,h): wof_lf_new.iloc[w-1,h-1]for w in weeks for h in hours}
        dict_wof_lf={**dict_wof_lf,**dict_wof_lf_local}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

# Build the dict
pt_ren_wof.set_LF(copy.deepcopy(dict_wof_lf))

#--------------------------
# Economical parameters
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 937 - Eolien offshore posé - hypothèse : Référence

pe_ren_wof = prm_eco()
pe_ren_wof.set_r(r)
lt = 30
ct = 2 # construction time
pe_ren_wof.set_lt(lt)
pe_ren_wof.set_deco_cost(3e5) # pif


# FIX CAPEX
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data => Eolien en mer "posé" !!
if occ_wof == 'medium':
    data_occ = [2600e3,1700e3,1500e3,1300e3,1300e3] # CAPEX en €/MW sans intercalaire
elif occ_wof == 'low':
    data_occ = [2600e3,1300e3,1000e3,750e3,750e3] # CAPEX en €/MW sans intercalaire
pe_ren_wof.calculate_capex_dict(data_occ,ct,lt,pe_ren_wof.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None
pe_ren_wof.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om_years = [2020,2030,2040,2050,2060] # Available data for data
data_fix_om   = [80e3 , 58e3 , 47e3 , 36e3 , 36e3] # €/MW/an
pe_ren_wof.set_fix_om(data_fix_om,data_fix_om_years)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_ren_wof.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_ren_wof.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_ren_wof.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_ren_wof.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_ren_wof.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_wof = prm_fatal()

#--------------------------
# Historical Capacities
#--------------------------

# Investment defined until 2018
hist_data_inv = {y: 0.0e3 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0e3 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity
hist_data_capa = {}
#Source : CINEASTE/data/source/Eolien_Nouveaux_raccordements - reférence : SDES
hist_data_inv.update({2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 4, 2019: 0, 2020: 0, 2021: 0, 2022: 480, 2023: 993}) # En MW
# Source CINEASTE/data/source/Eolien_Evolution_puissance_inst - reférence : SDES
hist_data_capa.update({2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 4, 2019: 4, 2020: 4, 2021: 4, 2022: 4, 2023: 484, 2024: 1477}) # En MW

# Set data
pt_ren_wof.set_historic_data('CAPA',hist_data_capa)
pt_ren_wof.set_historic_data('INV',hist_data_inv)
pt_ren_wof.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_ren_wof.set_InvMax({y: 4e3 for y in range(years.start-1, years.stop-1)})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','wof', pe_ren_wof, pt_ren_wof, ps_ren_wof)
index = index + 1
