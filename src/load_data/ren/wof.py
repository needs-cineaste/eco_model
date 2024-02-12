############################
# REN - Wind Off Shore
############################

# Technical parameters
pt_ren_wof = prm_tech(years,hours)
pt_ren_wof.set_isPvar({y: True for y in years})
pt_ren_wof.set_isEvar({(y,h): True for y in years for h in hours})
pt_ren_wof.set_isFatal(True)

# Define wof LF at y and h
wof_lf = np.loadtxt('../data/formatted/ren/wind/offshore/2019.inc').tolist()
dict_wof_lf = {(y, h): wof_lf[h-1] for y in years for h in hours}
pt_ren_wof.set_LF(copy.deepcopy(dict_wof_lf))

# Economical parameters
# PIF
pe_ren_wof = prm_eco(years)
pe_ren_wof.set_r(r)

pe_ren_wof.set_occ(4.5e6) 
pe_ren_wof.set_ct(1)
pe_ren_wof.set_dt(30)

# PIF
pe_ren_wof.set_fix_om(120)
pe_ren_wof.set_fix_mi(0)
pe_ren_wof.set_var_om(0)
pe_ren_wof.set_var_f(0)
pe_ren_wof.set_var_co2(0)
pe_ren_wof.set_var_mi(0)

pe_ren_wof.update_costs()

tec_ren_wof = Techno('ren','wof', pe_ren_wof, pt_ren_wof)
#tec_ren_wof.Print()

data_techno[index] = copy.deepcopy(tec_ren_wof)
index = index + 1
