class Techno:
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, ttype, tname, ttitle, prm_eco, prm_tech, prm_spec):
        self._type     = ttype     # family of the techno ('dispatch', 'fatal', 'storage')
        self._name     = tname    # name of techno ('nuclear', 'gas', 'vre', etc.)
        self._title    = ttitle    # type of technos ('new', 'hist' for 'nuclear, 'pv', 'wof' for 'vre', etc.)
        self._prm_eco  = prm_eco
        self._prm_tech = prm_tech
        self._prm_spec = prm_spec
# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_type(self):
        return self._type
    def get_name(self):
        return self._name
    def get_title(self):
        return self._title
    def get_eco(self):
        return self._prm_eco
    def get_tech(self):
        return self._prm_tech
    def get_spec(self):
        return self._prm_spec

    # Set methods
    def set_type(self, ttype):
        self._type = ttype
    def set_name(self, tname):
        self._name = tname
    def set_title(self, ttitle):
        self._title = ttitle

    def set_eco(self, prm_eco):
        self._prm_eco = prm_eco
    def set_tech(self, prm_tech):
        self._prm_tech = prm_tech
    def set_spec(self, prm_spec):
        self._prm_spec = prm_spec

# --------------------- PRINT methods ---------------------------------------------------------------------------------
    def Print(self):
        print()
        print('#####################################################################')
        print('######### Techno ####################################################')
        print('#####################################################################\n')
        print(f"name : {self._name}")
        print(f"type : {self._type}")
        #self._prm_eco.Print()
        #self._prm_tech.Print()
        print('#####################################################################')
        print('#####################################################################')
        print()
    