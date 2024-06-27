class prm_storage:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self):

        self._mode  = None      # mode[y,h] is either 'turbine' or 'compress'
        self._EC    = None      # Energy compressed EC[y,h]
        self._level = None      # level of the storage get_level()[y,h] [MWh]
        self._levelstart = None # level of the storage get_level()[y,h] [MWh]
        self._levelmax = None   # level max [MWh]
        self._levelmin = None   # level min [MWh]
        self._efficiency_discharge = None
        self._efficiency_charge = None
        self.loss=None #pourcetage de perte à l'année

       # Add dynamics variables ...

# --------------------- End Of Constructor ----------------------------------------------------------------------------

# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_mode(self):
        return self._mode
    def get_EC(self):
        return self._EC
    def get_level(self):
        return self._level
    def get_level_max(self):
        return self._levelmax
    def get_level_min(self):
        return self._levelmin
    def get_level_start(self):
        return self._levelstart
    def get_efficiency_charge(self):
        return self._efficiency_charge
    def get_efficiency_discharge(self):
        return self._efficiency_discharge

    # Set methods
    def set_mode(self, mode):
        self._mode = mode
    def set_EC(self, EC):
        self._EC = EC
    def set_level(self, lev):
        self._level = lev
    def set_level_max(self, levmax):
        self._levelmax = levmax
    def set_level_min(self, levmin):
        self._levelmin = levmin
    def set_level_start(self, levstart):
        self._levelstart = levstart
    def set_efficiency_charge(self, eff):
        self._efficiency_charge = eff
    def set_efficiency_discharge(self, eff):
        self._efficiency_discharge = eff
        