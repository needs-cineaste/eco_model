class Techno_Storage(Techno):
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, tname, ttype, tech_params, eco_params, prm_storage):
        super().__init__('storage', tname, ttype, prm_eco, prm_storage)
        
        self._prm_spec = prm_storage
# --------------------- End Of Constructor ----------------------------------------------------------------------------
        


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_spec(self):
        return self._prm_spec


    # Set methods
    def set_spec(self, prm_storage):
        self._prm_spec = prm_storage


# --------------------- PRINT methods ---------------------------------------------------------------------------------

