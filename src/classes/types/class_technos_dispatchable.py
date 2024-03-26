class Techno_Dispatchable(Techno):
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, tname, ttype, tech_params, eco_params, prm_dispatchable):
        super().__init__('dispatchable', tname, ttype, prm_eco, prm_dispatchable)
        
        self._prm_spec = prm_dispatchable
# --------------------- End Of Constructor ----------------------------------------------------------------------------
        


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_spec(self):
        return self._prm_spec


    # Set methods
    def set_spec(self, prm_dispatchable):
        self._prm_spec = prm_dispatchable


# --------------------- PRINT methods ---------------------------------------------------------------------------------

