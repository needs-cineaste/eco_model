############################
# Nuclear - New
############################

#--------------------------
# Technical parameters
#--------------------------

pt_nuclear_new = prm_tech(years,hours)
pt_nuclear_new.set_isPvar({y: True for y in years}) # Capacity is endogeneous
pt_nuclear_new.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours}) # Energy is endogeneous

#--------------------------
# Economical parameters
#--------------------------

# Source : ISTE chap 2
pe_nuclear_new = prm_eco(years)
pe_nuclear_new.set_r(r)


#pe_nuclear_new.set_fix_cap(500e3)
occ, ct, dt = 5.5e6, 10, 60
pe_nuclear_new.calculate_capex(occ,ct,dt,r) # 383e3

# Fix Costs - Staff, external consumption, Central functions, taxes - CdC 2014 : 120 €/kW
pe_nuclear_new.set_fix_om(120e3)
pe_nuclear_new.set_fix_mi(0)
pe_nuclear_new.set_var_om(13)
pe_nuclear_new.set_var_f(8)
pe_nuclear_new.set_var_co2(0)
pe_nuclear_new.set_var_mi(0)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_nuclear_new = prm_dispatchable()

ps_nuclear_new.set_rup(0.10) # 10%Pn / hour
ps_nuclear_new.set_rdo(0.10) # 10%Pn / hour


#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','nuclear','new', pe_nuclear_new, pt_nuclear_new, ps_nuclear_new)
index = index + 1
