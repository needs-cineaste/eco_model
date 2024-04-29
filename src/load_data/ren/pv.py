############################
# REN - PV
############################

#--------------------------
# Technical parameters
#--------------------------

pt_ren_pv = prm_tech(years,hours)
pt_ren_pv.set_isPvar({y: True for y in years})
pt_ren_pv.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})

# Define PV LF at y,w,h
#pv_lf = np.loadtxt('../data/formatted/ren/solar/pv/2019.inc').tolist()
#dict_pv_lf = {(y, h): pv_lf[h-1] for y in years for h in hours}
#pt_ren_pv.set_LF(copy.deepcopy(dict_pv_lf))

# Get 52 weeks of data
pv_lf = np.loadtxt('../data/formatted/ren/solar/pv/2019.inc').tolist()[:int(7*24*52)]
# Build dataframe with matrix form
pv_lf_reshape = pd.DataFrame(np.array(pv_lf).reshape(-1, 7 * 24))
# Get list of demand groupby 
group = np.arange(len(pv_lf_reshape)) // (52 / number_of_mean_weeks)
# Select a random index from the filtered indices
pv_lf_random = pd.DataFrame()
for week in range(number_of_mean_weeks):
    pv_lf_random = pd.concat([pv_lf_random, pd.DataFrame([pv_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
# Iterate over the DataFrame and populate the dictionary demand
dict_pv_lf = {(y,w,h): pv_lf_random.iloc[w-1,h-1] for y in years for w in weeks for h in hours}
# Build the dict
pt_ren_pv.set_LF(copy.deepcopy(dict_pv_lf))

#--------------------------
# Economical parameters
#--------------------------
# PIF
pe_ren_pv = prm_eco(years)
pe_ren_pv.set_r(r)

occ, ct, dt = 1.7e6, 1, 25
pe_ren_pv.calculate_capex(occ,ct,dt,r) # 383e3

# PIF
pe_ren_pv.set_fix_om(20)
pe_ren_pv.set_fix_mi(0)
pe_ren_pv.set_var_om(0)
pe_ren_pv.set_var_f(0)
pe_ren_pv.set_var_co2(0)
pe_ren_pv.set_var_mi(0)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_pv = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','pv', pe_ren_pv, pt_ren_pv, ps_ren_pv)
index = index + 1
