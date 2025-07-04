from ll import Linkedlist,Iteratore
from farmaco import Farmaco
from produttore import Produttore

class Gestione:
    def __init__(self,listaFarmaci : Linkedlist,listaProduttori:Linkedlist,listaPrincAttivi:Linkedlist):
        self.listaFarmaci = listaFarmaci
        self.listaProduttori = listaProduttori
        self.listaPrincAttivi = listaPrincAttivi

    def farmacoCaro(self,p):
        d = {}
        for farmaco in self.listaFarmaci:
            principi = farmaco.getPrincAttivi()
            if p in principi:
                if not farmaco in d:
                    d[farmaco] = 0
                d[farmaco] = farmaco.getPrezzo()
        max = max(d.values())
        items = d.items()
        for it in items:
            if it[1] == max:
                return it[0]
            
    def _verificaFarmacoEquivalente(self,f1:Farmaco,f2:Farmaco):
        principiF1=f1.getPrincAttivi()
        principiF2=f2.getPrincAttivi()
        if principiF1 == principiF2: #anche se sono linked list è possibile perchè la classe contiene il medoto __eq__
            return True
        return False
        
    def esclusivisti(self):
        ll = Linkedlist()
        for prod in self.listaProduttori:
            listafar = []
            cod = prod.getCodice()
            for farmaco in self.listaFarmaci:
                if farmaco.getProduttore() == cod:
                    listafar.append(farmaco)
            
            esclusivo=True
            for i in range(0,len(listafar)):
                for j in range(i+1,len(listafar)):
                    if self._verificaFarmacoEquivalente(listafar[i],listafar[j]) == True:
                        esclusivo= False
                        break
            if esclusivo:
                ll._aggiungiCoda(prod)
        return ll

    def _creadiz(self):
        d =  {}
        for prod in self.listaProduttori:
            nazione = prod.getNazione()
            if not nazione in d:
                d[nazione]=Linkedlist()
            for farmaco in self.listaFarmaci:
                codProd = farmaco.getProduttore()
                if prod.getCodice()== codProd:
                    listaPrinc = farmaco.getPrincAttivi()
                    for princ in listaPrinc:
                         d[nazione]._aggiungiCoda(princ)
        return d

        #d={nazione1:ll principi 1, nazione 2:ll principi 2}

    def universali(self):
        ll = Linkedlist()
        d = self._creadiz()
        sets = []
        value = d.values()
        items = d.items()
        for v in value:
            it = iter(v)
            while not it.finito():
                sets.append(next(it))
        sets= set(sets)

        commons = []
        for s in sets:
            comune = True
            for it in items:
                if s not in it[1]:
                    comune = False
                    break
            if comune:
                commons.append(s)
        
        for c in commons:
            ll._aggiungiCoda(c)

        return ll
                








            

    