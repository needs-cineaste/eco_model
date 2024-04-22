############################
# REN - Wind On Shore
############################

#--------------------------
# Technical parameters
#--------------------------

pt_ren_won = prm_tech(years,hours)
pt_ren_won.set_isPvar({y: True for y in years})
pt_ren_won.set_isEvar({(y,w,h): True for y in years for w in weeks for h in hours})

# Define won LF at y and h
#won_lf = np.loadtxt('../data/formatted/ren/wind/onshore/2019.inc').tolist()
#dict_won_lf = {(y, h): won_lf[h-1] for y in years for h in hours}
#pt_ren_won.set_LF(copy.deepcopy(dict_won_lf))

# Get 52 weeks of data
won_lf = np.loadtxt('../data/formatted/ren/wind/onshore/2019.inc').tolist()[:int(7*24*52)]
# Build dataframe with matrix form
won_lf_reshape = pd.DataFrame(np.array(won_lf).reshape(-1, 7 * 24))
# Get list of demand groupby 
group = np.arange(len(won_lf_reshape)) // (52 / number_of_mean_weeks)
# Select a random index from the filtered indices
won_lf_random = pd.DataFrame()
for week in range(number_of_mean_weeks):
    won_lf_random = pd.concat([won_lf_random, pd.DataFrame([won_lf_reshape.iloc[random.choice(np.where(group == week)[0])]])], ignore_index=True)
# Iterate over the DataFrame and populate the dictionary demand
dict_won_lf = {(y,w,h): won_lf_random.iloc[w-1,h-1] for y in years for w in weeks for h in hours}
# Build the dict
pt_ren_won.set_LF(copy.deepcopy(dict_won_lf))

#--------------------------
# Economical parameters
#--------------------------
# PIF
pe_ren_won = prm_eco(years)
pe_ren_won.set_r(r)

occ, ct, dt = 2e6, 1, 30
pe_ren_won.calculate_capex(occ,ct,dt,r) # 383e3

# PIF
pe_ren_won.set_fix_om(60)
pe_ren_won.set_fix_mi(0)
pe_ren_won.set_var_om(0)
pe_ren_won.set_var_f(0)
pe_ren_won.set_var_co2(0)
pe_ren_won.set_var_mi(0)

#--------------------------
# Specific parameters for Fatal
#--------------------------

ps_ren_won = prm_fatal()

#--------------------------
# Final object
#--------------------------

techno[index] = Techno('fatal','ren','won', pe_ren_won, pt_ren_won, ps_ren_won)
index = index + 1
