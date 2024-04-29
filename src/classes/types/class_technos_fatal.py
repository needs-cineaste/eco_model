class Techno_Fatal(Techno):
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, tname, ttype, tech_params, eco_params, prm_fatal):
        super().__init__('fatal', tname, ttype, prm_eco, prm_tech)
        
        self._prm_spec = prm_fatal
# --------------------- End Of Constructor ----------------------------------------------------------------------------
        


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_spec(self):
        return self._prm_fatal


    # Set methods
    def set_spec(self, prm_fatal):
        self._prm_fatal = prm_fatal


# --------------------- PRINT methods ---------------------------------------------------------------------------------

