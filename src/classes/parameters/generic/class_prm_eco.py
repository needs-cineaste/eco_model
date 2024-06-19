class prm_eco:
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self):
        self._r        = None  # Discount rate
        self._fix_cap  = None  # Annual CAPEX [€/MW/y]
        self._fix_dep  = None  # annuel Depreciation [€/MW/y] if there is no CAPEX
        self._fix_ref  = None  # Refurbishment investment [€/MW/y]

        self._is_cap   = False # Tell if there is a capex with historical data
        self._is_dep   = False # Tell if there is a anuity without any historical data

        self._fix_om   = None  # Fix OM cost [€/MW/y]
        self._fix_mi   = None  # Misc Fix cost [€/MW/y] => Sum of other fixed costs
        self._var_om   = None  # var OM cost [€/MWh ouput]
        self._var_f    = None  # var fuel cost [€/MWh input]
        self._var_co2  = None  # var carbon cost [€/MWh i]
        self._var_mi   = None  # Misc var [€/MWh i] => Sum of other variable costs
        self._lt       = None  # Life time of the technolog

# --------------------- End Of Constructor ---------------------------------------------------------------------------    
#    def calculate_capex(self, occ, ct, dt, r, y):
#        tic = occ / ct * ( (1 + r[y]) / r[y] ) * ( (1 + r[y])**ct - 1)
#        capex = tic * ( ( r[y] * ( 1 + r[y] )**dt ) / ( (1 + r[y])**dt - 1) ) 
#        self._fix_cap = capex

    def calculate_capex_dict(self,occ,ct,dt,r,yd_l=None) : #occ_l : liste data capex ou element simple | yd_l : list des année connu (si necessaire) | ct : temps de construction
        #| dt = temps de vie
        if occ is None :
            self._is_cap = False
            self._fix_cap={0 for y in years_world}
            print(" WARNING, CAPEX is 0")
        # occ_l Liste - regression lineaire entre éléments connu
        elif isinstance(occ, list) :
            self._is_cap = True
            occ_l= np.interp(years_world,yd_l,occ)
            capex={}
            for i, y in enumerate(years_world):
                tic = occ_l[i] / ct * ( (1 + r[y]) / r[y] ) * ( (1 + r[y])**ct - 1)
                capex[y] = tic * ( ( r[y] * ( 1 + r[y] )**dt ) / ( (1 + r[y])**dt - 1) )
            self._fix_cap = capex
        # occ is a float
        else :
            self._is_cap = True
            capex={}
            for i, y in enumerate(years_world):
                tic = occ / ct * ( (1 + r[y]) / r[y] ) * ( (1 + r[y])**ct - 1)
                capex[y] = tic * ( ( r[y] * ( 1 + r[y] )**dt ) / ( (1 + r[y])**dt - 1) )
            self._fix_cap = capex

# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_r(self):
        return self._r
    def get_fix_cap(self):
        return self._fix_cap
    def get_fix_dep(self):
        return self._fix_dep
    def get_fix_ref(self):
        return self._fix_ref

    def is_cap(self):
        return self._is_cap
    def is_dep(self):
        return self._is_dep
    
    def get_fix_om(self):
        return self._fix_om
    def get_fix_mi(self):
        return self._fix_mi
    def get_var_om(self):
        return self._var_om
    def get_var_f(self):
        return self._var_f
    def get_var_co2(self):
        return self._var_co2
    def get_var_mi(self):
        return self._var_mi
    def get_lt(self):
        return self._lt
    
    def get_var_tot(self):
        var = {y: self._var_om[y]+ self._var_f[y] + self._var_co2[y] + self._var_mi[y] for y in years_world}
        return var
    
    def get_cost_profile_tot(self,y):
        U = np.arange(1, 8761, 1)
        if self._is_cap:
            return self._fix_cap[y] + self._fix_om[y]+ self._fix_mi[y] + (self._var_om[y]+ self._var_f[y] + self._var_co2[y] + self._var_mi[y]) * U
        else:
            return self._fix_dep[y] + self._fix_om[y]+ self._fix_mi[y] + (self._var_om[y]+ self._var_f[y] + self._var_co2[y] + self._var_mi[y]) * U

    def get_cost_profile_fix(self) :
        if self._is_cap:
            fix = {y: self.get_fix_cap()[y] + self.get_fix_mi()[y] + self.get_fix_om()[y] for y in years_world}
        else:
            fix = {y: self.get_fix_dep()[y] + self.get_fix_mi()[y] + self.get_fix_om()[y] for y in years_world}
        return fix
    

    # Set methods
    def set_r(self, r, yd_l=None):
        if r is None:
            self._r ={ y :0 for y in years_world}
        elif isinstance(r, list):
            if len(r) == 1:
                self._r ={ y : r[0] for y in years_world}
            else:
                self._r = create_val_dictionary(r, yd_l)
        else:
            self._r ={ y : r for y in years_world}

    def set_lt(self, lt):
        self._lt = lt

