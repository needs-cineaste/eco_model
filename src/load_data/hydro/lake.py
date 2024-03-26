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

# Define ROR LF at y and h
lake_lf = np.loadtxt('../data/formatted/hydro/lake/2019.inc').tolist()
dict_lake_lf = {(y,h): lake_lf[h-1] for y in years for h in hours}
pt_hydro_lake.set_LF(copy.deepcopy(dict_lake_lf))

# Energy
pt_hydro_lake.set_isEvar({(y,h): False for y in years for h in hours})
E = {(y,h): P[y] * dict_lake_lf[y,h] for y in years for h in hours}
pt_hydro_lake.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

# PIF
pe_hydro_lake = prm_eco(years)
pe_hydro_lake.set_r(r)

occ, ct, dt = 0, 1, 50
pe_hydro_lake.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_lake.set_fix_om(10e3)
pe_hydro_lake.set_fix_mi(0)
pe_hydro_lake.set_var_om(10)
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
