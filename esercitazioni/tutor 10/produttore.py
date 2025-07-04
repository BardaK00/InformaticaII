from ll import Linkedlist,Iteratore
class Produttore:
    def __init__(self,codice,nome,nazione):
        self.codice = codice
        self.nome = nome
        self.nazione = nazione

    def getCodice(self):
        return self.codice
    def getNome(self):
        return self.nome
    def getNazione(self):
        return self.nazione
        