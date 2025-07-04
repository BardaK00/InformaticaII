class Node:
    def __init__(self,value):
        self.succ = None
        self.value=value

    def __repr__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self):
        self._inizializza()
    
    def _inizializza(self):
        self._testa= None
        self._coda=None
        #necessaria per poterci lavorare di sopra sennò servirebbe un iterazione che scandisca tutti gli 
        #elementi e aumenti un contatore
        self._len=0

    def _aggiungiCoda(self,value):
        node=Node(value)
        #se nella lista non esiste il primo valore aggiunto in coda sarà anche l'unico elemento della lista
        #quindi ne diventa anche la testa
        if self._len==0:
            self.testa=node
        else:
            self._cosasucc=node
        self._coda=node
        self._len+=1

    def _aggiungiTesta(self,value):
        node=Node(value)
        node.succ=self._testa
        self._testa=node
        if self._len==0:
            self._coda=node
        self._len+=1

    def __repr__(self):
        ret="["
        curr = self._testa
        #va avanti finchè non troverà la coda che avrà come succ=None
        while curr is not None:
            #aggiunge in stringa il valore del nodo corrente
            ret += str(curr)
            #se esiste un successivo crea una freccia
            if curr.succ != None:
                ret+="->"
            #assegno a corrente il suo successivo
            curr = curr.succ
            #termina la scrittura con la parentasi quadra chiusa
        ret+="]"
        return ret
    



    
l=Linkedlist()
l._aggiungiTesta(5)
l._aggiungiTesta(10)
l._aggiungiTesta(15)
print(l)
