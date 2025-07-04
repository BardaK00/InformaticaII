#linked list da 0, possiede un valore e un puntatore a un nodo successivo

class Node:
    def __init__(self,value):
        self._value=value
        self._succ=None

    def __repr__(self):
        return str(self._value)
    
    def _getValue(self):
        return self._value
    
    
class Linkedlist:
    def __init__(self, lista = None):
        self._inizializza()
        if lista is not None:
            curr = lista.testa
            while curr is not None:
                self._aggiungiCoda(curr._value)
                curr = curr._succ

    def __iter__(self):
        #dentro il main si può creare una variabile t come iteratore di una lista
        return Iteratore(self)
         

    def _inizializza(self):
        self.testa = None
        self.coda = None
        #necessario specificarla sempre
        self.len=0

    def __str__(self):
        ret="["
        curr = self.testa
        #va avanti finchè non troverà la coda che avrà come succ=None
        while curr is not None:
            #aggiunge in stringa il valore del nodo corrente
            ret += str(curr)
            #se esiste un successivo crea una freccia
            if curr._succ != None:
                ret+="->"
            #assegno a corrente il suo successivo
            curr = curr._succ
            #termina la scrittura con la parentasi quadra chiusa
        ret+="]"
        return ret
    
    def _aggiungiTesta(self,value):
        node = Node(value)
        node._succ=self.testa
        if self.len == 0:
            self.coda=node
        self.testa=node
        self.len+=1

    def _aggiungiCoda(self,value):
        node = Node(value)
        if self.len == 0:
            self.testa = node
        else:
            self.coda._succ = node
        self.coda = node
        self.len += 1

    def _rimuoviTesta(self):
        if self.testa is not None:

            if self.len == 1:
                self._inizializza()

            self.testa = self.testa._succ
            self.len-=1
        if self.len==0:
            raise Exception("lista vuota")
        
    def _rimuoviCoda(self):
        if self.len==0:
            raise Exception("lista vuota")
        if self.len==1:
            self._inizializza()
        else:
            curr = self.testa
            while curr._succ is not self.coda:
                curr=curr._succ
            self.coda=curr
            self.coda._succ = None
        self.len-=1

    #Data una lista inserisci un elemento in una posizione specificata
    def _aggiungiInPos(self,pos,value):
        if pos<0 or pos >self.len:
            raise IndexError("posizione non valida,la posizione può essere massimo:"+str(self.len))
        
        node=Node(value)
        
        if pos==0:
            self._aggiungiTesta(value)
            return 
        if pos==self.len:
            self._aggiungiCoda(value)
            return
        else:
            curr=self.testa
            for _ in range(1,pos):
                curr =curr._succ

            temp = curr._succ
            curr._succ=node
            node._succ=temp
            self.len+=1

    def _rimuoviInPos(self,pos):
        if pos ==0:
            self._rimuoviTesta()
        if pos ==self.len-1:
            self._rimuoviCoda()
        else:
            curr=self.testa
            for _ in range (0,pos-1):
                curr = curr._succ
            temp = curr._succ
            curr._succ=temp._succ
            self.len -=1
   
    def _findMin(self):
        if self.len == 0:
            raise Exception("lista vuota")
        
        min = self.testa._value
        curr = self.testa._succ
        while curr is not None:
            if  curr._value < min:
                min=curr._value
            curr=curr._succ
        return min
    
    #riscrivere _findMin in forma ricorsiva
    def _findMinRic(self):
        if self.len ==0:
            raise Exception("lista vuota")
        return self._minimo_da(self.testa)

    def _minimo_da(self,node):
        #creare il tappo della ricorsione , in questo caso il tappo è quando la lunghezza della lista = 1 
        #e quindi il nodo successivo a l'unico nella lista è none
        if node._succ is None:
            return node._value
        minDestra = self._minimo_da(node._succ)
        if minDestra > self.testa._value:
            return self.testa._value
        else:
            return minDestra
        
    def sommaRic(self):
        if self.testa is None:
            raise Exception("lista vuota")
        return self._somma_ricorsiva(self.testa) 

    def _somma_ricorsiva(self,node):
        if node is None:
            return 0
        return node._value + self._somma_ricorsiva(node._succ)
    
    def _len_ricorsiva(self):
        return self._conta_da(self.testa)
    
    def _conta_da(self,curr):
        if curr is None:
            return 0
        return 1 + self._conta_da(curr._succ)
    #scrivere i metodi:
    #ricerca lineare
    def _ricercaLineare(self,target):
        curr = self.testa
        while curr._succ is not None:
            if curr._value == target:
                return curr
            curr=curr._succ
    
    def _contaOcc(self,target):
        cont = 0
        curr = self.testa
        while curr._succ is not None:
            if curr._value == target:
                cont +=1
            curr=curr._succ
        return cont
    #conta che dato una lista e un valore returna il numero di volte che il valore è contenuto nella lista
    def _ric_da(self,target):
        if self.len == 0:
            raise Exception("lista vuota")
        return self._ricercaRic(self.testa,target)
    
    def _ricercaRic(self,node,target):
        if node is None:
            return 0
        if node._value== target:
            return node._value
        else:
            return self._ricercaRic(node._succ,target)
            
    def contaOccric(self,target):
        if self.len ==0:
            raise Exception ("lista vuota")
        return self._contaOccRic(self.testa,target)
    
    def _contaOccRic(self,node,target):
        if node is None:
            return 0
        if node._value == target:
            return 1 + self._contaOccRic(node._succ,target)
        else:
            return self._contaOccRic(node._succ, target) 
        
            
        
        
    def _findMax(self):
        if self.len == 0:
            raise Exception("lista vuota")
        
        max = self.testa._value
        curr = self.testa._succ
        while curr is not None:
            if  curr._value > max:
                max=curr._value
            curr=curr._succ
        return max
    
        #creare il metodo rimuoviInPos(self,indice) fatto
        #creare il metodo che data una lista restituisce il valore minimo fatto
        #creare il metodo massimo fatto
        
        #metodo __eq__ prendendo come argomento una altra lista(scandire le liste e fermarsi quando un elemento è diverso)
        #o quando l'abiamo scandita tutta
    def __eq__(self,obj):
        if obj is None or not(isinstance(obj,Linkedlist)):
            return False
        
        if obj is self:
            return True
        
        currSelf = self.testa
        currObj = obj.testa

        if self.len != obj.len:
            return False
        
        while currSelf._succ is not None:
            if currSelf._value != currObj._value:
                return False
            currSelf = currSelf._succ
            currObj = currObj._succ
        return True
    
    def __getitem__(self,pos):
        if pos < 0 or pos > self.len:
            raise IndexError
        curr = self.testa
        for _ in range(1,pos+1):
            curr = curr._succ
        return curr

    def __len__(self):
        return self.len
    
    
    def _ricerdaMinIterDa(self):
        it = iter(self)
        if self.len == 0:
            raise Exception("lista vuota")
        return self._ricMinIter(it)
    
    def _ricMinIter(self,iteratore):
        val = next(iteratore)
        if next(iteratore) is None:
            return 
        if val < next(iteratore):
           return val
        else:
            return self._ricMinIter(iteratore)
           
    def _indiceDiOrd(self,target):
        i = 0
        curr = self.testa
        while curr is not None and curr._value <= target:
            if curr._value == target:
                return i
            i+=1
            curr= curr._succ
        return -1
    
    def _aggiungiOrd(self,value):
        if value < self.testa._value or self.len==0:
            self._aggiungiTesta(value)
            return

        n= Node(value)
        curr = self.testa
        while curr is not None and curr._succ is not None and curr._succ._value <= value:
            curr = curr._succ

        n._succ = curr._succ
        curr._succ = n
        self.len+=1

        if n._succ is None:
            self.coda=n
    
    ####################### ESERCIZI D'ESAME ########################################################################

