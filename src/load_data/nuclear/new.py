############################
# Nuclear - New
############################

# Technical parameters
pt_nuclear_new = prm_tech(years,hours)
pt_nuclear_new.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_nuclear_new.set_isEvar({(y,h): True for y in years for h in hours}) # Energy is endogeneous

# Economical parameters
# Source : ISTE chap 2
pe_nuclear_new = prm_eco(r)
pe_nuclear_new.set_occ(5.5e6) 
pe_nuclear_new.set_ct(10)
pe_nuclear_new.set_dt(60)

# Fix Costs - Staff, external consumption, Central functions, taxes - CdC 2014 : 120 €/kW
pe_nuclear_new.set_fix_om(120e3)
pe_nuclear_new.set_var_om(13)
pe_nuclear_new.set_var_f(8)
pe_nuclear_new.set_var_co2(0)

tec_nuclear_new = Techno('nuclear','new', pe_nuclear_new, pt_nuclear_new)
#tec_nuclear_new.Print()

data_techno[index] = copy.deepcopy(tec_nuclear_new)
index = index + 1
