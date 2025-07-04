from ll import Linkedlist,Iteratore
from viaggio import Viaggio
from conducente import Conducente
class Sistema:
    def __init__(self,listaViaggi:Linkedlist,listaConducenti:Linkedlist):
        self.listaViaggi = listaViaggi 
        self.listaConducenti = listaConducenti

    def _getOreConducente(self,conducente:Conducente):
        sumOre = 0
        viaggiCond = conducente.getViaggi()
        for viaggio in viaggiCond:
            sumOre += viaggio.Getdurata()
        return sumOre

    def verifica(self,min_ore,max_passeggeri):
        for conducente in self.listaConducenti:
            oreConducente = self._getOreConducente(conducente)
            if oreConducente < min_ore:
                return False
            
        for viaggio in self.listaViaggi:
            passeggeri = viaggio.getNumPasseggeri()
            if passeggeri > max_passeggeri:
                return False
            
        return True
    
    def _calcDestInViaggio(self,d):
        cont = 0
        for viaggio in self.listaViaggi:
            if viaggio.getDestinazione() == d:
                cont +=1
        return cont

    def destinazioni_richieste(self,passeggeri_min):
        ll = Linkedlist()
        for viaggio in self.listaViaggi:
            if viaggio.getNumPasseggeri() > passeggeri_min and self._calcDestInViaggio(viaggio.getDestinazione()) >=2:
                ll._aggiungiCoda(viaggio.getDestinazione())
        return ll
    
    def conducenti_diversi(self,conducente:Conducente):
        ll = Linkedlist()
        
        lb=Linkedlist()
        viaggiCond=conducente.getViaggi()
        
        for b in viaggiCond:
            lb._aggiungiCoda(b.getDestinazione())

        for condu in self.listaConducenti:
            if condu == conducente:
                continue
            la=Linkedlist()
            listaViaggi = condu.getViaggi()
            for a in listaViaggi:
                la._aggiungiCoda(a.getDestinazione())
            
            if self._verificaDest(la,lb):
                ll._aggiungiCoda(condu.getNome())
        return ll
    
    def _verificaDest(self,l1 :Linkedlist,l2:Linkedlist):
        for dest in l1:
            if dest in l2:
                return False
        return True
                    


