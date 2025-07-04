#linked list da 0, possiede un valore e un puntatore a un nodo successivo
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
        
     
#esercizio ricorsivo: trovare il minore di una LinkedList di interi.
    def minimoLista(self):
        return self._trovaMinDa(self._testa)
    
    def _trovaMinDa(self,node):
        if node is None:
            return float('inf')
        
        return min(node.value,self._trovaMinDa(node.successivo))


#esercizio ricorsivo: verificare se una LinkedList di interi è simmetrica
    def verificaSimmetrice(self):
        if self.len == 0 or self.len == 1:
            return True
        return self._verificaSimmetria(self._testa,self._testa)

    def _verificaSimmetria(self,testa,node):
        if node is None:
            return True
        
        testa , ok = self._verificaSimmetria(testa,node.successivo)
        if not ok:
            return testa,False
        
        if testa._info != node._info:
            return testa ,False
        
        return testa.successivo,True
    
#esercizio ricorsivo: date 2 linkedlist l1, l2. Creare una linkedlist che contiene tutti 
# gli elementi tali che l1[i] != l2[i]. in tal caso aggiungere alla linkedlist prima l1[i] e 
# poi l2[i]. se le due linkedlist list hanno diversa dimensione, allorché si giunge alla fine 
# di quella più piccola, aggiungere alla linkedlist da restituire gli elementi rimanenti di quella più grande
    
    def nuovall(self,l1,l2):
         return self._nuovall(l1._testa,l2._testa,Linkedlist())
        
    def _nuovall(self,nodeL1,nodeL2,l3):
        if nodeL1 is not None and nodeL2 is not None:
            if nodeL1._info != nodeL2._info:
                l3.aggiungiInCoda(nodeL1._info)
                l3.aggiungiInCoda(nodeL2._info)
            return self._nuovall(nodeL1.successivo,nodeL2.successivo,l3)
            
        if nodeL1 is None and nodeL2 is not None:
            l3.aggiungiInCoda(nodeL2._info)
            return self._nuovall(nodeL1,nodeL2.successivo,l3)
        
        if nodeL2 is None and nodeL1 is not None:
            l3.aggiungiInCoda(nodeL1._info)
            return self._nuovall(nodeL1.successivo,nodeL2,l3)
        
        if nodeL2 is None and nodeL1 is None:
            return l3


#Conta quanti elementi pari ci sono in una linked list.
    def contaelmentiPari(self):
        return self._contaDa(self._testa)
    
    def _contaDa(self,node):
        if node is None:
            return 0
        if node._info % 2 ==0:
            return 1 + self._contaDa(node.successivo)
        return self._contaDa(node.successivo)

#verifica lista palindroma
    def isPalindroma(self):
        self.punt_testa = self.testa
        return self._checkPalindroma(self._testa)
    
    def _checkPalindroma(self,node):
        if node is None:
            return True
        
        if not self._checkPalindroma(node.successivo):
            return False
        if self.punt_testa._info != node._info:
            return False
        
        self.punt_testa = self.punt_testa.successivo
        return True

#Data una lista semplicemente collegata di interi, scrivi un metodo che verifichi se la lista è “speculare” secondo questa definizione:
#La lista è speculare se per ogni elemento i-esimo dall’inizio e i-esimo dalla fine, il valore nel nodo di 
# testa è maggiore o uguale al valore nel nodo corrispondente dalla coda.

    def verificaListaSpeculare(self):
        self.hPointer = self._testa
        return self._verificaListaSpeculareDa(self._testa)
    
    def _verificaListaSpeculareDa(self,node):
        if node is None:
            return True
        if not self._verificaListaSpeculareDa(node.successivo):
            return False
        if self.hPointer._info < node._info:
            return False
        
        self.hPointer = self.hPointer.successivo
        return True
    
#esercizio ricorsivo: trovare la somma degli elementi in posizione pari che si anche trovano nella posizione 
# simmetrica di un’altra lista

    def sommaSimmetrica(self,l2):
        self.hPointerL2 = l2._testa
        return self._sommaSimmetricaDa(self._testa,0)
    
    def _sommaSimmetricaDa(self,node,pos):
        if node is None:
            return 0
        
        
        somma = self._sommaSimmetricaDa(node.successivo,pos+1)
    
        if pos % 2 == 0 and self.hPointerL2 is not None and self.hPointerL2._info == node._info:
            somma += node._info
        
        if self.hPointerL2 is not None:
            self.hPointerL2 = self.hPointerL2.successivo
        
        return somma


