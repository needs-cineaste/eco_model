############################
# Nuclear - New
############################

#--------------------------
# Technical parameters
#--------------------------

pt_nuclear_new = prm_tech()

pt_nuclear_new.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_nuclear_new.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

pt_nuclear_new.set_A({(y,w): 0.80 for y in years for w in weeks}) # Availability factor

#--------------------------
# Economical parameters
#--------------------------

#Source : CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - CCG Methane pour CAPEX et OPEX fixes et p937 CCG gaz fossile pour OPEX variable
pe_nuclear_new = prm_eco()
pe_nuclear_new.set_r(r)

lt = 60
ct = 10 # construction time
pe_nuclear_new.set_lt(lt)
pe_nuclear_new.set_deco_cost(350e6/1e3) # 350e6 €/reactor


# FIX CAPEX
# https://www.usinenouvelle.com/article/cout-design-calendrier-les-nouveaux-reacteurs-nucleaires-epr2-d-edf-encore-flous.N2210775
data_occ_years = None # Available data for data
data_occ       = 6.77e6 # OCC en €/MW sans intercalaire
pe_nuclear_new.calculate_capex_dict(data_occ,ct,lt,pe_nuclear_new.get_r(),data_occ_years)
# FIX DEP
data_fix_dep = None # €/MW/an -> Loyer économique => 186 (Amort. CAPEX RTE) - data_fix_om
pe_nuclear_new.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   = 120e3 # €/MW/an
pe_nuclear_new.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_nuclear_new.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # Var OM - 13 or None depends on fix OM or not ... To dig ! 
pe_nuclear_new.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = 8 # Var Fuel - Data is based on ISTE Economy of Energy
pe_nuclear_new.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_nuclear_new.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_nuclear_new.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_nuclear_new = prm_dispatchable()

ps_nuclear_new.set_rup(nuke_new_rup) #Pn / hour
ps_nuclear_new.set_rdo(nuke_new_rdo) #Pn / hour

#--------------------------
# Historical Capacities
#--------------------------

# Investment defined until 2018
hist_data_inv = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Decommissioning defined until 2018
hist_data_dec = {y: 0.0 for y in range(start_world, start_of_scenario)}
# Historical needed Capacity 
hist_data_capa = {}
hist_data_capa[start_of_scenario-1] = 0.0e3

# Set data
pt_nuclear_new.set_historic_data('CAPA',hist_data_capa)
pt_nuclear_new.set_historic_data('INV',hist_data_inv)
pt_nuclear_new.set_historic_data('DEC',hist_data_dec)

# Maximum investment
pt_nuclear_new.set_InvMax({y: nuclear_invest_max for y in range(years.start-1, years.stop-1)})


#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','nuclear','new', pe_nuclear_new, pt_nuclear_new, ps_nuclear_new)
index = index + 1
