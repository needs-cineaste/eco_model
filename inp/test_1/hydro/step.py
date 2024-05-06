############################
# HYDRO - STEP
############################

#--------------------------
# Technical parameters
#--------------------------

pt_hydro_step = prm_tech(years,hours)

pt_hydro_step.set_isPvar({y: False for y in years})

P = {y: 5000 for y in years} # 5 GW 
pt_hydro_step.set_P(copy.deepcopy(P))

pt_hydro_step.set_isEvar({(y,h): True for y in years for h in hours})

#--------------------------
# Economical parameters
#--------------------------

pe_hydro_step = prm_eco(years)
pe_hydro_step.set_r(r)
# PIF

occ, ct, dt = 5e6, 10, 100
pe_hydro_step.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_step.set_fix_om(10e3)
pe_hydro_step.set_fix_mi(0)
pe_hydro_step.set_var_om(10)
pe_hydro_step.set_var_f(0)
pe_hydro_step.set_var_co2(0)
pe_hydro_step.set_var_mi(0)

#--------------------------
# Specific parameters for Storage
#--------------------------

ps_hydro_step = prm_storage()

ps_hydro_step.set_level_max(500e3) # 500 GWh au pif !!!
ps_hydro_step.set_level_min(0)
ps_hydro_step.set_level_start(250e3)

ps_hydro_step.set_efficiency(0.70)

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('storage','hydro','step', pe_hydro_step, pt_hydro_step, ps_hydro_step)
index = index + 1