#Esercizio 1 – Conta valori maggiori della media
#Data una lista collegata di interi, calcolare ricorsivamente quanti elementi sono maggiori della media 
# aritmetica dei valori contenuti nella lista.

    def valoriMaggioriMedia(self):
        somma,elementi = self._calcolaMedia(self._testa)
        media = somma // elementi
        return self._contaMaggioriDa(self._testa,media)
    
    def _calcolaMedia(self,node):
        if node is None:
            return 0,0
        
        somma,numeroEl = self._calcolaMedia(node.successivo)
        return somma + node._info ,numeroEl + 1
    
    def _contaMaggioriDa(self,node,media):
        if node is None :
            return 0

        if node._info > media:
            return 1 + self._contaMaggioriDa(node.successivo,media)
        else:
            return self._contaMaggioriDa(node.successivo,media)


#Esercizio 2 – Crea lista dei doppi valori
#Data una lista collegata l1, costruire ricorsivamente una nuova lista l2 contenente il doppio di ciascun valore di l1, 
# nello stesso ordine.


    def crealistadoppivalori(self,l1):
        return self._crealista(l1._testa,Linkedlist())
    
    def _crealista(self,node,l2):
        if node is None:
            return l2
        l2.aggiungiInCoda((node._info*2))
        return self._crealista(node.successivo,l2)
    


#Esercizio 3 – Verifica ordine crescente simmetrico
#Data una lista collegata di interi, verificare ricorsivamente se per ogni coppia simmetrica di elementi 
# (es: primo e ultimo, secondo e penultimo, ecc.) vale la proprietà che il primo è minore o uguale al simmetrico.


    def verificaOrdineSimmetrico(self):
        self.hPointer = self._testa
        return self._verificaOrdineSimmetrico(self._testa)
    
    def _verificaOrdineSimmetrico(self,node):
        if node is None:
            return True
        
        if not self._verificaOrdineSimmetrico(node.successivo):
            return False
        
        if node._info < self.hPointer._info:
            return False
        
        self.hPointer = self.hPointer.successivo
        return True
    
#Date due liste l1 e l2, costruire ricorsivamente una terza lista l3 che contiene solo i valori comuni tra l1 e l2, 
# ma inseriti in ordine alternato (prima un elemento di l1, poi uno di l2, ecc.). Se non ci sono più valori comuni 
# da una delle due, si ignorano quelli rimanenti.

    def listaAlternata(self,l1,l2):
        return self._creaListaAlternata(l1._testa,l2._testa,Linkedlist(),True)
    
    def _creaListaAlternata(self,nodeL1,nodeL2,lista3,alterna):
        if nodeL1 is None or nodeL2 is None:
            return lista3
        
        if nodeL1._info == nodeL2._info and alterna:
            lista3.aggiungiInCoda(nodeL1._info)
            alterna =False
        else:
            return self._creaListaAlternata(self,nodeL1.successivo,nodeL2,lista3,alterna)

        if nodeL1._info == nodeL2._info and not alterna:
            lista3.aggiungiInCoda(nodeL2._info)
            alterna =True
        else:
            return self._creaListaAlternata(self,nodeL1,nodeL2.successivo,lista3,alterna)
    
#3. Verifica ricorsivamente se una lista è ordinata in modo strettamente crescente
#Restituisce True se ogni elemento è strettamente maggiore del precedente.

    def verificaOrdinamento(self):
        return self._verificaDa(self._testa)
    
    def _verificaDa(self,node):
        if node is None or node.successivo is None:
            return True
        if node._info > node.successivo._info:
            return False
        return self._verificaDa(node.successivo)
    
#1. Conta gli elementi duplicati consecutivi
#Scrivi una funzione ricorsiva che conta quanti elementi consecutivi uguali ci sono nella lista.
#Input: 1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4
#(Conta i duplicati consecutivi: 1 duplicato, 3 duplicato due volte)

    def contaDuplicati(self):
        return self._contaDa(self._testa)
    
    def _contaDa(self,node):
        if node is None or node.successivo is None:
            return 0
        if node._info == node.successivo._info:
            return 1+ self._contaDa(node.successivo)
        else:
            return self._contaDa(node.successivo)
        
#5. Cancella ricorsivamente tutti gli elementi pari da una lista
#Restituisci la lista senza elementi pari.

    def cancellaPari(self):
        return self._cancellaPariDa(self._testa,0)
    
    def _cancellaPariDa(self,node,pos):
        if node is None:
            return 
        if node._info % 2 != 0:
            return self._cancellaPariDa(node.successivo,pos+1)
        else:
             self.rimuoviInPos(node._info,pos)
             return self._cancellaPariDa(node,pos)
    #######ESERCIZI DA CHATGPT #############
    #FUNZIONE CHE RIMUOVE TUTTI I NODI UN CERTO VALORE

    def removeValue(self,value):
        if self._testa is None:
            raise Exception("lista vuota")
        
        while self._testa._info == value:
            self._rimuoviTesta()
        return self._removeFrom(self._testa,value)
    
    def _removeFrom(self,node,value):
        if node is None or node.successivo is None:
            return 
        prec = node
        curr = node.successivo
        if curr._info == value:
            prec.successivo = curr.successivo
            self._removeFrom(node,value)
        else:
            self._removeFrom(node.successivo,value)
            
