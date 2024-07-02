############################
# Gas - CCGT (Combined Cycle Gas Turbine)¶
############################

#--------------------------
# Technical parameters
#--------------------------

pt_gas_ccgt = prm_tech()
pt_gas_ccgt.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_gas_ccgt.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

pt_gas_ccgt.set_A({(y,w): 0.8 for y in years for w in weeks}) # Availability factor


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
data_co2_year = [2000,2020,2050]
data_var_co2  = [0,cost_co2_2020*co2*1e-6*1e3,cost_co2_2050*co2*1e-6*1e3] # €/MWh
pe_gas_ccgt.set_var_co2(data_var_co2, data_co2_year)
# VAR MI
data_var_mi   = None # €/MWh
pe_gas_ccgt.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_gas_ccgt = prm_dispatchable()
ps_gas_ccgt.set_rup(0.99) # 99%Pn / hour
ps_gas_ccgt.set_rdo(0.99) # 99%Pn / hour

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
#source : https://fr.wikipedia.org/wiki/Centrale_thermique_de_Bouchain + https://assets.rte-france.com/analyse-et-donnees/2023-11/2023-10-16-chapitre3-production-stockage-electricite.pdf (P46)
hist_data_inv.update({2005 : 790 , 2006 : 0 , 2007 : 0 , 2008 : 0 ,2009 : 412 , 2010 : 860 + 424 + 489 , 2011 : 435 + 408 + 430 , 2012 : 465 , 2013 : 413 + 465 , 2014 : 0 , 2015 : 0 , 2016 : 605 , 2022 : 446 , 2023 : 0 })
hist_data_capa.update({2019 : 6196 , 2020 : 6196 , 2021: 6196 , 2022 : 6196, 2023 : 6642, 2024 : 6642}) # 6642

# Set data
pt_gas_ccgt.set_historic_data('CAPA',hist_data_capa)
pt_gas_ccgt.set_historic_data('INV',hist_data_inv)
pt_gas_ccgt.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_gas_ccgt.set_InvMax({y: 100e3 for y in range(years.start-1, years.stop-1)})

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','gas','ccgt', pe_gas_ccgt, pt_gas_ccgt, ps_gas_ccgt)
index = index + 1
