############################
# HYDRO - LAKE
############################

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_hydro_lake = prm_tech()

pt_hydro_lake.set_isPvar({y: False for y in years})

#Source :  Panorama des energies renouvelables dec 2023 - ORE - ENEDIS - RTE - SER
P = {y: 13610 for y in years}
pt_hydro_lake.set_P(copy.deepcopy(P))

# Define lake LF at y and h
#lake_lf = np.loadtxt('../data/formatted/hydro/lake/2019.inc').tolist()
#dict_lake_lf = {(y,h): lake_lf[h-1] for y in years for h in hours}
#pt_hydro_lake.set_LF(copy.deepcopy(dict_lake_lf))

# Get 52 weeks of data
lake_lf = np.loadtxt(arg).tolist()[:int(7*24*52)]
# Build dataframe with matrix form
lake_lf_reshape = pd.DataFrame(np.array(lake_lf).reshape(-1, 7 * 24))

#--------------------------
# Weeks managment
#--------------------------
if profil_weeks == 'average' or  profil_weeks == "M4" :
    # Select a random index from the filtered indices
    #    lake_lf_random = pd.DataFrame()
    #    dict_lake_lf={}
    #    for y in years :
    #        lake_lf_random = pd.DataFrame()
    #        for week in range(number_of_mean_weeks):
    #            lake_lf_random = pd.concat([lake_lf_random, pd.DataFrame([lake_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
    #        # Iterate over the DataFrame and populate the dictionary demand
    #        dict_lake_lf_local = {(y,w,h): lake_lf_random.iloc[w-1,h-1]for w in weeks for h in hours}
    #        dict_lake_lf={**dict_lake_lf,**dict_lake_lf_local}

    lake_lf_average = lake_lf_reshape.groupby(group).mean()
    dict_lake_lf = {(y,w,h): lake_lf_average.iloc[w-1, h-1] for y in years for w in weeks for h in hours}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

pt_hydro_lake.set_LF(copy.deepcopy(dict_lake_lf))

# Energy
pt_hydro_lake.set_isEvar({(y,w,h): False for y in years for w in weeks for h in hours})
E = {(y,w,h): P[y] * dict_lake_lf[y,w,h] for y in years for w in weeks for h in hours}
pt_hydro_lake.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - hydro existant
pe_hydro_lake = prm_eco()
pe_hydro_lake.set_r(r)

lt = None
ct = None # construction time
pe_hydro_lake.set_lt(lt)

# FIX CAP
# data_fix_cap = None # €/MW/an
# pe_hydro_lake.set_fix_cap(data_fix_cap)
# FIX DEP
data_fix_dep = 121*0.5e3 # €/MW/an
pe_hydro_lake.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  121*0.5e3  # €/MW/an
pe_hydro_lake.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_hydro_lake.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_hydro_lake.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_hydro_lake.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_hydro_lake.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_hydro_lake.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_hydro_lake = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','hydro','lake', pe_hydro_lake, pt_hydro_lake, ps_hydro_lake)
index = index + 1
