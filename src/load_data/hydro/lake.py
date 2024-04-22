############################
# HYDRO - LAKE
############################

#--------------------------
# Technical parameters
#--------------------------

pt_hydro_lake = prm_tech(years,hours)

pt_hydro_lake.set_isPvar({y: False for y in years})

# Power
P = {y: 10300 for y in years}
pt_hydro_lake.set_P(copy.deepcopy(P))

# Define lake LF at y and h
#lake_lf = np.loadtxt('../data/formatted/hydro/lake/2019.inc').tolist()
#dict_lake_lf = {(y,h): lake_lf[h-1] for y in years for h in hours}
#pt_hydro_lake.set_LF(copy.deepcopy(dict_lake_lf))

# Get 52 weeks of data
lake_lf = np.loadtxt('../data/formatted/hydro/lake/2019.inc').tolist()[:int(7*24*52)]
# Build dataframe with matrix form
lake_lf_reshape = pd.DataFrame(np.array(lake_lf).reshape(-1, 7 * 24))
# Get list of demand groupby 
group = np.arange(len(lake_lf_reshape)) // (52 / number_of_mean_weeks)
# Select a random index from the filtered indices
lake_lf_random = pd.DataFrame()
for week in range(number_of_mean_weeks):
    lake_lf_random = pd.concat([lake_lf_random, pd.DataFrame([lake_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
# Iterate over the DataFrame and populate the dictionary demand
dict_lake_lf = {(y,w,h): lake_lf_random.iloc[w-1,h-1] for y in years for w in weeks for h in hours}
# Build the dict
pt_hydro_lake.set_LF(copy.deepcopy(dict_lake_lf))

# Energy
pt_hydro_lake.set_isEvar({(y,w,h): False for y in years for w in weeks for h in hours})
E = {(y,w,h): P[y] * dict_lake_lf[y,w,h] for y in years for w in weeks for h in hours}
pt_hydro_lake.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

# PIF
pe_hydro_lake = prm_eco(years)
pe_hydro_lake.set_r(r)

occ, ct, dt = 2.5e6, 10, 80
pe_hydro_lake.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_lake.set_fix_om(70e3)
pe_hydro_lake.set_fix_mi(0)
pe_hydro_lake.set_var_om(0)
pe_hydro_lake.set_var_f(0)
pe_hydro_lake.set_var_co2(0)
pe_hydro_lake.set_var_mi(0)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_hydro_lake = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','hydro','lake', pe_hydro_lake, pt_hydro_lake, ps_hydro_lake)
index = index + 1
