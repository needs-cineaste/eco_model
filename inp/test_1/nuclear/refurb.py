############################
# Nuclear - Refurbishment
############################

# Technical parameters
pt_nuclear_ref = prm_tech(years,hours)
pt_nuclear_ref.set_isPvar(True) # Capacity is exogeneous
pt_nuclear_ref.set_isEvar(True)  # Energy is endogeneous
pt_nuclear_ref.set_P(61.4e3)

# Economical parameters
pe_nuclear_ref = prm_eco(r)
# CAPEX is not required because P is exogeneous
# [TO REDO]
pe_nuclear_ref.set_occ(1.0e6) # Tell that 80% is deprecated - 100 Md €
pe_nuclear_ref.set_ct(10)
pe_nuclear_ref.set_dt(20)

# Fix Costs - Staff, external consumption, Central functions, taxes - CdC 2014 : 120 €/kW
pe_nuclear_ref.set_fix_om(120e3)
pe_nuclear_ref.set_var_om(13)
# Hansen & Percebois - Energie p 307
pe_nuclear_ref.set_var_f(3)
# ADEME 6g/kWh - EDF 4g/kWh
# [TO REDO]
pe_nuclear_ref.set_var_co2(cost_co2 * 1e-6 * 1e-6 * 6 * 1e3)

tec_nuclear_ref = Techno('nuclear','refu', pe_nuclear_ref, pt_nuclear_ref)
#tec_nuclear_ref.Print()

data_techno[index] = copy.deepcopy(copy.deepcopy(tec_nuclear_ref)
index = index + 1
