# Class to emulate row in NIMA
class nima_row:
    def __init__(self, identifier, fVal, sVal, iVal):
        self.identifier = identifier
        self.float_val = fVal
        self.string_val = sVal
        self.int_val = iVal
    
    def __str__(self):
        return "Row {0} F: {1} I: {2} S: {3}".format(str(self.identifier), 
                                                     str(self.float_val), 
                                                     self.string_val, 
                                                     str(self.int_val))