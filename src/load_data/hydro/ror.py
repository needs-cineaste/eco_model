############################
# REN - PV
############################

# Technical parameters
pt_hydro_ror = prm_tech(years,hours)
pt_hydro_ror.set_isPvar({y: False for y in years})
pt_hydro_ror.set_isEvar({(y,h): False for y in years for h in hours})
pt_hydro_ror.set_isFatal(True)

# Define PV LF at y and h
pv_lf = np.loadtxt('../data/formatted/hydro/pv/2019.inc').tolist()
dict_pv_lf = {(y, h): pv_lf[h-1] for y in years for h in hours}
pt_hydro_ror.set_LF(copy.deepcopy(dict_pv_lf))

# Economical parameters
# PIF
pe_hydro_ror = prm_eco(r)
pe_hydro_ror.set_occ(1.700e6) 
pe_hydro_ror.set_ct(1)
pe_hydro_ror.set_dt(25)

# PIF
pe_hydro_ror.set_fix_om(20)
pe_hydro_ror.set_var_om(0)
pe_hydro_ror.set_var_f(0)
pe_hydro_ror.set_var_co2(0)

tec_hydro_ror = Techno('ren','pv', pe_hydro_ror, pt_hydro_ror)
#tec_hydro_ror.Print()

data_techno[index] = copy.deepcopy(tec_hydro_ror)
index = index + 1
