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
    pv_lf_random = pd.DataFrame()
    dict_pv_lf={}
    for y in years :
        pv_lf_random = pd.DataFrame()
        for week in range(number_of_mean_weeks):
            pv_lf_random = pd.concat([pv_lf_random, pd.DataFrame([pv_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
        # Iterate over the DataFrame and populate the dictionary demand
        dict_pv_lf_local = {(y,w,h): pv_lf_random.iloc[w-1,h-1]for w in weeks for h in hours}
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

# FIX CAPEX
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data
data_occ       = [747e3, 597e3, 517e3, 477e3, 477e3] # CAPEX en €/MW sans intercalaire
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

# Investment defined until 2018
hist_data_inv = {y: 0.0e3 for y in range(years[0]-60,years[0])}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0e3 for y in range(years[0] - 60, years[0])}
# Historical needed Capacity
hist_data_capa = {}
hist_data_capa[2019] = 9.4e3

# Set data
pt_ren_pv.set_historic_data('CAPA',hist_data_capa)
pt_ren_pv.set_historic_data('INV',hist_data_inv)
pt_ren_pv.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_ren_pv.set_InvMax({y: 100e3 for y in years})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','pv', pe_ren_pv, pt_ren_pv, ps_ren_pv)
index = index + 1
