from ll import Linkedlist,Iteratore
from persona import Persona
from immobile import Immobile
from proprieta import Proprietà

class Sistema:
    def __init__(self,listaPersone :Linkedlist, listaImmobili : Linkedlist,listaProprieta:Linkedlist):
        self.listaPersona = listaPersone
        self.listaImmobili = listaImmobili
        self.listaProprieta = listaProprieta

    def contribuenti(self,c):
        ll = Linkedlist()
        for immobile in self.listaImmobili:
            cittaImm = immobile.getCitta()
            if cittaImm == c:
                listaProp = immobile.getListaProprietari()
                for p in listaProp:
                    ll._aggiungiCoda(p)
        return ll
    
    def _getImmobiliPiùProp(self):
        l = []
        for immobile in self.listaImmobili:
            listaProp = immobile.getListaProprietari()
            if len(listaProp) > 1: #fattibile perchè abbiamo il metodo __len__ nella nostra linkedList
                l.append(immobile)
        return l
    
    def piuProprietari(self):
        ll = Linkedlist()
        immobiliDaVerificare = self._getImmobiliPiùProp()
        for immobile in immobiliDaVerificare:
            proprietari = immobile.getListaProprietari()
            count = 0
            for p in proprietari:
                if p.getCitta() == immobile.getCitta():
                    count += 1
            if count == 1:
                ll._aggiungiCoda(immobile)
        return ll
                

    def grandiProprietà(self,c,d):
        ll = Linkedlist()
        lista = []
        l = []
        listaVie = []   
        for persona in self.listaPersona:
            if persona.getCitta() == c:
                l.append(persona.getCf()) ####considera i cf di colore che abitano in c
                listaVie.append(persona.getVia())
        for cf in l:
            for proprietà in self.listaProprieta:
                if cf == proprietà.getCf():### se la proprietà ha il cf inserito il lista allora trova l'immobile 
                    codImmobile = proprietà.getCodice()
                    for immobile in self.listaImmobili:
                        if codImmobile == immobile.getCodiceCatastale() and immobile.getDimensione() > d:#se l'immobile è più grande di d lo aggiunge in lsta
                            lista.append(cf)
                            for persona in self.listaPersona:
                                if persona.getCf()==cf:
                                    listaVie.append(persona.getVia())
        lista = set(lista)
        listaVie = list(set(listaVie))
        listaVie.sort()
        return self._sortByVie(lista,listaVie)
    
    def _sortByVie(self,listaCF,listaVie):
        ll = Linkedlist()
        for via in listaVie:
            for cf in listaCF:
                for persona in self.listaPersona:
                    if persona.getVia()==via and cf == persona.getCf():
                        ll._aggiungiCoda(cf)
        return ll 
                

        
    def _calcolaPatrimonio(self,cf):
        patr = 0
        for proprietà in self.listaProprieta:
            if proprietà.getCf() == cf:
                codImmobile = proprietà.getCodice()
                for immobile in self.listaImmobili:
                    if immobile.getCodiceCatastale() == codImmobile:
                        valore = immobile.getValore()
                        patr += (proprietà.getPossesso()) * valore 
        return patr
    
    def patrimoni(self,c):
        d ={}
        for persona in self.listaPersona:
            if persona.getCitta() == c:
                cf = persona.getCf()
                d[cf]=self._calcolaPatrimonio(cf)
        return d



    
   