#esercizio n.2 traccia 16 set 2020 (tutor_5)
#Si arricchisca la classe ListaConcatenataInt sviluppata durante il corso con un metodo stesseSottosequenze 
#che restituisca true se e solo se sono verificate entrambe le seguenti condizioni: 
#la lista non è vuota e la sua lunghezza è pari; 
#se un nodo (ad eccezione degli ultimi due) si trova in posizione i  e contiene il valore n, 
#allora il nodo che si trova in posizione i+2 contiene lo stesso valore n. 
#Ad esempio, la lista [7,2,7,2,7,2] soddisfa entrambe le condizioni di cui sopra. Il metodo stesseSottosequenze 
#dovrà essere ricorsivo o invocare un opportuno metodo ricorsivo sulla classe NodoInt.

    def startFrom(self):
        if self.len == 0 or self.len%2!=0:
            return False
        return self.stesseSottosequenze(self.testa)

    def stesseSottosequenze(self,node):
        succ= node._succ
        succSucc = succ._succ
        if succSucc is None:
            return True 
        
        if node._value == succSucc._value:
            return self.stesseSottosequenze(succ)
        else:
            return False

#Si arricchisca la classe ListaConcatenataInt sviluppata durante il corso con un metodo contaTriple() 
#che conta quante volte la lista contiene una sottosequenza di tre elementi consecutivi di cui il primo negativo, 
#il secondo uguale a zero e il terzo positivo. Ad esempio, la lista [5,-1,0,2,-2,-4,0,1,-2,-3,0,3,0,-2,0] 
#contiene tre triple della forma richiesta (in grassetto). Il metodo contaTriple dovrà essere ricorsivo o 
#invocare un opportuno metodo ricorsivo sulla classe NodoInt.  

    def contaTriple(self):
        if self.len < 3:
            raise Exception("la lista contiene meno di 3 elementi ")
        return self._contaTripleRic(self.testa)

    def _contaTripleRic(self,node):
        succ = node._succ
        succSucc = succ._succ
        if succSucc is None:
            return 0
        if node._value < 0 and succ._value == 0 and succSucc._value >0:
            return 1 + self._contaTripleRic(succSucc._succ)
        else:
            return self._contaTripleRic(node._succ)

