from ll import Linkedlist
from componente import Componente
from articolo import Articolo

class Sistema:
    def __init__(self,Linkedlist : listaComponenti,Linkedlist: listaArticoli):
        self.listaArticoli = listaArticoli
        self.listaComponenti = listaComponenti

    def _calcprofitto(self,nomeArt):
        somma = 0
        for art in self.listaArticoli:
            if art.getNome() == nomeArt:
            vendita = art.getPrezzo()
            comps = art,getComponenti()
            for componente in comps:
                somma += componente.getPrezzo()
        return somma - vendita

    def articoloTop(self):
        iter = iter(self.listaArticoli)
        currArt = next(iter)
        art = currArt.getNome
        x = self._calcprofitto(art())
        
        while not iter.finito():
            currArt =next(iter)
            y = self._calcprofitto(currArt.getNome)
            if y >x:
                x = y
                art = currArt.getNome()
        return art

    def _createdict(self):
        d = {}
        for art in self.listaArticoli:
            nome = art.getNome()
            x = art.getComponenti()
            it = iter(x)
            while not it.finito():
                comp = next(it)
                if not comp in d:
                    d[comp]=[]
                d[comp].append(nome)
        return d
    
    def _lenArt(self):
        len = 0
        for art in self.listaArticoli:
            len += 1 
        return len
    
    def componentiUniversali(self):
        ll = Linkedlist()
        lenArt = self._lenArt()
        d = self._createdict()
        items=d.items()
        for it in items:
            if lenArt == len(it[1]):
                ll.aggiungiInCoda(it[0])
        return ll
    
    def ArticoliComponentiCostosi(self,p):
        ll = Linkedlist()
        for art in self.listaArticoli:
            nome = art.getNome()
            x = art.getComponenti()
            for c in x:
                if c.getPrezzo() > p:
                    ll.aggiungiInCoda(nome)
        return ll