####### trova la lunghezza fino ad un valore dato, se il valore non è in lista return -1
    
    def lenFinoA(self,valore):
        if self._checkValoreInLista(self._testa,valore):
            return self._calcLenFinoA(self._testa,valore)
        else:
            return -1
        
    def _checkValoreInLista(self,node,valore):
        if node is None:
            return False
        if node._info == valore:
            return True
        return self._checkValoreInLista(node.successivo,valore)
        
    def _calcLenFinoA(self,node,valore):
        if node._info == valore:
            return 0
        return 1 + self._calcLenFinoA(node.successivo,valore)


## crea una lista fino a n crescente
    def crealistafinoa(self,n):
        if self._testa is not None:
            raise Exception("la lista contiene già dei valori")
        self._crealistaDa(n)
    
    def _crealistaDa(self,n):
        if n == 0:
            return 
        self._aggiungiInTesta(n)
        self._crealistaDa(n-1)

#####scrivi una funzione che tronca una lista e restituisce i primi n nodi

    def truncate(self,n):
        return self._troncaDa(self._testa,n)
    
    def _troncaDa(self,node,n):
        if node is None:
            return 
        if n != 1:
            return self._troncaDa(node.successivo,n-1)
        else:
            node.successivo = None
            return
        
#### scrivi una funzione che duplica ogni nodo in una lista

    def duplicates_nodes(self):
        if self._testa is None:
            raise Exception("lista vuota")
        return self._duplidaDa(self._testa)
    
    def _duplidaDa(self,node):
        if node is None or node.successivo is None:
            return 
        newNode = Node(node._info)
        temp = node.successivo
        node.successivo = newNode
        newNode.successivo = temp
        self._duplidaDa(temp)

    ####### scrivere una funzione che riturni true se l1[i] == l2[i] per ogni i 
    def are_equal(self,l2):#se la lista self che chiama il metodo è uguale ad l2
        if self._testa is None or l2._testa is None:
            raise Exception("una delle due lista è vuota")
        if self._len != l2._len:
            raise Exception("le due liste hanno diverse lunghezze")
        return self._checkEqual(self._testa,l2._testa)

    def _checkEqual(self,nodeSelf,nodeL2):
        if nodeSelf is None and nodeL2 is None:
            return True
        if not nodeSelf._info == nodeL2._info:
            return False
        return self._checkEqual(nodeSelf.successivo,nodeL2.successivo)


### scrivere una funzione che elimina i duplicati se la lista è ordinata
    def deleteDuplicates(self):
        if self._testa is None:
            raise Exception("lista vuota")
        if self._checkOrdinamento(self._testa):
            self._rimuoviDa(self._testa)
        else:
            raise Exception("lista non ordinata...abort")

    def _checkOrdinamento(self,node):
        if node is None or node.successivo is None:
            return True
        
        if not node._info <= node.successivo._info:
            return False
        return self._checkOrdinamento(node.successivo)
    
    def _rimuoviDa(self,node):
        if node is None or node.successivo is None:
            return 
        curr = node.successivo
        if node._info == curr._info:
            node.successivo = curr.successivo
            self._rimuoviDa(node)
        else:
            self._rimuoviDa(node.successivo)
            
    ##### scrivere una funzione da data una lista l2 e self ordinate le unisce in modo ordinato,
    #presupporre che le liste siano già ordinate

    def unisci_liste(self,l2):
        if self._testa is None or l2._testa is None:
            raise Exception("una delle due liste è vuota")
        return self._unisciListeDa(self._testa,l2._testa,Linkedlist())

    def _unisciListeDa(self,nodeSelf,nodeL2,listaUnita):
        if nodeL2 is None and nodeSelf is None:
            return listaUnita
        
        if nodeL2 is None:
            return self._AddOther(nodeSelf,listaUnita)
        
        if nodeSelf is None:
            return self._AddOther(nodeL2,listaUnita)
            
        if nodeSelf._info <= nodeL2._info:
            listaUnita._aggiungiCoda(nodeSelf._info)
            return self._unisciListeDa(nodeSelf.successivo,nodeL2)

        if nodeSelf._info > nodeL2._info:
            listaUnita._aggiungiCoda(nodeL2._info)
            return self._unisciListeDa(nodeSelf,nodeL2.successivo)

        return listaUnita
    
    def _AddOther(self,node,listaUnita):
        if node is None:
            return listaUnita
        listaUnita._aggiungiCoda(node._info)
        return self._AddOther(node.successivo)

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

print(l.valori())



























