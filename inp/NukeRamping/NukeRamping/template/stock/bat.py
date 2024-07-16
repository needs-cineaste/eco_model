############################
# HYDRO - STEP
############################

#----------------------------------------------------------------
# Technical parameters  CHARGE
#----------------------------------------------------------------

pt_stock_bat_c = prm_tech()

pt_stock_bat_c.set_isPvar({y: True for y in years})

pt_stock_bat_c.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})  # Energy is endogeneous

#--------------------------
# Economical parameters - STEP Charge
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 939 - STEP -

pe_stock_bat_c = prm_eco()
pe_stock_bat_c.set_r(r)
lt = 15
ct = 1 # construction time

pe_stock_bat_c.set_lt(lt)

# FIX OM
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data
data_occ   =  [740 , 550 , 427  , 370 , 370] # €/MW/an
pe_stock_bat_c.calculate_capex_dict(data_occ,ct,lt,pe_stock_bat_c.get_r(),data_occ_years)

# FIX DEP
data_fix_dep = None # €/MW/an -> RTE : CAPEX = 1000 => /2 because charge discharge => 29e3 annual (!)
pe_stock_bat_c.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  15e3  # €/MW/an
pe_stock_bat_c.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_stock_bat_c.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_stock_bat_c.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_stock_bat_c.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_stock_bat_c.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_stock_bat_c.set_var_mi(data_var_mi)


#--------------------------
# Historical Capacities
#--------------------------
# Investment defined until 2018
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity
hist_data_capa = {}
# https://analysesetdonnees.rte-france.com/bilan-electrique-2023/flexibilites#Stockage
hist_data_inv.update({2018 : 16.1 , 2019 : 67.3 , 2020 : 232.6 , 2021 : 174 , 2022 : 317}) # En MW
# Source CINEASTE/data/source/Solaire_Evolution_puissance_inst - reférence : SDES
hist_data_capa.update({2019 : 16.1 , 2020 : 83.4 , 2021 : 316 , 2022 : 490 , 2023 : 807 }) 

# Set data
pt_stock_bat_c.set_historic_data('CAPA',hist_data_capa)
pt_stock_bat_c.set_historic_data('INV',hist_data_inv)
pt_stock_bat_c.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_stock_bat_c.set_InvMax({y: 10e3 for y in range(years.start-1, years.stop-1)})


#----------------------------------------------------------------
# Technical parameters  DISCHARGE
#----------------------------------------------------------------

pt_stock_bat_d = prm_tech()

pt_stock_bat_d.set_isPvar({y: False for y in years})
pt_stock_bat_d.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})  # Energy is endogeneous

pt_stock_bat_d.set_P(5394)

#--------------------------
# Economical parameters - STEP discharge
#--------------------------

#Source CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 939 - STEP -

pe_stock_bat_d = prm_eco()
pe_stock_bat_d.set_r(r)
lt = 15
ct = 1 # construction time
pe_stock_bat_d.set_lt(lt)

# FIX OM
data_occ_years = [2020,2030,2040,2050,2060] # Available data for data
data_occ   =  [740 , 550 , 427  , 370 , 370] # €/MW/an
pe_stock_bat_d.set_fix_om(data_occ,data_occ_years)
pe_stock_bat_d.calculate_capex_dict(data_occ,ct,lt,pe_stock_bat_d.get_r(),data_occ_years)

# FIX DEP
data_fix_dep = None # €/MW/an -> RTE : CAPEX = 1000 => /2 because charge discharge => 29e3 annual (!)
pe_stock_bat_d.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  15e3  # €/MW/an
pe_stock_bat_d.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_stock_bat_d.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_stock_bat_d.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = None # €/MWh -
pe_stock_bat_d.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_stock_bat_d.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_stock_bat_d.set_var_mi(data_var_mi)

#--------------------------
# Historical Capacities
#--------------------------
# Investment defined until 2018
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity
hist_data_capa = {}
# https://analysesetdonnees.rte-france.com/bilan-electrique-2023/flexibilites#Stockage
hist_data_inv.update({2018 : 16.1 , 2019 : 67.3 , 2020 : 232.6 , 2021 : 174 , 2022 : 317}) # En MW
# Source CINEASTE/data/source/Solaire_Evolution_puissance_inst - reférence : SDES
hist_data_capa.update({2019 : 16.1 , 2020 : 83.4 , 2021 : 316 , 2022 : 490 , 2023 : 807 }) 

# Set data
pt_stock_bat_d.set_historic_data('CAPA',hist_data_capa)
pt_stock_bat_d.set_historic_data('INV',hist_data_inv)
pt_stock_bat_d.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_stock_bat_d.set_InvMax({y: 10e3 for y in range(years.start-1, years.stop-1)})



#--------------------------
# Specific parameters for Storage
#--------------------------

ps_stock_bat = prm_storage()

ps_stock_bat.set_level_max_time(4) # 4 h 
ps_stock_bat.set_level_min(0)
ps_stock_bat.set_level_start(0)

ps_stock_bat.set_efficiency_discharge(0.95)
ps_stock_bat.set_efficiency_charge(0.95)

ps_stock_bat.set_is_P_sym(True)

ps_stock_bat.set_rup(1) # 99%Pn / hour
ps_stock_bat.set_rdo(1) # 99%Pn / hour


#--------------------------
# Final object
#--------------------------
index_step = index
techno[index] = Techno('storage','bat_4h','charge', pe_stock_bat_c, pt_stock_bat_c, ps_stock_bat)
index = index + 1

techno[index] = Techno('storage','bat_4h','discharge', pe_stock_bat_d, pt_stock_bat_d, ps_stock_bat)
index = index + 1