class prm_eco:
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, years):        
        self._r        = None  # Discount rate
        self._fix_cap  = None  # Annual CAPEX [€/MW/y]
        self._fix_om   = None  # Fix OM cost [€/MW/y]
        self._fix_mi   = None  # Misc Fix cost [€/MW/y] => Sum of other fixed costs
        self._var_om   = None  # var OM cost [€/MWh ouput]
        self._var_f    = None  # var fuel cost [€/MWh input]
        self._var_co2  = None  # var carbon cost [€/MWh i]
        self._var_mi   = None  # Misc var [€/MWh i] => Sum of other variable costs
        
# --------------------- End Of Constructor ---------------------------------------------------------------------------    

    def calculate_capex(self, occ, ct, dt, r):
        tic = occ / ct * ( (1 + r) / r ) * ( (1 + r)**ct - 1)
        capex = tic * ( ( r * ( 1 + r )**dt ) / ( (1 + r)**dt - 1) ) 
        self._fix_cap = capex

# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_r(self):
        return self._r
    def get_fix_cap(self):
        return self._fix_cap
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
    
    def get_fix_tot(self):
        return self._fix_cap + self._fix_om + self._fix_mi
    def get_var_tot(self):
        return self._var_om + self._var_f + self._var_co2 + self._var_mi
    
    def get_cost_profile(self):
        U = np.arange(1, 8761, 1)
        return self._fix_cap + self._fix_om + self._fix_mi + (self._var_om + self._var_f + self._var_co2 + self._var_mi) * U
    
    # Set methods
    def set_r(self, r):
        self._r = r
    def set_fix_cap(self, fix_cap):
        self._fix_cap = fix_cap
    def set_fix_om(self, fix_om):
        self._fix_om = fix_om
    def set_fix_mi(self, fix_mi):
        self._fix_mi = fix_mi
    def set_var_om(self, var_om):
        self._var_om = var_om
    def set_var_f(self, var_f):
        self._var_f = var_f
    def set_var_co2(self, var_co2):
        self._var_co2 = var_co2
    def set_var_mi(self, var_mi):
        self._var_mi = var_mi
        
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
# 