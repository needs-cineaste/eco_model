############################
# HYDRO - STEP
############################

#--------------------------
# Technical parameters  CHARGE
#--------------------------

pt_hydro_step_c = prm_tech(years,hours)

pt_hydro_step_c.set_isPvar({y: False for y in years})

P = {y: 5000 for y in years} # 5 GW 
pt_hydro_step_c.set_P(copy.deepcopy(P))

#--------------------------
# Economical parameters   CHARGE
#------------------------- -

pe_hydro_step_c = prm_eco(years)
pe_hydro_step_c.set_r(r)
# PIF

occ, ct, dt = 5e6, 10, 100
pe_hydro_step_c.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_step_c.set_fix_om(10e3)
pe_hydro_step_c.set_fix_mi(0)
pe_hydro_step_c.set_var_om(-10)
pe_hydro_step_c.set_var_f(0)
pe_hydro_step_c.set_var_co2(0)
pe_hydro_step_c.set_var_mi(0)


#--------------------------
# Technical parameters  DISCHARGE
#--------------------------
pt_hydro_step_d = prm_tech(years,hours)

pt_hydro_step_d.set_isPvar({y: False for y in years})

P = {y: 5000 for y in years} # 5 GW 
pt_hydro_step_d.set_P(copy.deepcopy(P))


#--------------------------
# Economical parameters   DISCHARGE
#------------------------- -

pe_hydro_step_d = prm_eco(years)
pe_hydro_step_d.set_r(r)
# PIF

occ, ct, dt = 5e6, 10, 100
pe_hydro_step_d.calculate_capex(occ,ct,dt,r)

# PIF
pe_hydro_step_d.set_fix_om(10e3)
pe_hydro_step_d.set_fix_mi(0)
pe_hydro_step_d.set_var_om(10)
pe_hydro_step_d.set_var_f(0)
pe_hydro_step_d.set_var_co2(0)
pe_hydro_step_d.set_var_mi(0)

#--------------------------
# Specific parameters for Storage
#--------------------------

ps_hydro_step = prm_storage()

ps_hydro_step.set_level_max(500e3) # 500 GWh au pif !!!
ps_hydro_step.set_level_min(0)
ps_hydro_step.set_level_start(250e3)

ps_hydro_step.set_efficiency_discharge(0.85)
ps_hydro_step.set_efficiency_charge(0.85)

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('storage','step','charge', pe_hydro_step_c, pt_hydro_step_c, ps_hydro_step)
index = index + 1

techno[index] = Techno('storage','step','discharge', pe_hydro_step_d, pt_hydro_step_d, ps_hydro_step)
index = index + 1