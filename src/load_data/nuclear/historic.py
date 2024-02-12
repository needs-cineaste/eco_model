############################
# Nuclear - Historic
############################

nuclear_hist_lifetime = 40 # either 40, 50 or 60

#--------------------------
# Technical parameters
#--------------------------

pt_nuclear_hist = prm_tech(years,hours)

# Power trajectory
pt_nuclear_hist.set_isPvar({y: False for y in years}) # Capacity is exogeneous

# Capa installed
P = {}
df = pd.read_csv('../data/formatted/nuclear/capa_hist.dat', delim_whitespace=True, names=['Year', '40y', '50y', '60y'])
filtered_df = df[(df['Year'] >= years[0]) & (df['Year'] <= years[len(years)-1])]
if nuclear_hist_lifetime == 40:
    P = filtered_df.set_index('Year')[['40y']].to_dict()['40y']
if nuclear_hist_lifetime == 50:
    P = filtered_df.set_index('Year')[['50y']].to_dict()['50y']
if nuclear_hist_lifetime == 60:
    P = filtered_df.set_index('Year')[['60y']].to_dict()['60y']

pt_nuclear_hist.set_P(copy.deepcopy(P))

pt_nuclear_hist.set_isEvar({(y,h): True for y in years for h in hours})  # Energy is endogeneous

pt_nuclear_hist.set_rup(0.10) # 10%Pn / hour
pt_nuclear_hist.set_rdo(0.10) # 10%Pn / hour

#--------------------------
# Economical parameters
#--------------------------

pe_nuclear_hist = prm_eco(years)
pe_nuclear_hist.set_r(r)
# CAPEX is not required because P is exogeneous
# CAPEX is calculated to get a correct historical fleet cost 
# [TO REDO]
pe_nuclear_hist.set_occ(0.20 * 2e6) # Tell that 80% is deprecated - 2Md / MW -> To change !
pe_nuclear_hist.set_ct(10)
pe_nuclear_hist.set_dt(50)

# Fix Costs - Staff, external consumption, Central functions, taxes - CdC 2014 : 120 €/kW
pe_nuclear_hist.set_fix_om(120e3)
pe_nuclear_hist.set_fix_mi(0)

pe_nuclear_hist.set_var_om(13)
# Hansen & Percebois - Energie p 307
pe_nuclear_hist.set_var_f(3)
# ADEME 6g/kWh - EDF 4g/kWh
# [TO REDO]
#pe_nuclear_hist.set_var_co2(cost_co2 * 1e-6 * 1e-6 * 6 * 1e3)
pe_nuclear_hist.set_var_co2(0)
pe_nuclear_hist.set_var_mi(0)

pe_nuclear_hist.update_costs()

tec_nuclear_hist = Techno('nuclear','hist', pe_nuclear_hist, pt_nuclear_hist)
#tec_nuclear_hist.Print()

data_techno[index] = copy.deepcopy(tec_nuclear_hist)
index = index + 1
