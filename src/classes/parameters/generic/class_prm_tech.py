class prm_tech:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self, years, hours):
   
        self._isPvar  = {y: True for y in years}  # Tell if Power is endogeneous (variable) or exogeneous
        self._isEvar  = {(y,h): True for y in years for h in hours}  # Tell if Energy is endogeneous (variable) or exogeneous
   
        self._P  = None   # Capacity installed P[y] [MW]  
        self._E  = None   # Energy produced E[y,h]
        self._LF = None   # Load Factor LF[y,h]
        self._C  = None   # Curtailment C[y,h]
        self._A  = None   # Availabilité of dispatchable techno A[y,h] between 0 and 1
                            # 0 means all units are off
                            # 1 means all units are full operationnal
        

# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_isPvar(self):
        return self._isPvar
    def get_isEvar(self):
        return self._isEvar
    
    def get_P(self):
        return self._P
    def get_E(self):
        return self._E
    def get_LF(self):
        return self._LF
    def get_C(self):
        return self._C
    def get_A(self):
        return self._A

    
    # Set methods
    def set_isPvar(self, isPvar):
        self._isPvar = isPvar
    def set_isEvar(self, isEvar):
        self._isEvar = isEvar

    def set_P(self, P):
        self._P = P
    def set_E(self, E):
        self._E = E
    def set_LF(self, LF):
        self._LF = LF
    def set_C(self, C):
        self._C = C
    def set_A(self, avail):
        self._A = avail

            
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
