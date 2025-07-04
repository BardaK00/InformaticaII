from Tools.listaconcatenata import ListaConcatenata


class Piatto:
    def __init__(self, codice : str, nome : str, ingredienti : ListaConcatenata, dosi : ListaConcatenata):
        self.codice = codice
        self.nome = nome
        self.ingredienti = ingredienti
        self.dosi = dosi

    def __eq__(self, other):
        return self.codice == other.codice
    def __repr__(self):
        return f'{self.codice} {self.nome} {self.ingredienti} {self.dosi}'

    def getCodice(self):
        return self.codice
    def getNome(self):
        return self.nome
    def getIngredienti(self):
        return self.ingredienti
    def getDosi(self):
        return self.dosi
    
   
