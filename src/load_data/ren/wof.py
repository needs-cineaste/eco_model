############################
# REN - Wind Off Shore
############################

#--------------------------
# Technical parameters
#--------------------------

pt_ren_wof = prm_tech(years,hours)
pt_ren_wof.set_isPvar({y: True for y in years})
pt_ren_wof.set_isEvar({(y,h): True for y in years for h in hours})

# Define wof LF at y and h
wof_lf = np.loadtxt('../data/formatted/ren/wind/offshore/2019.inc').tolist()
dict_wof_lf = {(y, h): wof_lf[h-1] for y in years for h in hours}
pt_ren_wof.set_LF(copy.deepcopy(dict_wof_lf))

#--------------------------
# Economical parameters
#--------------------------
# PIF
pe_ren_wof = prm_eco(years)
pe_ren_wof.set_r(r)

occ, ct, dt = 4.5e6, 1, 30
pe_ren_wof.calculate_capex(occ,ct,dt,r)

# PIF
pe_ren_wof.set_fix_om(120)
pe_ren_wof.set_fix_mi(0)
pe_ren_wof.set_var_om(0)
pe_ren_wof.set_var_f(0)
pe_ren_wof.set_var_co2(0)
pe_ren_wof.set_var_mi(0)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_wof = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','wof', pe_ren_wof, pt_ren_wof, ps_ren_wof)
index = index + 1
