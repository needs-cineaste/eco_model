############################
# HYDRO - ROR
############################

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_hydro_ror = prm_tech()

pt_hydro_ror.set_isPvar({y: False for y in years})

# Source :  Panorama des energies renouvelables dec 2023 - ORE - ENEDIS - RTE - SER
pt_hydro_ror.set_P(6678)

# Define ROR LF at y and h
#ror_lf = np.loadtxt('../data/formatted/hydro/ror/2019.inc').tolist()
#dict_ror_lf = {(y,h): ror_lf[h-1] for y in years for h in hours}
#pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Get 52 weeks of data
ror_lf = np.loadtxt(arg).tolist()[:int(7*24*52)]
# Build dataframe with matrix form
ror_lf_reshape = pd.DataFrame(np.array(ror_lf).reshape(-1, 7 * 24))

#--------------------------
# Weeks managment
#--------------------------

if profil_weeks == 'average' or  profil_weeks == "M4" :
    # Select a random index from the filtered indices
    ror_lf_new = pd.DataFrame()
    dict_ror_lf={}
    for y in years :
        ror_lf_new = pd.DataFrame()
        for w in range(number_of_mean_weeks):

            # A random week inside each groups of the representative weeks is used
            if loadfactor_ror == 'random':
                ror_lf_new = pd.concat([ror_lf_new, pd.DataFrame([ror_lf_reshape.iloc[random.choice(np.where(group == w)[0])]])], ignore_index=True)
            
            # The maximum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_ror == 'high':
                # Find the index of the max load factor
                index_sol = ror_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmax()
                # Concat with the new line
                ror_lf_new = pd.concat([ror_lf_new, pd.DataFrame([ror_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The minimum Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_ror == 'low':
                # Find the index of the min load factor
                index_sol = ror_lf_reshape.sum(axis=1).iloc[np.where(group == w)].idxmin()
                # Concat with the new line
                ror_lf_new = pd.concat([ror_lf_new, pd.DataFrame([ror_lf_reshape.iloc[index_sol]])], ignore_index=True)
            
            # The "most medium" Load Factor of the week inside each groups of the representative weeks is used
            elif loadfactor_ror == 'medium':
                # Average of the serie
                avg = ror_lf_reshape.sum(axis=1).iloc[np.where(group == w)].mean()
                # Calculate abs difference with the average
                absd = (ror_lf_reshape.sum(axis=1).iloc[np.where(group == w)] - avg).abs()
                # Find the index of the minimum difference
                index_sol = absd.idxmin()
                # Concat with the new line
                ror_lf_new = pd.concat([ror_lf_new, pd.DataFrame([ror_lf_reshape.iloc[index_sol]])], ignore_index=True)
                            
            else:
                print('Choice to make for loadfactor_ror in [random,high,medium,low]... EXIT...')

        # Iterate over the DataFrame and populate the dictionary demand
        dict_ror_lf_local = {(y,w,h): ror_lf_new.iloc[w-1,h-1]for w in weeks for h in hours}
        dict_ror_lf={**dict_ror_lf,**dict_ror_lf_local}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Energy
pt_hydro_ror.set_isEvar({(y,w,h): False for y in years for w in weeks for h in hours})
E = {(y,w,h): pt_hydro_ror.get_P()[y] * dict_ror_lf[y,w,h] for y in years for w in weeks for h in hours}
pt_hydro_ror.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - hydro existant

pe_hydro_ror = prm_eco()
pe_hydro_ror.set_r(r)
lt = None
ct = None # construction time
pe_hydro_ror.set_lt(lt)
pe_hydro_ror.set_deco_cost(0) # don't know

# FIX CAP
# data_fix_cap = None # €/MW/an
# pe_hydro_ror.set_fix_cap(data_fix_cap)
# Tot RTE = 121 => Here, arbitrary 1/2 1/2 
data_fix_dep = 121*0.5e3 # €/MW/an
pe_hydro_ror.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  121*0.5e3  # €/MW/an
pe_hydro_ror.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_hydro_ror.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_hydro_ror.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_hydro_ror.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_hydro_ror.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_hydro_ror.set_var_mi(data_var_mi)
#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_hydro_ror = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','hydro','ror', pe_hydro_ror, pt_hydro_ror, ps_hydro_ror)
index = index + 1
