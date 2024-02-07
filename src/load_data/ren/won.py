############################
# REN - Wind On Shore
############################

# Technical parameters
pt_ren_won = prm_tech(years,hours)
pt_ren_won.set_isPvar({y: True for y in years})
pt_ren_won.set_isEvar({(y,h): True for y in years for h in hours})
pt_ren_won.set_isFatal(True)

# Define won LF at y and h
won_lf = np.loadtxt('../data/formatted/ren/wind/onshore/2019.inc').tolist()
dict_won_lf = {(y, h): won_lf[h-1] for y in years for h in hours}
pt_ren_won.set_LF(copy.deepcopy(dict_won_lf))

# Economical parameters
# PIF
pe_ren_won = prm_eco(r)
pe_ren_won.set_occ(2e6) 
pe_ren_won.set_ct(1)
pe_ren_won.set_dt(30)

# PIF
pe_ren_won.set_fix_om(60)
pe_ren_won.set_var_om(0)
pe_ren_won.set_var_f(0)
pe_ren_won.set_var_co2(0)

tec_ren_won = Techno('ren','won', pe_ren_won, pt_ren_won)
#tec_ren_won.Print()

data_techno[index] = copy.deepcopy(tec_ren_won)
index = index + 1
