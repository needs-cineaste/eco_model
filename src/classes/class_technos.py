class Techno:
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, tname, ttype, prm_eco, prm_tech):
        self._name     = tname    # name of techno ('nuclear', 'gas', 'vre', etc.)
        self._type     = ttype    # type of technos ('new', 'hist' for 'nuclear, 'pv', 'wof' for 'vre', etc.)
        self._prm_eco  = prm_eco
        self._prm_tech = prm_tech
# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_name(self):
        return self._name
    def get_type(self):
        return self._type
    def get_prm_eco(self):
        return self._prm_eco
    def get_prm_tech(self):
        return self._prm_tech

    # Set methods
    def set_name(self, tname):
        self._name = tname
    def set_id(self, tname):
        self._id = tname
    def set_type(self, ttype):
        self._type = ttype
    def set_prm_eco(self, prm_eco):
        self._prm_eco = prm_eco
    def set_prm_tech(self, prm_tech):
        self._prm_tech = prm_tech

# --------------------- PRINT methods ---------------------------------------------------------------------------------
    def Print(self):
        print()
        print('#####################################################################')
        print('######### Techno ####################################################')
        print('#####################################################################\n')
        print(f"id   : {self._id}")
        print(f"name : {self._name}")
        print(f"type : {self._type}")
        self._prm_eco.Print()
        self._prm_tech.Print()
        print('#####################################################################')
        print('#####################################################################')
        print()
    