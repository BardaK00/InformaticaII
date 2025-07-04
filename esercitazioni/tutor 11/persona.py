from ll import Linkedlist,Iteratore
class Persona:
    def __init__(self,cf,via,citta):
        self.cf = cf
        self.via = via
        self.citta = citta

    def getCf(self):
        return self.cf
    def getVia(self):
        return self.via
    def getCitta(self):
        return self.citta
    
    def __eq__(self,other):
        return self.cf == other.cf