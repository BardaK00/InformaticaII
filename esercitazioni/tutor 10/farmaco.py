
from ll import Linkedlist,Iteratore
class Farmaco:
    def __init__(self,codice,nome,Codproduttore,prezzo,princAttivi:Linkedlist):
        self.codice = codice
        self.nome = nome
        self.codProduttore = Codproduttore
        self.prezzo = prezzo
        self.princAttivi = princAttivi

    def getCodice(self):
        return self.codice
    
    def getNome(self):
        return self.nome
    
    def getCodProduttore(self):
        return self.codProduttore
    
    def getPrezzo(self):
        return self.prezzo
    
    def getPrincAttivi(self):
        return self.princAttivi