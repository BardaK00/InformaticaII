from ll import Linkedlist

class Calciatore:
    def __init__(self, nome : str, squadraAttuale : str):
        self.nome = nome
        self.squadraAttuale = squadraAttuale
    def __eq__(self, other):
        return self.nome == other.nome
    def __repr__(self):
        return f"Calciatore({self.nome})"

    def getNome(self):
        return self.nome

    def getSquadraAttuale(self):
        return self.squadraAttuale


class Contratto:
    def __init__(self, squadra : str, calciatore : str, prezzo : int, premi : Linkedlist):
        self.squadra = squadra
        self.calciatore = calciatore
        self.prezzo = prezzo
        self.premi = premi
    def __repr__(self):
        return f"Contratto({self.squadra})"
    def __eq__(self, other):
        return self.squadra == other.squadra and self.calciatore == other.calciatore
    def getSquadra(self):
        return self.squadra
    def getCalciatore(self):
        return self.calciatore
    def getPrezzo(self):
        return self.prezzo
    def getPremi(self):
        return self.premi


class Sistema:
    def __init__(self, listaContratti : Linkedlist[Contratto], listaCalciatori : Linkedlist[Calciatore]):
        self.listaContratti = listaContratti
        self.listaCalciatori = listaCalciatori
    ############ ESERCIZIO 1 #############
    def verificaDati(self):
        for contratti in self.listaContratti:
            giocatore = contratti.getCalciatore()
            for calciatori in self.listaCalciatori:
                if giocatore == calciatori.getNome() and calciatori.getSquadra() == contratti.getSquadra():
                    return False
        return True
    
    ########### ESERCIZIO 2 #################
    def _contaAcquisti(self,nomeSquadra : str):
        squad_vend = set()
        for contratti in self.listaContratti:
            if contratti.getSquadra() == nomeSquadra:
                calciatore = contratti.getCalciatore()
                for calc in self.listaCalciatori:
                    if calc.getNome() == calciatore:
                        squadAtt = calc.getSquadraAttuale()
                if contratti.getSquadra() != squadAtt:       
                    squad_vend.add(squadAtt)
        return len(squad_vend)
    
    def _contaPrezzo(self,nomeSquadra):
        prezzo = 0
        for contratto in self.listaContratti:
            if contratto.getSquadra() == nomeSquadra:
                prezzo += contratto.getPrezzo()
        return prezzo
    
    def _getSquadre(self):
        squadre = []
        for contratti in self.listaContratti:
            squadre.append(contratti.getSquadra())
        return list(set(squadre))


    def squadreAttive(self,pMin):
        l = Linkedlist()
        squadre = self._getSquadre()
        
        for s in squadre:
            if self._contaAcquisti(s) >= 3 and self._contaPrezzo(s) >= pMin: 
                l._aggiungiTesta(s)
        return l

    ########### ESERCIZIO 3 #############    
    def sommaPremiCalc(self,nomeCalc):
        somma = 0
        for contratto in self.listaContratti:
            if contratto.getCalciatore() == nomeCalc:
                premi = contratto.getPremi()
                for p in premi:
                    somma += p._value
        return somma

    def calciatoriPocoPremiati(self,pMin):
        l = Linkedlist()
        for calc in self.listaCalciatori:
            somma = self.sommaPremiCalc(calc.getNome())
            if somma <= pMin:
                l._aggiungiTesta(calc)

        return l
    
    ############### ESERCIZIO RICORSIVO ALBERO ################
    
    #def verificaCammino(self,x):
    #    if self._card==0:
    #        return None
    #    return self._verificaCamminoDa(self._root,x,0,0)
    #
    #def _verificaCamminoDa(self,node,x,cont,somma):
    #    
    #    if node is None:
    #        return False
    #   somma = somma + node.value
    #    cont +=1
    #    if node.Lson is None and node.Rson is None:
    #        return somma/(cont)>x
    #    return self._verificaCamminoDa(node.Rson,x,cont,somma) or self._verificaCamminoDa(node.Lson,x,cont,somma)
    