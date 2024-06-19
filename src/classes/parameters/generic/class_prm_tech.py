class prm_tech:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self):

        self._isPvar  = {y: True for y in years}  # Tell if Power is endogeneous (variable) or exogeneous
        self._isEvar  = {(y,w,h): True for y in years for w in weeks for h in hours}  # Tell if Energy is endogeneous (variable) or exogeneous
   
        self._P   = None   # Capacity installed P[y] [MW]  
        self._Inv = None   # Investment in capacity Inv[y] [MW]  
        self._InvMax = None   # Maximum capacity deployment per year [y] [MW/y]  
        self._Dec = None   # Decommissioning in capacity Dec[y] [MW]  
        self._E   = None   # Energy produced E[y,h]
        self._LF  = None   # Load Factor LF[y,h]
        
        self._C02 = None   # CO2 emission factor [g/kWh]

        self._C   = None   # Curtailment C[y,h]
        self._A   = None   # Availabilité of dispatchable techno A[y,h] between 0 and 1
                            # 0 means all units are off
                            # 1 means all units are full operationnal
        self._hist_capa = None # Historical capacity data
        self._hist_inv  = None # Historical investment data
        self._hist_dec  = None # Historical decommisionning data

# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_isPvar(self):
        return self._isPvar
    def get_isEvar(self):
        return self._isEvar
    def get_P(self):
        return self._P
    def get_Inv(self):
        return self._Inv
    def get_InvMax(self):
        return self._InvMax
    def get_Dec(self):
        return self._Dec
    def get_E(self):
        return self._E
    def get_LF(self):
        return self._LF
    def get_CO2(self):
        return self._CO2
    def get_C(self):
        return self._C
    def get_A(self):
        return self._A
    
    # Historical data
    def get_historic_data(self, data_type):
        if data_type not in ['CAPA', 'INV', 'DEC']:
            raise ValueError("Invalid data type. Must be one of: 'DEC', 'CAPA', 'INV'")
        if data_type == 'CAPA':
            return self.get_hist_capa()
        elif data_type == 'INV':
            return self.get_hist_inv()
        elif data_type == 'DEC':
            return self.get_hist_dec()
    
    def get_hist_inv(self):
        return self._hist_inv
    def get_hist_capa(self):
        return self._hist_capa
    def get_hist_dec(self):
        return self._hist_dec 

    
    # Set methods
    def set_isPvar(self, isPvar):
        self._isPvar = isPvar
    def set_isEvar(self, isEvar):
        self._isEvar = isEvar

    def set_P(self, P):
        self._P = P
    def set_Inv(self, Inv):
        self._Inv = Inv
    def set_InvMax(self, InvMax):
        self._InvMax = InvMax
    def set_Dec(self, Dec):
        self._Dec = Dec
    def set_E(self, E):
        self._E = E
    def set_LF(self, LF):
        self._LF = LF
    def set_CO2(self, CO2):
        self._CO2 = CO2
    def set_C(self, C):
        self._C = C
    def set_A(self, avail):
        self._A = avail
        
    def set_historic_data(self, data_type, data):
        if data_type not in ['DEC', 'CAPA', 'INV']:
            raise ValueError("Invalid data type. Must be one of: 'DEC', 'CAPA', 'INV'")
        
        if data_type == 'CAPA':
            self._hist_capa = data
        elif data_type == 'INV':
            self._hist_inv = data
        elif data_type == 'DEC':
            self._hist_dec = data

            
# --------------------- PRINT methods ---------------------------------------------------------------------------------

#    def Print(self):
#        print()
#        print('--------------------------------------------')
#        print('--- Technical parameters -------------------')
#        print('--------------------------------------------')
#
#        print('--------------------------------------------')
#        print(f" -> Installed Capacity : {self._P} MW")
#        print('--------------------------------------------')
#        print(f" -> Energy Production [MWh] :")
#        print(np.array(self._E))
#        print('--------------------------------------------')
#        print()
