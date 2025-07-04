class Ingrediente:
    def __init__(self, codice: str, nome: str, costoUnitario: float, adattoVegetariani: bool):
        self.codice = codice
        self.nome = nome
        self.costoUnitario = costoUnitario
        self.adattoVegetariani = adattoVegetariani

    def getCodice(self):
        return self.codice

    def getNome(self):
        return self.nome

    def getCostoUnitario(self):
        return self.costoUnitario

    def getAdattoVegetariani(self):
        return self.adattoVegetariani

    def __eq__(self, other):
        return self.codice == other.codice

    def __repr__(self):
        return f"{self.codice} {self.nome} {self.costoUnitario}"

