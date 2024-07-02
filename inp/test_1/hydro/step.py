############################
# HYDRO - STEP
############################

#----------------------------------------------------------------
# Technical parameters  CHARGE
#----------------------------------------------------------------

pt_hydro_step_c = prm_tech()

pt_hydro_step_c.set_isPvar({y: False for y in years})

P = {y: 5394 for y in years} # 5 GW 
pt_hydro_step_c.set_P(copy.deepcopy(P))
pt_hydro_step_c.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})  # Energy is endogeneous

#--------------------------
# Economical parameters - STEP Charge
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 939 - STEP -

pe_hydro_step_c = prm_eco()
pe_hydro_step_c.set_r(r)
lt = 50
ct = 1 # construction time

pe_hydro_step_c.set_lt(lt)

# FIX DEP
data_fix_dep = 29e3 # €/MW/an -> RTE : CAPEX = 1000 => /2 because charge discharge => 29e3 annual (!)
pe_hydro_step_c.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  7.5e3  # €/MW/an
pe_hydro_step_c.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_hydro_step_c.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_hydro_step_c.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_hydro_step_c.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_hydro_step_c.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_hydro_step_c.set_var_mi(data_var_mi)

#----------------------------------------------------------------
# Technical parameters  DISCHARGE
#----------------------------------------------------------------

pt_hydro_step_d = prm_tech()

pt_hydro_step_d.set_isPvar({y: False for y in years})
pt_hydro_step_d.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})  # Energy is endogeneous

P = {y: 5394 for y in years} # 5 GW 
pt_hydro_step_d.set_P(copy.deepcopy(P))

#--------------------------
# Economical parameters - STEP discharge
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 939 - STEP -

pe_hydro_step_d = prm_eco()
pe_hydro_step_d.set_r(r)
lt = 50
ct = 1 # construction time
pe_hydro_step_d.set_lt(lt)

# FIX DEP
data_fix_dep = 29e3 # €/MW/an -> RTE : CAPEX = 1000 => /2 because charge discharge => 29e3 annual (!)
pe_hydro_step_d.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  7.5e3  # €/MW/an
pe_hydro_step_d.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_hydro_step_d.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_hydro_step_d.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_hydro_step_d.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_hydro_step_d.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_hydro_step_d.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Storage
#--------------------------

ps_hydro_step = prm_storage()

ps_hydro_step.set_level_max(500e3) # 500 GWh au pif !!!
ps_hydro_step.set_level_min(0)
ps_hydro_step.set_level_start(250e3)

ps_hydro_step.set_efficiency_discharge(0.85)
ps_hydro_step.set_efficiency_charge(0.85)

ps_hydro_step.set_rup(0.99) # 99%Pn / hour
ps_hydro_step.set_rdo(0.99) # 99%Pn / hour


#--------------------------
# Final object
#--------------------------

techno[index] = Techno('storage','step','charge', pe_hydro_step_c, pt_hydro_step_c, ps_hydro_step)
index = index + 1

techno[index] = Techno('storage','step','discharge', pe_hydro_step_d, pt_hydro_step_d, ps_hydro_step)
index = index + 1