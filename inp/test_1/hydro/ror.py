############################
# HYDRO - ROR
############################

#--------------------------
# Technical parameters
#--------------------------

pt_hydro_ror = prm_tech(years,hours)

pt_hydro_ror.set_isPvar({y: False for y in years})

# Power
P = {y: 11000 for y in years}
pt_hydro_ror.set_P(copy.deepcopy(P))

# Define ROR LF at y and h
#ror_lf = np.loadtxt('../data/formatted/hydro/ror/2019.inc').tolist()
#dict_ror_lf = {(y,h): ror_lf[h-1] for y in years for h in hours}
#pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Get 52 weeks of data
ror_lf = np.loadtxt('../../../data/formatted/hydro/ror/2019.inc').tolist()[:int(7*24*52)]
# Build dataframe with matrix form
ror_lf_reshape = pd.DataFrame(np.array(ror_lf).reshape(-1, 7 * 24))
# Get list of demand groupby 
group = np.arange(len(ror_lf_reshape)) // (52 / number_of_mean_weeks)
# Select a random index from the filtered indices
ror_lf_random = pd.DataFrame()
for week in range(number_of_mean_weeks):
    ror_lf_random = pd.concat([ror_lf_random, pd.DataFrame([ror_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
# Iterate over the DataFrame and populate the dictionary demand
dict_ror_lf = {(y,w,h): ror_lf_random.iloc[w-1,h-1] for y in years for w in weeks for h in hours}
# Build the dict
pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Energy
pt_hydro_ror.set_isEvar({(y,w,h): False for y in years for w in weeks for h in hours})
E = {(y,w,h): P[y] * dict_ror_lf[y,w,h] for y in years for w in weeks for h in hours}
pt_hydro_ror.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

# PIF
pe_hydro_ror = prm_eco(years)
pe_hydro_ror.set_r(r)

occ, ct, dt = 2.5e6, 10, 80
pe_hydro_ror.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_ror.set_fix_om(70e3)
pe_hydro_ror.set_fix_mi(0)
pe_hydro_ror.set_var_om(0)
pe_hydro_ror.set_var_f(0)
pe_hydro_ror.set_var_co2(0)
pe_hydro_ror.set_var_mi(0)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_hydro_ror = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','hydro','ror', pe_hydro_ror, pt_hydro_ror, ps_hydro_ror)
index = index + 1
