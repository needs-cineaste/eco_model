############################
# Nuclear - Historic
############################

#--------------------------
# Technical parameters
#--------------------------

pt_nuclear_hist = prm_tech()

# Power trajectory
pt_nuclear_hist.set_isPvar({y: False for y in years}) # Capacity is exogeneous

# Capa installed
df = pd.read_csv('../../../data/formatted/nuclear/capa_hist.dat', sep='\s+', names=['Year', '40y', '50y', '60y'])
data_P_years=list(df["Year" ])
if nuclear_hist_lifetime == 40:
    data_P = list(df["40y"])
    refu_annual_cost = 0
if nuclear_hist_lifetime == 50:
    data_P = list(df["50y"])
    refu_annual_cost = 50e9 / 60e3 / 20 # REDO Better
if nuclear_hist_lifetime == 60:
    data_P = list(df["60y"])
    refu_annual_cost = 50e9*2 / 60e3 / 30 # REDO Better
pt_nuclear_hist.set_P(data_P,data_P_years)

pt_nuclear_hist.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})  # Energy is endogeneous

#--------------------------
# Economical parameters
#--------------------------

pe_nuclear_hist = prm_eco()
pe_nuclear_hist.set_r(r)

lt = nuclear_hist_lifetime
ct = 5 # construction time
pe_nuclear_hist.set_lt(lt)
pe_nuclear_hist.set_deco_cost(350e6/1e3) # 350e6 €/reactor

#
# !! HERE, The Grand Carénage (refurbishment) is not taken into account !!
#
# FIX CAP - Here Null
# pe_nuclear_hist.calculate_capex_dict(None,ct,lt,pe_nuclear_hist.get_r())
# FIX DEP
data_fix_dep = 66e3 + refu_annual_cost # €/MW/an -> Loyer économique => 186 (Amort. CAPEX RTE) - data_fix_om + refurbishment
pe_nuclear_hist.set_fix_dep(data_fix_dep)
# FIX OM
data_fix_om   =  120e3  # €/MW/an -> ISTE
pe_nuclear_hist.set_fix_om(data_fix_om)
# FIX MI
data_fix_mi   = None # €/MW/an
pe_nuclear_hist.set_fix_mi(data_fix_mi)
# VAR OM
data_var_om   = None # €/MWh -
pe_nuclear_hist.set_var_om(data_var_om)
# VAR Fuel
data_var_f    = 8 # €/MWh - ISTE
pe_nuclear_hist.set_var_f(data_var_f)
# VAR CO2
data_var_co2 = None
pe_nuclear_hist.set_var_co2(data_var_co2)
# VAR MI
data_var_mi   = None
pe_nuclear_hist.set_var_mi(data_var_mi)

#--------------------------
# Specific parameters for Dispatchable
#--------------------------

ps_nuclear_hist = prm_dispatchable()

ps_nuclear_hist.set_rup(0.10) # 10%Pn / hour
ps_nuclear_hist.set_rdo(0.10) # 10%Pn / hour

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('dispatchable','nuclear','hist', pe_nuclear_hist, pt_nuclear_hist, ps_nuclear_hist)
#techno_D[index] = copy.deepcopy(tec_nuclear_hist)
index = index + 1
