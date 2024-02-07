class prm_tech:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self, years, hours):
   
        self._isFatal = False # Tell if Power is Fatal => E(t) = P * LF(t) with LF(t) exogeneous
        self._isPvar  = {y: True for y in years}  # Tell if Power is endogeneous (variable) or exogeneous
        self._isEvar  = {(y,h): True for y in years for h in hours}  # Tell if Energy is endogeneous (variable) or exogeneous
   
        self._P  = None   # Capacity installed [MW]  
        self._E  = None   # Energy produced for each 8760 time steps in a year
        self._LF = None   # Load Factor for each 8760 time steps in a year
        self._C  = None   # Curtailment for each 8760 time steps in a year
        self._avail = None # Availabilité of techno for each 8760 time steps in a year
                                 # 0 means all units are off
                                 # 1 means all units are full operationnal
        
        self._Emax = 1e20 # Maximum of energy/power on 1 hour
        self._Emin = 0    # Minimum of energy/power on 1 hour
        self._rup  = 1    # Ramping up dynamic [0,1]
                          # 0 means not flexible up
                          # 1 means 100%Pn/h
        self._rdo  = 1    # Ramping down dynamic [0,1]
                          # 0 means not flexible down
                          # 1 means 100%Pn/h

# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_P(self):
        return self._P
    def get_E(self):
        return self._E
    def get_LF(self):
        return self._LF
    def get_C(self):
        return self._C
    def get_isFatal(self):
        return self._isFatal
    def get_isPvar(self):
        return self._isPvar
    def get_isEvar(self):
        return self._isEvar
    def get_avail(self):
        return self._avail
    def get_Emax(self):
        return self._Emax
    def get_Emin(self):
        return self._Emin
    def get_rup(self):
        return self._rup
    def get_rdo(self):
        return self._rdo
    
    # Set methods
    def set_P(self, P):
        self._P = P
    def set_E(self, E):
        self._E = E
    def set_LF(self, LF):
        self._LF = LF
    def set_C(self, C):
        self._C = C
    def set_isFatal(self, isFatal):
        self._isFatal = isFatal
    def set_isPvar(self, isPvar):
        self._isPvar = isPvar
    def set_isEvar(self, isEvar):
        self._isEvar = isEvar
    def set_avail(self, avail):
        self._avail = avail
    def set_Emax(self, Emax):
        self._Emax = Emax
    def set_Emin(self, Emin):
        self._Emin = Emin
    def set_rup(self, rup):
        self._rup = rup
    def set_rdo(self, rdo):
        self._rdo = rdo

# --------------------- PRINT methods ---------------------------------------------------------------------------------

    def Print(self):
        print()
        print('--------------------------------------------')
        print('--- Technical parameters -------------------')
        print('--------------------------------------------')
        if self._isPvar:
            print('P is endogeneous variable')
        else:
            print('P is exogeneous variable')
        if self._isEvar:
            print('E is endogeneous variable')
        else:
            print('E is exogeneous variable')
        print('--------------------------------------------')
        print(f" -> Installed Capacity : {self._P} MW")
        print('--------------------------------------------')
        print(f" -> Energy Production [MWh] :")
        print(np.array(self._E))
        print('--------------------------------------------')
        print()
