from ll import Linkedlist,Iteratore
class Conducente:
    def __init__(self,nome,viaggi:Linkedlist):
        self.nome = nome
        self.viaggi = viaggi
    def getNome(self):
        return self.nome
    def getViaggi(self):
        return self.viaggi
    def __eq__(self, other):
        if not other.isIstance(Conducente):
            return False
        return self.nome == other.nome and self.viaggi == other.viaggi
        