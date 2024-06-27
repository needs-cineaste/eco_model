############################
# REN - Wind On Shore
############################

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_ren_won = prm_tech()
pt_ren_won.set_isPvar({y: True for y in years})
pt_ren_won.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})

#--------------------------
# Get 52 weeks of data
#--------------------------
won_lf = np.loadtxt(arg).tolist()[:int(7*24*52)]
# Build dataframe with matrix form
won_lf_reshape = pd.DataFrame(np.array(won_lf).reshape(-1, 7 * 24))

#--------------------------
# Weeks managment
#--------------------------

if profil_weeks == 'average' or  profil_weeks == "M4" :
    # Select a random index from the filtered indices
    won_lf_new = pd.DataFrame()
    dict_won_lf={}
    for y in years :
        won_lf_new = pd.DataFrame()
        for w in range(number_of_mean_weeks):

            # A random week inside each groups of the representative weeks is used
            if ren_loadfactor == 'random':
                won_lf_new = pd.concat([won_lf_new, pd.DataFrame([won_lf_reshape.iloc[random.choice(np.where(group == w)[0])]])], ignore_index=True)
            
            # The maximum Load Factor of the week inside each groups of the representative weeks is used
            elif ren_loadfactor == 'high':
                # Find the index of the max load factor
                index_sol = won_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmax()
                # Concat with the new line
                won_lf_new = pd.concat([won_lf_new, pd.DataFrame([won_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The minimum Load Factor of the week inside each groups of the representative weeks is used
            elif ren_loadfactor == 'low':
                # Find the index of the min load factor
                index_sol = won_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmin()
                # Concat with the new line
                won_lf_new = pd.concat([won_lf_new, pd.DataFrame([won_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The "most medium" Load Factor of the week inside each groups of the representative weeks is used
            elif ren_loadfactor == 'medium':
                # Average of the serie
                avg = won_lf_reshape.sum(axis=1).iloc[np.where(group == w)].mean()
                # Calculate abs difference with the average
                absd = (won_lf_reshape.sum(axis=1).iloc[np.where(group == w)] - avg).abs()
                # Find the index of the minimum difference
                index_sol = absd.idxmin()
                # Concat with the new line
                won_lf_new = pd.concat([won_lf_new, pd.DataFrame([won_lf_reshape.iloc[index_sol]])], ignore_index=True)
                
            else:
                print('Choice to make for ren_loadfactor in [random,high,medium,low]... EXIT...')

        # Iterate over the DataFrame and populate the dictionary demand
        dict_won_lf_local = {(y,w,h): won_lf_new.iloc[w-1,h-1]for w in weeks for h in hours}
        dict_won_lf={**dict_won_lf,**dict_won_lf_local}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

# Build the dict
pt_ren_won.set_LF(copy.deepcopy(dict_won_lf))

#--------------------------
# Economical parameters
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 937 - Eolien offshore posé - hypothèse : Référence
pe_ren_won = prm_eco()
pe_ren_won.set_r(r)
lt = 30
ct = 1 # construction time
pe_ren_won.set_lt(lt)

# FIX CAPEX
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data
data_occ       = [1300e3, 1200e3 , 1050e3, 900e3, 900e3] # CAPEX en €/MW sans intercalaire
pe_ren_won.calculate_capex_dict(data_occ,ct,lt,pe_ren_won.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None
pe_ren_won.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om_years = [2020,2030,2040,2050,2060] # Available data for data
data_fix_om   = [40e3, 35e3, 30e3, 25e3, 25e3] # €/MW/an
pe_ren_won.set_fix_om(data_fix_om,data_fix_om_years)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_ren_won.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_ren_won.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_ren_won.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_ren_won.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_ren_won.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_won = prm_fatal()

#--------------------------
# Historical Capacities
#--------------------------

#--------------------------
# Historical Capacities
#--------------------------
#Initialisation avec des 0
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity
hist_data_capa = {}
# Source Chiffres clés des énergie renouvelables  2023 - SDES - https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-energies-renouvelables-2023/
hist_data_inv.update({2000: 41, 2001: 20, 2002: 83, 2003: 92, 2004: 155, 2005: 495, 2006: 836, 2007: 784, 2008: 1090, 2009: 1169, 2010: 1199, 2011: 832, 2012: 774, 2013: 585, 2014: 1178, 2015: 997, 2016: 1474, 2017: 1772, 2018: 1612, 2019: 1424, 2020: 1177, 2021: 1309, 2022: 1478}) # En MW
# Source CINEASTE/data/source/Eolien_Evolution_puissance_inst - reférence : SDES
hist_data_capa.update({2009: 3495, 2010: 4664, 2011: 5903, 2012: 6756, 2013: 7560, 2014: 8145, 2015: 9280, 2016: 10479, 2017: 11957, 2018: 13746, 2019: 15413, 2020: 16765, 2021: 18006, 2022: 19251, 2023: 20772, 2024: 21899}) # En MW

# Set data
pt_ren_won.set_historic_data('CAPA',hist_data_capa)
pt_ren_won.set_historic_data('INV',hist_data_inv)
pt_ren_won.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_ren_won.set_InvMax({y: 100e3 for y in range(years.start-1, years.stop-1)})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','won', pe_ren_won, pt_ren_won, ps_ren_won)
index = index + 1
