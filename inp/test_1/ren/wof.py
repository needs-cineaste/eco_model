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
    wof_lf_random = pd.DataFrame()
    dict_wof_lf={}
    for y in years :
        wof_lf_random = pd.DataFrame()
        for week in range(number_of_mean_weeks):
            wof_lf_random = pd.concat([wof_lf_random, pd.DataFrame([wof_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
        # Iterate over the DataFrame and populate the dictionary demand
        dict_wof_lf_local = {(y,w,h): wof_lf_random.iloc[w-1,h-1]for w in weeks for h in hours}
        dict_wof_lf={**dict_wof_lf,**dict_wof_lf_local}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

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

# FIX CAPEX
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data
data_occ       = [2600e3,1700e3,1500e3,1300e3,1300e3] # CAPEX en €/MW sans intercalaire
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
hist_data_inv = {y: 0.0e3 for y in range(years[0]-60,years[0])}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0e3 for y in range(years[0] - 60, years[0])}
# Historical needed Capacity
hist_data_capa = {}
hist_data_capa[2019] = 0.0e3

# Set data
pt_ren_wof.set_historic_data('CAPA',hist_data_capa)
pt_ren_wof.set_historic_data('INV',hist_data_inv)
pt_ren_wof.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_ren_wof.set_InvMax({y: 100e3 for y in years})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','wof', pe_ren_wof, pt_ren_wof, ps_ren_wof)
index = index + 1