#    def set_fix_cap(self, fix_cap, yd_l=None):
#        if fix_cap is None:
#            self._is_cap = False
#            self._fix_cap ={ y :0 for y in years}
#        elif isinstance(fix_cap, list):
#            self._is_cap = True
#            if len(fix_cap) == 1:
#                self._fix_cap ={ y : fix_cap[0] for y in years}
#            elif len(fix_cap) > 1:
#                self._fix_cap = create_val_dictionary(fix_cap, yd_l)
#            else:
#                print("error : fix_cap=[] is not good")
#        else:
#            self._is_cap = True
#            self._fix_cap ={ y : fix_cap for y in years}

    def set_fix_dep(self, fix_dep, yd_l=None):
        if fix_dep is None:
            self._is_dep = False
            self._fix_dep = { y :0 for y in years_world}
        elif isinstance(fix_dep, list):
            self._is_dep = True
            if len(fix_dep) == 1:
                self._fix_dep ={ y : fix_dep[0] for y in years_world}
            elif len(fix_dep) > 1:
                self._fix_dep = create_val_dictionary(fix_dep, yd_l)
            else:
                print("error : fix_dep=[] is not good")
        else:
            self._is_dep = True
            self._fix_dep ={ y : fix_dep for y in years_world}
            
    def set_fix_ref(self, fix_ref, yd_l=None):
        if fix_ref is None:
            self._fix_ref = { y :0 for y in years_world}
        elif isinstance(fix_ref, list):
            if len(fix_ref) == 1:
                self._fix_ref ={ y : fix_ref[0] for y in years_world}
            elif len(fix_ref) > 1:
                self._fix_ref = create_val_dictionary(fix_ref, yd_l)
            else:
                print("error : fix_ref=[] is not good")
        else:
            self._fix_ref ={ y : fix_ref for y in years_world}

    def set_fix_om(self, fix_om,yd_l=None):
        if fix_om is None:
            self._fix_om ={ y :0 for y in years_world}
        elif isinstance(fix_om, list):
            if len(fix_om) == 1:
                self._fix_om ={ y : fix_om[0] for y in years_world}
            elif len(fix_om) > 1:
                self._fix_om = create_val_dictionary(fix_om, yd_l)
            else:
                print("error : fix_om=[] is not good")
        else:
            self._fix_om ={ y :fix_om for y in years_world}
            
    def set_fix_mi(self, fix_mi,yd_l=None):
        if fix_mi is None:
            self._fix_mi ={ y :0 for y in years_world}
        elif isinstance(fix_mi, list):
            if len(fix_mi) == 1:
                self._fix_mi ={ y :fix_mi[0] for y in years_world}
            elif len(fix_mi) > 1:
                self._fix_mi = create_val_dictionary(fix_mi, yd_l)
            else:
                print("error : fix_mi=[] is not good")
        else:
            self._fix_mi ={ y :fix_mi for y in years_world}
            
    def set_var_om(self, var_om,yd_l=None):
        if var_om is None:
            self._var_om ={ y :0 for y in years_world}
        elif isinstance(var_om, list):
            if len(var_om) == 1:
                self._var_om ={ y :var_om[0] for y in years_world}
            elif len(var_om) > 1:
                self._var_om = create_val_dictionary(var_om, yd_l)
            else:
                print("error : var_om=[] is not good")
        else:
            self._var_om ={ y :var_om for y in years_world}
            
    def set_var_f(self, var_f,yd_l=None):
        if var_f is None:
            self._var_f ={ y :0 for y in years_world}
        elif isinstance(var_f, list):
            if len(var_f) == 1:
                self._var_f ={ y :var_f[0] for y in years_world}
            elif len(var_f) > 1:
                self._var_f = create_val_dictionary(var_f, yd_l)
            else:
                print("error : var_f=[] is not good")
        else:
            self._var_f ={ y :var_f for y in years_world}
            
    def set_var_co2(self, var_co2,yd_l=None):
        if var_co2 is None:
            self._var_co2 ={ y :0 for y in years_world}
        elif isinstance(var_co2, list):
            if len(var_co2) == 1:
                self._var_co2 ={ y :var_co2[0] for y in years_world}
            elif len(var_co2) > 1:
                self._var_co2 = create_val_dictionary(var_co2, yd_l)
            else:
                print("error : var_co2=[] is not good")
        else:
            self._var_co2 ={ y :var_co2 for y in years_world}
            
    def set_var_mi(self, var_mi,yd_l=None):
        if var_mi is None:
            self._var_mi ={ y :0 for y in years_world}
        elif isinstance(var_mi, list):
            if len(var_mi) == 1:
                self._var_mi ={ y :var_mi[0] for y in years_world}
            elif len(var_mi) > 1:
                self._var_mi = create_val_dictionary(var_mi, yd_l)
            else:
                print("error : var_mi=[] is not good")
        else:
            self._var_mi ={ y :var_mi for y in years_world}        
# --------------------- PRINT methods ---------------------------------------------------------------------------------

#     def Print(self):
#         print()
#         print('--------------------------------------------')
#         print('--- Eco parameters -------------------------')
#         print('--------------------------------------------')
#         print(f"discount rate : {self._r}")
#         print('--------------------------------------------')
#         print(f"construction time : {self._ct} y")
#         print(f"depreciation time : {self._dt} y ")
#         print('--------------------------------------------')
#         print(f"Overnight Construction Cost :  {self._occ} M€/MW")
#         print(f" -> Interest During Construction : {self._idc} M€/MW")
#         print(f" -> Total Investment Costs :       {self._tic} M€/MW")
#         print(f" -> Annual CAPEX :                 {self._fix_cap} M€/MW/y")
#         print('--------------------------------------------')
#         print(f"fix_om:  {self._fix_om} M€/MW/y")
#         print(f"var_om:  {self._var_om} M€/MWh")
#         print(f"var_f:   {self._var_f} M€/MWhi")
#         print(f"var_co2: {self._var_co2} M€/MWh")
#         print('--------------------------------------------')
#         print()
#     

















