class prm_dispatchable:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self):

        self._LFmax  = None   # Maximal Load Factor LF[y,h]
        self._LFmin  = None   # Minimal Load Factor LF[y,h]
        
        self._rup  = 1    # Ramping up dynamic [0,1]
                          # 0 means not flexible up
                          # 1 means 100%Pn/h
        self._rdo  = 1    # Ramping down dynamic [0,1]
                          # 0 means not flexible down
                          # 1 means 100%Pn/h
                
# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # get methods
    def get_LFmax(self):
        return self._LFmax
    def get_LFmin(self):
        return self._LFmin
    
    def get_rup(self):
        return self._rup
    def get_rdo(self):
        return self._rdo


    # set methods
    def set_LFmax(self, LFmax):
        self._LFmax = LFmax
    def set_LFmin(self, LFmin):
        self._LFmin = LFmin
    
    def set_rup(self, rup):
        self._rup = rup
    def set_rdo(self, rdo):
        self._rdo = rdo
