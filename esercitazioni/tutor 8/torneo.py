from squadra import Squadra
from partita import Partita
from ll import Linkedlist

class Torneo:
    def __init__(self,listaSquadra,listaPartite):
        self.listaSquadre = listaSquadra
        self.listaPartite = listaPartite

    def _createdict(self):
        d = {}
        for p in self.listaPartite:
            goalfatti=p.getGoalSquadraCasa()
            goalsubiti = p.getGoalSquadraOspite()
            nomeS = p.getNomeSquadraCasa()
            if not nomeS in d:
                d[nomeS]=[]
            d[nomeS].append(goalfatti)
            d[nomeS].append(goalsubiti)
        return d
    
    def _contavitt(self,nomeS):
        contv = 0
        contp = 0
        d = self._createdict()
        items = d.items()
        for it in items:
            for p in range (0,len(it[1]),2):
                if it[0] == nomeS and it[1][p] > it[1][p+1]:
                    contv+=1
                elif it[0] == nomeS and it[1][p] < it[1][p+1]:
                    contp += 1
        return contv - contp

    def squadreCasalinghe(self):
        lista = []
        ll = Linkedlist()
        for p in self.listaPartite:
            nome = p.getNomeSquadraCasa()
            lista.append(nome)
        lista = set(lista)
        lista = list(lista)
        for i in range (0,len(lista)):
            if self._contavitt(lista[i]) > 0:
                ll.aggiungiInCoda(lista[i])
        return ll
    
    def _getCittaPerSquadra(self,nomeS):
        for s in self.listaSquadre:
            if s.getNome()== nomeS:
                return s.getCitta()
        
    def arbitroFuoriCitta(self):
        ll = Linkedlist()
        for p in self.listaPartite:
            cittaSquad = self._getCittaPerSquadra(p.getNomeSquadraCasa())
            arb = True
            if p.getCittaArbitro() == cittaSquad:
                arb = False
            if arb:
                ll.aggiungiInCoda(p.getNomeArbitro())
        return ll
    
    def _createDictArb(self):
        d = {}
        for p in self.listaPartite:
            arbitro = p.getNomeArbitro()
            squadC = p.getNomeSquadraCasa()
            squadO = p.getNomeSquadraOspite()
            if not arbitro in d:
                d[arbitro]=[]
            d[arbitro].append(squadC)
            d[arbitro].append(squadO)
        return d

    def arbitri3squadre(self):
        ll = Linkedlist()
        d = self._createDictArb()
        items = d.items()
        for it in items:
            x = set(it[1])
            x = list(x)
            if len(x)==3:
                ll.aggiungiInCoda(it[0])
        return ll




def contaelementi(self):
    if self.len < 5:
        raise Exception("lista troppo corta")
    return self._contaelementida(self.testa,0)

def _contaelementida(self,node,prec_value):
    if node is None:
        return 0
    curr = node
    succ = node.succ
    succ_value = succ.value if succ is not None else 0
    media = (prec_value + succ_value)/2
    if curr.value <= media:
        return 1+self._contaelementida(succ,curr)
    else:
        return self._contaelementida(succ,curr)