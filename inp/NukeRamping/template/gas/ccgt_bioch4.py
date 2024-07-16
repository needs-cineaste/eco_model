############################
# Gas - CCG (Combined Cycle Gas Methane)¶
############################

#--------------------------
# Technical parameters
#--------------------------

pt_gas_ccgt_bioch4 = prm_tech()
pt_gas_ccgt_bioch4.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_gas_ccgt_bioch4.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

pt_gas_ccgt_bioch4.set_A({(y,w): 0.8 for y in years for w in weeks}) # Availability factor

#--------------------------
# Economical parameters
#--------------------------

#Source : CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - CCG Methane pour CAPEX et OPEX fixes et p937 CCG gaz fossile pour OPEX variable
pe_gas_ccgt_bioch4 = prm_eco()
pe_gas_ccgt_bioch4.set_r(r)

lt = 40
ct = 2 # construction time
pe_gas_ccgt_bioch4.set_lt(lt)
pe_gas_ccgt_bioch4.set_deco_cost(0) # don't know

# FIX CAPEX
#data_occ_years = None # Available data for data
#data_occ       = 1000e3 # CAPEX en €/MW sans intercalaire - Limiter le déploiement avant 2040!! 

data_occ_years = [2020  ,2030  ,2034  ,2035  ,2040  ,2050  ,2060]
data_occ       = [1000e6,1000e6,1000e6,1000e3,1000e3,1000e3,1000e3] # €/MWh PIF 


pe_gas_ccgt_bioch4.calculate_capex_dict(data_occ,ct,lt,pe_gas_ccgt_bioch4.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None
pe_gas_ccgt_bioch4.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   = 40e3 # €/MW/an
pe_gas_ccgt_bioch4.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_gas_ccgt_bioch4.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = 4.2 # €/MWh - https://www.eia.gov/electricity/annual/html/epa_08_04.html
pe_gas_ccgt_bioch4.set_var_om(data_var_om)
# VAR Fuel
data_var_f_year = [2020,2030,2040,2050,2060]
data_var_f      = [100,100 ,100 ,100 ,100] # €/MWh PIF 
pe_gas_ccgt_bioch4.set_var_f(data_var_f,data_var_f_year)
# VAR CO2
data_var_co2 = None
pe_gas_ccgt_bioch4.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None # €/MWh
pe_gas_ccgt_bioch4.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_gas_ccgt_bioch4 = prm_dispatchable()
ps_gas_ccgt_bioch4.set_rup(0.99) # 99%Pn / hour
ps_gas_ccgt_bioch4.set_rdo(0.99) # 99%Pn / hour

#--------------------------
# Historical Capacities
#--------------------------

# Investment defined until 2018
hist_data_inv = {y: 0 for y in range(years[0]-60,years[0])}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(years[0] - 60, years[0])}
for y in range(years[0] - 60, years[0]):
    if y > years[0] - 30:
        hist_data_dec[y] = 0.1e3
# Historical needed Capacity
hist_data_capa = {}
# Investment defined until 2018
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity 
hist_data_capa = {}
hist_data_capa[start_of_scenario-1] = 0.0e3

# Set data
pt_gas_ccgt_bioch4.set_historic_data('CAPA',hist_data_capa)
pt_gas_ccgt_bioch4.set_historic_data('INV',hist_data_inv)
pt_gas_ccgt_bioch4.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_gas_ccgt_bioch4.set_InvMax({y: 3e3 for y in range(years.start-1, years.stop-1)})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','gas','ccgt_bioch4', pe_gas_ccgt_bioch4, pt_gas_ccgt_bioch4, ps_gas_ccgt_bioch4)
index = index + 1
