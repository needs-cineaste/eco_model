############################
# Gas - CCGT (Combined Cycle Gas Turbine)¶
############################

# Technical parameters
pt_gas_ccgt = prm_tech(years,hours)
pt_gas_ccgt.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_gas_ccgt.set_isEvar({(y,h): True for y in years for h in hours}) # Energy is endogeneous

# Economical parameters
# PIF
pe_gas_ccgt = prm_eco(r)
pe_gas_ccgt.set_occ(1.0e6) 
pe_gas_ccgt.set_ct(3)
pe_gas_ccgt.set_dt(30)

# PIF
pe_gas_ccgt.set_fix_om(15)
pe_gas_ccgt.set_var_om(1.5)
pe_gas_ccgt.set_var_f(100)
pe_gas_ccgt.set_var_co2(50)

tec_gas_ccgt = Techno('gas','ccgt', pe_gas_ccgt, pt_gas_ccgt)

#tec_gas_ccgt.Print()

data_techno[index] = copy.deepcopy(tec_gas_ccgt)
index = index + 1
