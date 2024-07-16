############################
# Gas - Congeneration (
############################


if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("No argument provided for won.py... Please provide a path.")
    sys.exit()

#--------------------------
# Technical parameters
#--------------------------

pt_gas_cogen = prm_tech()
pt_gas_cogen.set_isPvar({y: False for y in years}) # Capacity is endogeneous
pt_gas_cogen.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

# Source : https://assets.rte-france.com/analyse-et-donnees/2023-11/2023-10-16-chapitre3-production-stockage-electricite.pdf 
data_P_years = [2020 , 2030 , 2045 , 2050]
data_P       = [4900 , 4900 , 2000 , 2000]
    
pt_gas_cogen.set_P(data_P,data_P_years)

#--------------------------
# Weeks managment
#--------------------------
if profil_weeks == 'average' or  profil_weeks == "M4" :
    
    cogen_lf_average = lake_lf_reshape.groupby(group).mean()
    dict_cogen_lf = {(y,w,h): lake_lf_average.iloc[w-1, h-1] for y in years for w in weeks for h in hours}

elif profil_weeks == 'maxmin':
    print('Not yet implemented ... EXIT(1)')
    exit()

pt_gas_cogen.set_LF(copy.deepcopy(dict_lake_lf))

# Energy
pt_gas_cogen.set_isEvar({(y,w,h): False for y in years for w in weeks for h in hours})
E = {(y,w,h): pt_gas_cogen.get_P()[y] * dict_cogen_lf[y,w,h] for y in years for w in weeks for h in hours}
pt_gas_cogen.set_E(copy.deepcopy(E))

# CO2 emission rate - g/kWh
# CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 944
co2 = 495 #kgCO2/MWh
pt_gas_cogen.set_CO2(co2)

#--------------------------
# Economical parameters
#--------------------------

#Source : CINEASTE/data/source/annexes_rappor_2050_RTE/Chapitre 11, p 938 - CCG Methane pour CAPEX et OPEX fixes et p937 CCG gaz fossile pour OPEX variable
pe_gas_cogen = prm_eco()
pe_gas_cogen.set_r(r)

lt = 40
ct = None # construction time
pe_gas_cogen.set_lt(lt)
pe_gas_cogen.set_deco_cost(0) # don't know

# FIX CAPEX
data_occ_years = None # Available data for data
data_occ       = None # CAPEX
# FIX DEPm
data_fix_dep = 94e3 # €/MW/an
pe_gas_cogen.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   = 0 # €/MW/an
pe_gas_cogen.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_gas_cogen.set_fix_mi(data_fix_mi)
# VAR OM                     ######### ATTENTIOn A rétudier - ICI VALEUR DE RTE MAIS AVEC PRIX GAZ FAIBLE ? 
data_var_om   = 30 # €/MWh - 
pe_gas_cogen.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = 0 # €/MWh - Data to adjust !  Reference to find for the long term gas price ...
pe_gas_cogen.set_var_f(data_var_f)
# VAR CO2
data_co2_year = [2000,2020,2050]
data_var_co2  = [0,cost_co2_2020*co2*1e-6*1e3,cost_co2_2050*co2*1e-6*1e3] # €/MWh
pe_gas_cogen.set_var_co2(data_var_co2, data_co2_year)
# VAR MI
data_var_mi   = None # €/MWh
pe_gas_cogen.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_gas_cogen = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','gas','cogen', pe_gas_cogen, pt_gas_cogen, ps_gas_cogen)
index = index + 1
