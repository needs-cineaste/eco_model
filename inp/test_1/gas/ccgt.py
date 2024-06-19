############################
# Gas - CCGT (Combined Cycle Gas Turbine)¶
############################

#--------------------------
# Technical parameters
#--------------------------

pt_gas_ccgt = prm_tech()
pt_gas_ccgt.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_gas_ccgt.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

# CO2 emission rate - g/kWh
# https://www.acer.europa.eu/sites/default/files/documents/Official_documents/Acts_of_the_Agency/Opinions/Documents/ACERs%20Opinion%2022-2019%20examples%20of%20calculation.pdf
co2 = 374
pt_gas_ccgt.set_CO2(co2)

#--------------------------
# Economical parameters
#--------------------------

#Source : CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - CCG Methane pour CAPEX et OPEX fixes et p937 CCG gaz fossile pour OPEX variable
pe_gas_ccgt = prm_eco()
pe_gas_ccgt.set_r(r)

lt = 40
ct = 2 # construction time
pe_gas_ccgt.set_lt(lt)

# FIX CAPEX
data_occ_years = None # Available data for data
data_occ       = 900e3 # CAPEX en €/MW sans intercalaire
pe_gas_ccgt.calculate_capex_dict(data_occ,ct,lt,pe_gas_ccgt.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None
pe_gas_ccgt.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   = 40e3 # €/MW/an
pe_gas_ccgt.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_gas_ccgt.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = 4.2 # €/MWh - https://www.eia.gov/electricity/annual/html/epa_08_04.html
pe_gas_ccgt.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = 50 # €/MWh - Data to adjust !  Reference to find for the long term gas price ...
pe_gas_ccgt.set_var_f(data_var_f)
# VAR CO2
data_co2_year = [2020,2050]
data_var_co2  = [50 * co2*1e-6*1e3,1000 * co2*1e-6*1e3] # €/MWh
pe_gas_ccgt.set_var_co2(data_var_co2, data_co2_year)
# VAR MI
data_var_mi   = None # €/MWh
pe_gas_ccgt.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_gas_ccgt = prm_dispatchable()

#--------------------------
# Historical Capacities
#--------------------------

# Investment defined until 2018
hist_data_inv = {y: 0.2e3 for y in range(years[0]-60,years[0])}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(years[0] - 60, years[0])}
for y in range(years[0] - 60, years[0]):
    if y > years[0] - 30:
        hist_data_dec[y] = 0.1e3
# Historical needed Capacity
hist_data_capa = {}
hist_data_capa[2019] = 18.54e3

# Set data
pt_gas_ccgt.set_historic_data('CAPA',hist_data_capa)
pt_gas_ccgt.set_historic_data('INV',hist_data_inv)
pt_gas_ccgt.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_gas_ccgt.set_InvMax({y: 100e3 for y in years})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','gas','ccgt', pe_gas_ccgt, pt_gas_ccgt, ps_gas_ccgt)
index = index + 1
