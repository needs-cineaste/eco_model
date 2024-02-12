############################
# HYDRO - ROR
############################

# Technical parameters
pt_hydro_ror = prm_tech(years,hours)
pt_hydro_ror.set_isPvar({y: False for y in years})

P = {y: 11000 for y in years}
pt_hydro_ror.set_P(copy.deepcopy(P))

pt_hydro_ror.set_isEvar({(y,h): True for y in years for h in hours})
pt_hydro_ror.set_isFatal(True)

# Define ROR LF at y and h
ror_lf = np.loadtxt('../data/formatted/hydro/ror/2019.inc').tolist()
dict_ror_lf = {(y, h): ror_lf[h-1] for y in years for h in hours}
pt_hydro_ror.set_LF(copy.deepcopy(dict_ror_lf))

# Economical parameters
pe_hydro_ror = prm_eco(years)
pe_hydro_ror.set_r(r)
# PIF
pe_hydro_ror.set_occ(0) 
pe_hydro_ror.set_ct(1)
pe_hydro_ror.set_dt(50)

# PIF
pe_hydro_ror.set_fix_om(10e3)
pe_hydro_ror.set_fix_mi(0)
pe_hydro_ror.set_var_om(10)
pe_hydro_ror.set_var_f(0)
pe_hydro_ror.set_var_co2(0)
pe_hydro_ror.set_var_mi(0)

# Mandatory
pe_hydro_ror.update_costs()

tec_hydro_ror = Techno('hydro','ror', pe_hydro_ror, pt_hydro_ror)
#tec_hydro_ror.Print()

data_techno[index] = copy.deepcopy(tec_hydro_ror)
index = index + 1
