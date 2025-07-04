from ll import Linkedlist,Iteratore
class Immobile:
    def __init__(self,codCadastale,via,citta,dimensione,valore,listaProprietà:Linkedlist):
        self.codCatastale = codCadastale
        self.via = via 
        self.citta = citta
        self.dimensione = dimensione
        self.valore = valore
        self.listaProprietari = listaProprietà

    def getCodCatastale(self):
        return self.codCatastale
    
    def getVia(self):
        return self.via
    def getCitta(self):
        return self.citta
    def getDimensione(self):
        return self.dimensione
    def getValore(self):
        return self.valore
    def getListaProprietari(self):
        return self.listaProprietari
    
    def __eq__ (self,other):
        return self.codCatastale == other.codCastatale
    
    