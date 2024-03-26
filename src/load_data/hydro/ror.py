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
ror_lf = np.loadtxt('../data/formatted/hydro/ror/2019.inc').tolist()
dict_ror_lf = {(y,h): ror_lf[h-1] for y in years for h in hours}
pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Energy
pt_hydro_ror.set_isEvar({(y,h): False for y in years for h in hours})
E = {(y,h): P[y] * dict_ror_lf[y,h] for y in years for h in hours}
pt_hydro_ror.set_E(copy.deepcopy(E))

#--------------------------
# Economical parameters
#--------------------------

# PIF
pe_hydro_ror = prm_eco(years)
pe_hydro_ror.set_r(r)

occ, ct, dt = 0, 1, 50
pe_hydro_ror.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_ror.set_fix_om(10e3)
pe_hydro_ror.set_fix_mi(0)
pe_hydro_ror.set_var_om(10)
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
