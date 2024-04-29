class prm_dispatchable:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self):

        self._rup  = 1    # Ramping up dynamic [0,1]
                          # 0 means not flexible up
                          # 1 means 100%Pn/h
        self._rdo  = 1    # Ramping down dynamic [0,1]
                          # 0 means not flexible down
                          # 1 means 100%Pn/h
                
# --------------------- End Of Constructor ----------------------------------------------------------------------------


# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # get methods
    def get_rup(self):
        return self._rup
    def get_rdo(self):
        return self._rdo


    # set methods
    def set_rup(self, rup):
        self._rup = rup
    def set_rdo(self, rdo):
        self._rdo = rdo
