class Viaggio:
    def __init__(self,codice,destinazione,durata,num_passeggeri):
        self.codice = codice
        self.destinazione = destinazione
        self.durata = durata
        self.num_passeggeri = num_passeggeri

    def getCodice(self):
        return self.codice
    def getDestinazione(self):
        return self.destinazione
    def getDurata(self):
        return self.durata
    def getNumPasseggeri(self):
        return self.num_passeggeri
    def __eq__(self,other):
        if not other.isinstance(Viaggio):
            return False
        return self.codice == other.codice and self.destinazione== other.destinazione and self.durata == other.durata and self.num_passeggeri == other.num_passeggeri