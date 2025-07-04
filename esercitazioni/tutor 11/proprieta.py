from ll import Linkedlist,Iteratore
class Proprietà:
    def __init__(self,cf,codice,possesso):
        self.cf = cf
        self.codice = codice
        self.possesso = possesso

    def __eq__(self,other):
        return self.cf == other.cf and self.codice == other.codice
    
    def getCF(self):
        return self.cf
    def getCodice(self):
        return self.codice
    def getPossesso(self):
        return self.possesso
    