#Si arricchisca la classe ListaConcatenataInt sviluppata durante il corso con un metodo ordinataTratti che 
#restituisca true se e solo se lista è “ordinata a tratti”. Ossia, scorrendo la lista dall’inizio alla fine, 
#i valori devono essere ordinati in senso crescente fino a che non viene incontrato il numero “delimitatore” 
#0 o viene raggiunta la fine della lista. Dopo ogni occorrenza del delimitatore 0, il senso di ordinamento 
#viene invertito: se prima era crescente, diventa decrescente; se prima era decrescente, diventa crescente. 
#Si assuma che nel primo tratto l’ordinamento debba essere crescente. Si assuma inoltre che una lista vuota 
#soddisfi la proprietà verificata da ordinataTratti. Il metodo ordinataTratti dovrà essere ricorsivo o invocare 
#un opportuno metodo ricorsivo sulla classe NodoInt.  

    def ordinataTratti(self):
        if self.len == 0:
            return True
        return self._ordinataTrattiRic(self.testa,ord=True)
    
    def _ordinataTrattiRic(self,node,ord):
        
        if node is None:
           return True
        print(f"Nodo: {node._value}, Ordinamento crescente: {ord}")  # DEBUG
        succ = node._succ

        if succ is None:
            return True

        if node._value == 0:
            return self._ordinataTrattiRic(succ,not ord)
        
        if succ._value == 0:
            return self._ordinataTrattiRic(succ._succ,not ord)
        
        if ord:
            if node._value < succ._value:
                return self._ordinataTrattiRic(succ,ord)
            else:
                return False
        else:
            if node._value > succ._value:
                return self._ordinataTrattiRic(succ,ord)
            else:
                return False
        
 
       
        
        



    
class Iteratore:
    #lista sta per la lista alla quale va abbinato il costruttore
    def __init__(self,lista):
        self._curr = lista.testa

    def __next__(self):
        if self._curr is None:
            raise StopIteration("non ci sono più elementi")
        val = self._curr._value
        self._curr = self._curr._succ
        return val
    
    def __iter__(self):
        return self
    
    def finito(self):
        return self._curr is None
    

############### INIZIALIZZAZIONE DELLA LINKED LIST ################################
l = Linkedlist()




        
    

l._aggiungiTesta(4)
l._aggiungiTesta(6)
l._aggiungiTesta(8)
l._aggiungiTesta(0)
l._aggiungiTesta(5)
l._aggiungiTesta(3)
l._aggiungiTesta(1)

[1, 3, 5, 0, 8, 6, 4]
print(l)

print(l.ordinataTratti())



























