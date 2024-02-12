############################
# REN - PV
############################

# Technical parameters
pt_ren_pv = prm_tech(years,hours)
pt_ren_pv.set_isPvar({y: True for y in years})
pt_ren_pv.set_isEvar({(y,h): True for y in years for h in hours})
pt_ren_pv.set_isFatal(True)
# Read pv load factor

# Define PV LF at y and h
pv_lf = np.loadtxt('../data/formatted/ren/solar/pv/2019.inc').tolist()
dict_pv_lf = {(y, h): pv_lf[h-1] for y in years for h in hours}
pt_ren_pv.set_LF(copy.deepcopy(dict_pv_lf))

# Economical parameters
# PIF
pe_ren_pv = prm_eco(years)
pe_ren_pv.set_r(r)

pe_ren_pv.set_occ(1.700e6) 
pe_ren_pv.set_ct(1)
pe_ren_pv.set_dt(25)

# PIF
pe_ren_pv.set_fix_om(20)
pe_ren_pv.set_fix_mi(0)
pe_ren_pv.set_var_om(0)
pe_ren_pv.set_var_f(0)
pe_ren_pv.set_var_co2(0)
pe_ren_pv.set_var_mi(0)

pe_ren_pv.update_costs()

tec_ren_pv = Techno('ren','pv', pe_ren_pv, pt_ren_pv)
#tec_ren_pv.Print()

data_techno[index] = copy.deepcopy(tec_ren_pv)
index = index + 1
