class Node:
    def __init__(self,value):
        self.value = value
        #punta ad un albero coi predecessori
        self.Lson = None
        #punta ad un albero coi successori 
        self.Rson = None

    def __repr__(self):
        return str(self.value)
    
class BinaryTree:
    def __init__(self):
        self._inizializza()
    
    def _inizializza(self):
        self._root = None
        self._card = 0
    
    def _add_node_iterative(self,value):
        self._card +=1
        if self._root is None:
            self.root = Node(value)
        else:
           padre = self._root
           inserito = False

           while not inserito:
                if value <= padre.Lson.value:
                    if padre.Lson is None:
                        padre.Lson = Node(value)
                        inserito = True
                    else:
                        padre = padre.Lson
                else:
                    if value > padre.Lson.value:
                                if padre.Rson is None:
                                    padre.Rson=Node(value)
                                    inserito = True
                                else:
                                    padre = padre.Rson
    def __repr__(self):
        return self.convertFrom()
############# AGGIUNGE UN VALORE ALL'ALBERO ################        
    def aggiungi(self,value):
        if self._root is None:
            self._root = Node(value)
            self._card +=1
        else:
            self._card +=1
            return self.aggiungiDa(self._root,value)
    
    def aggiungiDa(self,node,value):
        if node is None:
            return Node(value)
        
        if value <= node.value:
            node.Lson= self.aggiungiDa(node.Lson,value)
        else:
            node.Rson=self.aggiungiDa(node.Rson,value)
        return node
    
############# TRASFORMA L'ALBERO IN STRINGA PRINTABILE ################
    def convertFrom(self):
        return " "+self.string_convert(self._root)
    
    def string_convert(self,node):
        if node is None:
            return ""
        return str(self.string_convert(node.Lson))+" "+str(node.value)+" "+str(self.string_convert(node.Rson))
    
############# CONTA OCCORRENZE DI UN VALORE NELL'ALBERO ################    
    def contaOcc(self,value):
        return self._contaDa(self._root,value)
    
    def _contaDa(self,node,value):
        if node is None:
            return 0
        cont = 0
        if value == node.value:
            cont+= 1

        cont+= self._contaDa(node.Lson,value)
        cont+=self._contaDa(node.Rson,value)
        return cont
    
############# CALCOLA PROFONDITA' E BILANCIAMENTO DELL'ALBERO ################
    def CalcProfondità(self):
        if self._card<=1:
            return 0
        return self._CalcolaProfonditàDa(self._root)

    def _CalcolaProfonditàDa(self,node):
        if node is None:
            return 0
        profL =self._CalcolaProfonditàDa(node.Lson)
        profR =self._CalcolaProfonditàDa(node.Rson)
        return max(profL,profR)+1
    
    def isBilanciato(self):
        if self._card == 1:
            return False
        if abs(self._CalcolaProfonditàDa(self._root.Lson) - self._CalcolaProfonditàDa(self._root.Rson)) == 1:
            return True
        return False
    
############# TROVA MINIMO ################   
    def findMin(self):
        if self._card==0:
            raise Exception("albero vuoto")
        return self.findMinDa(self._root)
    
    def findMinDa(self,node):
        if node is None:
            return  float("inf")
        minimo = node.value
        minL = self.findMinDa(node.Lson)
        minR = self.findMinDa(node.Rson)
        return min(minimo,minR,minL)
    
############# TROVA MASSIMO ################
    def findMax(self):
        if self._card==0:
            raise Exception("albero vuoto")
        return self.findMaxDa(self._root)
    def findMaxDa(self,node):
        if node is None:
            return float("-inf")
        maxR= self.findMaxDa(node.Rson)
        maxL= self.findMaxDa(node.Lson)
        return max(node.value,maxL,maxR)
    

###################ESERCIZIO D'ESAME RICORSIVO TUTOR 6###################
#dato x verificare che almeno un cammino ,sommando i suoi e facendone la media sia maggiore di x

    def verificaCammino(self,x):
        if self._card==0:
            return None
        return self._verificaCamminoDa(self._root,x,0,0)
    
    def _verificaCamminoDa(self,node,x,cont,somma):
        
        if node is None:
            return False
        somma = somma + node.value
        cont +=1
        if node.Lson is None and node.Rson is None:
            return somma/(cont)>x
        return self._verificaCamminoDa(node.Rson,x,cont,somma) or self._verificaCamminoDa(node.Lson,x,cont,somma)
    
        
########ESERCIZI RICORSIVI CON CHATGPT #######################
#Somma delle foglie
#Calcola la somma di tutti i valori contenuti nei nodi foglia dell’albero.  

    def sommaRicorsiva(self):
        if self.cardinalità == 0:
            raise Exception("albero vuoto")
        return self._contaDa(self.radice,0)
    
    def _contaDa(self,node,somma):
        if node is None:
            return 0
        somma = node.value + self._contaDa(node.Lson,somma) + self._contaDa(node.Rson,somma)
        return somma
   

#Conta nodi con un solo figlio
#Conta quanti nodi nell’albero hanno esattamente un solo figlio (o sinistro o destro).

    def contaNodiConSoloUnFiglio(self):
        if self.cardinalità == 0:
            raise Exception("albero vuoto")
        return self._contaSoloUnFiglioDa(self.radice)
    
    def _contaSoloUnFiglioDa(self,node):
        if node is None:
            return 0
        
        if (node.Rson is None) != (node.Lson is None):
            return 1 + self._contaSoloUnFiglioDa(node.Lson) + self._contaSoloUnFiglioDa(node.Rson)
        else:
            return self._contaSoloUnFiglioDa(node.Lson) + self._contaSoloUnFiglioDa(node.Rson)


#Verifica cammino con somma esatta
#Dato un numero k, verifica se esiste un cammino dalla radice a una foglia la cui somma dei valori 
#sia esattamente uguale a k.

    def verificaCamminoSommaEsatta(self,k):
        if self.cardinalità == 0:
            raise Exception("albero vuoto")
        return self._verificaCamminoDa(self.radice,0,k)
    
    def _verificaCamminoDa(self,node,somma,k):
        if node is None:
            return False
        somma += node.value
        if node.Rson is None and node.Rson is None:
            return somma == k
        return self._verificaCamminoDa(node.Lson,somma,k) or self._verificaCamminoDa(node.Rson,somma,k)
        
#Cammini con valore massimo
# Trova il valore massimo ottenibile sommando i valori lungo un qualsiasi cammino dalla radice a una foglia.
        
    def ValoreMassimoFinoAFoglia(self):
        if self.cardinalità== 0:
            raise Exception("lista vuota")
        if self.cardinalità == 1:
            return self.radice.valore
        return self._calcValoreMassimoDa(self.radice,0,0)
    
    def _calcValoreMassimoDa(self,node,max_attuale):
        if node is None:
            return -9999999
        if node.Rson is None and node.Lson is None:
            return max_attuale + node.value
        
        max_attuale+=node.value

        if node.Lson is None and node.Rson is None:  # foglia
            return max_attuale

        max_destro = self._calcValoreMassimoDa(node.Rson,max_attuale)
        max_left =self._calcValoreMassimoDa(node.Lson,max_attuale)
        
        return max(max_left,max_destro)


    def controllaDuplicati(self):
        return self._controllaDuplicatiDa(self.radice,list())
    
    def _controllaDuplicatiDa(self,node,valorivisti):
        if node is None:
            return False
        
        if node.value in valorivisti:
            return True
        valorivisti.append(node.value)
        return (self._controllaDuplicatiDa(node.Lson, valorivisti) or self._controllaDuplicatiDa(node.Rson, valorivisti))

    def contaNodiInterni(self):
        return self._contaNodiInterniDa(self.radice)
    
    def _contaNodiInterniDa(self,node):
        if node is None:
            return 0
        if node.Rson is None and node.Lson is None:
            return 0
        return 1+self._contaNodiInterniDa(node.Lson) + self._contaNodiInterniDa(node.Rson)

    ##corretto al primo tentativo
    def contaNodiPari(self,livello):
        return self._contaNodiPariDa(self.radice)
    
    def _contaNodiPariDa(self,node):
        if node is None:
            return 0
        if node.value % 2 == 0:
            return 1+self._contaNodiPariDa(node.Lson)+self._contaNodiPariDa(node.Rson)
        else:
            return self._contaNodiPariDa(node.Lson)+self._contaNodiPariDa(node.Rson)


    #3. Calcola la profondità massima di un nodo che contiene un valore maggiore di x.
    def calcolaProfMaggioreX(self,x):
        return self._calcolaDa(self.radice,x)
    
    def _calcolaDa(self,node,x):
        if node is None:
            return 0
        
        if node.value > x:
            profMaxDestra=1 + self._calcolaDa(node.Rson,x)
            profMaxSinistra =1 + self._calcolaDa(node.Lson,x)
        else:
            profMaxDestra=self._calcolaDa(node.Rson,x)
            profMaxSinistra =self._calcolaDa(node.Lson,x)
        return max(profMaxDestra,profMaxSinistra)

#4. Trova il valore minimo fra i nodi interni (cioè non foglia).
    def trovaFogliaMin(self):
        return self._calcMinFoglia(self.radice,self.radice.value)
    
    def _calcMinFoglia(self,node,minimoAtt):
        if node is None:
            return float('inf')
        if minimoAtt > node.value:
            minimoAtt=node.value

        if node.Rson is None and node.Lson is None:
            return minimoAtt
        
        minimoDestro=self._calcMinFoglia(node.Rson,minimoAtt)
        minimoSinistro=self._calcMinFoglia(node.Lson,minimoAtt)
        return min(minimoDestro,minimoSinistro)

    def calcolaMediaFoglia(self):
        return self._calcolaMediaDa(self.radice,0,0)
    
    def _calcolaMediaDa(self,node,somma,cont):
        if node is None:
            return 0
        if node.Rson is None and node.Lson is None:
            somma= node.value + self._calcolaMediaDa(node.Rson,somma,cont+1) + self._calcolaMediaDa(node.Lson,somma,cont+1)
        else:
            return (self._calcolaMediaDa(node.Rson,somma,cont) or self._calcolaMediaDa(node.Lson,somma,cont))
        return somma / cont
    

##########################. ESERCIZI A DIFFICOLTA CRESCENTE SULL'ALBERO DA CHATGPT ###########################
#🟢 Livello 1 — Base
#1.Somma dei nodi
#Calcola la somma di tutti i valori dei nodi dell’albero.

    def sommaNodi(self):
        return self._sommaNodiDa(self.root,0)
    
    def _sommaNodiDa(self,node):
        if node is None:
            return 0
        
        return node.value + self._sommaNodiDa(node.Rson) + self._sommaNodiDa(node.Lson)

    
#2.Conta nodi
#Conta quanti nodi contiene il BST.
    def contaNodi(self):
        return self._contaNodiDa(self.root)
    
    def _contaNodiDa(self,node):
        if node is None:
            return 0
        
        return 1+self._contaNodiDa(node.Rson)+self._contaNodiDa(node.Lson)
    
#3.Conta foglie
#Conta il numero di foglie presenti nell’albero

    def contaFoglie(self):
        return self._contaFoglieDa(self.root)
    
    def _contaFoglieDa(self,node):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return 1
        return self._contaFoglieDa(node.Rson)+self._contaFoglieDa(node.Lson)
        
        
#4.Trova valore minimo
#Restituisci il valore minimo presente nel BST.

    def trovaMinimoRicorsivo(self):
        return self._trovaMinimoDa(self.root)
    
    def _trovaMinimoDa(self,node):
        if node is None:
            return float('-inf')
        val = node.value
        
        minSx=self._trovaMinimoDa(node.Lson)
        minDx=self._trovaMinimoDa(node.Rson)
        return min(val,minDx,minSx)

        
#esercizio d'esame
#Dato un albero binario di ricerca (BST) e due valori p e q presenti nei nodi 
#dell'albero, scrivi una funzione ricorsiva per trovare l'antenato comune più vicino 
#(Lowest Common Ancestor, LCA) dei due nodi che contengono quei valori.

    def calcolaLivelloMinoreDi(self,liv:int):
        return self._calcolaDa(self.root,0,liv)
    
    def _calcolaDa(self,node,liv_att,liv):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            if liv_att <= liv:
                return 1
        else:
            return(self._calcolaDa(node.Rson,liv_att+1,liv) + self._calcolaDa(node.Lson,liv_att+1,liv) )
    

#2. Esiste foglia con valore compreso tra A e B
#Traccia:
#Restituire True se esiste almeno una foglia il cui valore è compreso tra a e b, estremi inclusi.


    def fogliaTraAeB(self,a,b):
        return self._trovaFoglia(self.root,a,b)
    
    def _trovaFoglia(self,node,a,b):
        if node is None:
            return False
        if node.Rson is None and node.Lson is None:
            if node.value >= a and node.value <= b:
                return True
        else:
            return (self._trovaFoglia(node.Lson,a,b) or self._trovaFoglia(node.Rson,a,b))

#1. Conta nodi con valore minore di X
#Traccia:Contare quanti nodi dell’albero hanno valore strettamente minore di un valore intero x.

    def contaNodiMinoriDi(self,x):
        return self._contaNodiMinoriDa(self.root,x)
    
    def _contaNodiMinoriDa(self,node,x):
        if node is None:
            return 0
        
        if node.value < x:
            return 1 + self._contaNodiMinoriDa(node.Lson,x) + self._contaNodiMinoriDa(node.Rson,x)
        
        return self._contaNodiMinoriDa(node.Lson,x) + self._contaNodiMinoriDa(node.Rson,x)
         

#Tutte le foglie sono a livello almeno L
#Traccia:Restituire True se tutte le foglie dell’albero si trovano ad un livello maggiore o uguale a L.

    def foglieLivelloMaggioreDi(self,L):
        result =  self._foglieMaggDa(self.root,0,L)
        if result:
            return True
        return False
    def _foglieMaggDa(self,node,liv_att,L):
        if node is None:
            return False

        if node.Rson is None and node.Lson is None:
            return liv_att >= L
        
        return (self._foglieMaggDa(node.Rson,liv_att +1 ,L) or self._foglieMaggDa(node.Lson,liv_att +1 ,L))
    
#Conta nodi interni con due figli
#Traccia:Restituire il numero di nodi che non sono foglie e che hanno sia figlio sinistro che destro (cioè due figli).

    def contaNodiConFigli(self):
        return self._contaNodiConFigliDa(self.root)
    
    def _contaNodiConFigliDa(self,node):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return 0 #anche se comunque la verifica dopo esclude le foglie perchè tutti e due i figli devono non essere none
        
        if node.Lson is not None and node.Rson is not None:
            return 1 + self._contaNodiConFigliDa(node.Rson) + self._contaNodiConFigliDa(node.Lson)
        
        return self._contaNodiConFigliDa(node.Rson) + self._contaNodiConFigliDa(node.Lson)
    
#🔁 Esercizio – Somma dei nodi interni con due figli
#Traccia:Restituire la somma dei valori contenuti nei nodi interni dell’albero 
#che hanno sia figlio sinistro che figlio destro.

    def sommaNodiConFigli(self):
        return self._sommaNodiConFigliDa(self.root,0)
    
    def _sommaNodiConFigliDa(self,node):
        if node is None:
            return 0
        
        if node.Rson is not None and node.Lson is not None:
            return node.value + self._sommaNodiConFigliDa(node.Rson) + self._sommaNodiConFigliDa(node.Lson)
        else:
            return self._sommaNodiConFigliDa(node.Rson) + self._sommaNodiConFigliDa(node.Lson)
        
#Verifica se esiste un nodo con valore x e almeno un figlio
#Traccia:Restituire True se esiste un nodo con valore x che non è foglia (ha almeno un figlio).


    def verMaggioreXeConUnFiglio(self,x:int):
        return self._verDa(self.root,x)
    
    def _verDa(self,node,x):
        if node is None:return False

        if node._value == x:
            if node.Lson is not None or node.Rson is not None:
                return True
        return (self._verDa(node.Rson,x) or self._verDa(node.Lson,x))
    

#6. Calcola il livello massimo di una foglia
#Traccia:Restituire il massimo livello in cui si trova una foglia 
#(utile per verificare la "profondità" dell'albero).

    def maxLevel(self):
        return self._calcMaxLevel(self.root,0)
    
    def _calcMaxLevel(self,node,liv_att):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return 1 
        maxL = self._calcMaxLevel(node.Lson,liv_att+1)
        maxR = self._calcMaxLevel(node.Rson,liv_att+1)

        return 1 + max(maxL,maxR)
    

#7. Conta le foglie con valore pari
#Traccia:Restituire il numero di foglie che hanno valore pari.

    def foglieConValorePari(self):
        return self._contaFogliePariDa(self.root)
    
    def _contaFogliePariDa(self,node):
        if node is None:return 0
        
        if node.Rson is None and node.Lson is None:
            if node.value % 2 == 0:return 1
            else:return 0
        else: return self._contaFogliePariDa(node.Rson) + self._contaFogliePariDa(node.Lson)

############# ESERCIZI DIFFICOLTA' 2 ########################
#1. Somma valori nodi foglia a livello pari
#Traccia: Calcolare la somma dei valori di tutte le foglie che si trovano 
#a un livello pari (0, 2, 4, …).

    def sommaFoglieLivPari(self):
        return self._sommaFoglieLivPariDa(self.root,0)
            
    def _sommaFoglieLivPariDa(self,node,liv_att):
        if node is None:
            return 0
        if node.Rson is None and node.Lson is None:
            if liv_att % 2 == 0:
                return node.value
            else:return 0
        return self._sommaFoglieLivPariDa(node.Rson,liv_att +1) + self._sommaFoglieLivPariDa(node.Lson,liv_att +1)
    
#2. Conta nodi con un solo figlio
#Traccia: Restituire il numero di nodi che hanno esattamente un solo figlio 
#(o sinistro o destro, ma non entrambi).

    def contaNodiUnicoFiglio(self):
        return self._contaNodiUnicoFiglioDa(self.root)
    
    def _contaNodiUnicoFiglio(self,node):
        if node is None:
            return 0
        
        if node.Rson is None or node.Lson is None:
            if node.Rson is None and node.Lson is None:
                return 0
            return 1 + self._contaNodiUnicoFiglio(node.Rson)+self._contaNodiUnicoFiglio(node.Lson)
        else:return self._contaNodiUnicoFiglio(node.Rson)+self._contaNodiUnicoFiglio(node.Lson)

    
#3. Verifica se esiste un percorso dalla radice a una foglia con somma valori pari a S
#Traccia: Restituire True se esiste un percorso dall’alto (radice) fino a una foglia 
#tale che la somma dei valori dei nodi lungo quel percorso sia esattamente S.

    def sommaRadiceFogliaPariA(self,S):
        return self._sommaRadiceFogliaDa(self.root,S)

    def _sommaRadiceFogliaDa(self,node,S):
        if node is None:
            return False
        
        S -= node.value
        if node.Lson is None and node.Rson is None:
            return S == 0
        else:
            return (self._sommaRadiceFogliaDa(node.Lson,S) or self._sommaRadiceFogliaDa(node.Rson,S))

#4. Conta foglie con valore maggiore della media dell’albero
#Traccia: Calcolare la media dei valori di tutti i nodi, 
#e poi restituire il numero di foglie con valore maggiore di questa media.

    def nodiMaggioreMedia(self):
        sum,numero = self._calcSommaeContRic(self.root)
        med = sum/numero
        return self._calcNodiMaggioriMedia(self.root,med)
    
    def _calcNodiMaggioriMedia(self,node,med):
        if node is None:
            return 0
        if node.value >med:
            return 1+self._calcNodiMaggioriMedia(node.Rson)+self._calcNodiMaggioriMedia(node.Lson)    
        else:
            return self._calcNodiMaggioriMedia(node.Rson)+self._calcNodiMaggioriMedia(node.Lson)

    def _calcSommaeContRic(self,node):
        if node is None:
            return (0,0)
        sL, cL = self._calcSommaeContRic(node.Lson)
        sR, cR = self._calcSommaeContRic(node.Rson)
        return (sL + sR + node.value, cL + cR + 1)
    
#5. Trova il valore minimo tra i nodi che hanno due figli
#Traccia: Restituire il valore minimo tra tutti i nodi che hanno sia figlio 
#sinistro che destro. Se non esistono, restituire None.

    def minimoConEntrambi(self):
        minimo = self._calcMinEntrambi(self.root)
        if minimo == float('+inf'):
            return None
        return minimo
    
    def _calcMinEntrambi(self,node):
        if node is None:
            return float('+inf')
        minR=self._calcMinEntrambi(node.Rson)
        minS=self._calcMinEntrambi(node.Lson)
        if node.Rson is not None and node.Lson is not None:
            return min(node.value,minR,minS)
        else:
            return min(minR,minS)
        
#6. Verifica se l’albero è perfettamente bilanciato
#Traccia: Restituire True se per ogni nodo la differenza tra la profondità massima 
#e minima delle sue foglie è al massimo 1, altrimenti False.


    def verificaBilanciamento(self):
        prof_max = self._calcMaxProf(self.root)
        return self._verificaDa(self.root,0,prof_max)
    
    def _verificaDa(self,node,liv_attuale,prof_max):
        if node is None:
            return True
        if prof_max - liv_attuale <=1:
            return (self._verificaDa(node.Rson,liv_attuale +1,prof_max) and self._verificaDa(node.Lson,liv_attuale +1,prof_max))
        else:
            return False


    def _calcMaxProf(self,node):
        if node is None:
            return 0
        maxPR=self._calcMaxProf(node.Rson)
        maxPL=self._calcMaxProf(node.Lson)
        return max(maxPR+1,maxPL+1)

        
#Conta i nodi con valore maggiore del genitore
#Traccia: Restituire il numero di nodi il cui valore è maggiore di 
#quello del nodo genitore (la radice non viene considerata).

    def nodiMaggioreGenitore(self):
        return self._verificaNodiGen(self.root)
    
    def _verificaNodiGen(self,node):
        if node is None:
            return 0

        val_gen = node.value
        if (node.Rson is not None and node.Rson.value> val_gen )or (node.Lson is not None and node.Lson.value > val_gen):
            return 1 + self._verificaNodiGen(node.Lson) + self._verificaNodiGen(node.Rson)
        else:
            return self._verificaNodiGen(node.Lson) + self._verificaNodiGen(node.Rson)
        
#7. Conta nodi con valore maggiore della somma dei figli
#Traccia: Restituire il numero di nodi il cui valore è strettamente maggiore 
# della somma dei valori dei suoi figli (0 se un figlio è assente).

    def valMaggioreDeiFigli(self):
        return self._calcolaValMaggiore(self.root)
    
    def _calcolaValMaggiore(self,node):
        if node is None:
            return 0
        
        if node.Rson is None:
            return self._calcolaValMaggiore(node.Lson)
        if node.Lson is None:
            return self._calcolaValMaggiore(node.Rson)
        
        if node.value> node.Rson.value + node.Lson.value:
            return 1+ self._calcolaValMaggiore(node.Lson) + self._calcolaValMaggiore(node.Rson)
        else:
            return self._calcolaValMaggiore(node.Lson) + self._calcolaValMaggiore(node.Rson)


#8.Conta nodi con entrambi i figli foglie
#Traccia: Restituire il numero di nodi che hanno sia figlio sinistro sia figlio destro, e
#che entrambi i figli sono foglie.

    def contaNodiConFigliFoglie(self):
        return self._contaNCFFDa(self.root)
    
    def _contaNCFFDa(self,node):
        if node is None:
            return 0
        
        Rson = node.Rson
        Lson = node.Lson
        if (Rson is not None and Rson.Rson is None and Rson.Lson is None  ) and ( Lson is not None and Lson.Lson is None and Lson.Rson is None ):
            return 1 + self._contaNCFFDa(node.Rson) + self._contaNCFFDa(node.Lson)
        else:
            return self._contaNCFFDa(node.Rson) + self._contaNCFFDa(node.Lson)

#10. Restituisci la somma dei valori di tutti i nodi a livello L
#Traccia: Calcolare la somma dei valori di tutti i nodi che si trovano esattamente 
#al livello L (radice livello 0).
    def sommaNodiLivello(self,L):
        return self._calcolaSommaNodiLivello(self.root,L,0)
    
    def _calcolaSommaNodiLivello(self,node,L,liv_attuale):
        if node is None:
            return 0
        
        if liv_attuale == L:
            return node.value + self._calcolaSommaNodiLivello(node.Lson,L,liv_attuale +1) + self._calcolaSommaNodiLivello(node.Rson,L,liv_attuale +1)
        else:
            return self._calcolaSommaNodiLivello(node.Lson,L,liv_attuale +1) + self._calcolaSommaNodiLivello(node.Rson,L,liv_attuale +1)
        
#11. Verifica se tutti i nodi interni hanno due figli
#Traccia: Restituire True se ogni nodo che non è foglia ha esattamente due figli.

    def verificaNodiInterni(self):
        return self._verificaNodiInterniDa(self.root)

    def _verificaNodiInterniDa(self,node):
        if node is None:
            return False
        
        if node.Lson is None and node.Rson is None:
            return True 
        
        if node.Lson is None or node.Rson is None:
            return False
        
        
        return (self._verificaNodiInterniDa(node.Lson) and self._verificaNodiInterniDa(node.Rson))
        

#12. Calcola la differenza tra la somma dei valori dei nodi a livelli pari e la somma 
#di quelli a livelli dispari
#Traccia: Restituire la differenza tra la somma dei nodi che stanno a livelli pari e la 
#somma di quelli a livelli dispari.

#(sum:nodiLivPARi)-(sum:nodiLivDispari)

    def diffNodi(self):
        sommaPari,sommaDispari =  self._calcDiffNodi(self.root,0)
        return sommaPari - sommaDispari
    def _calcDiffNodi(self,node,liv_att):
        if node is None:
            return 0,0
        
        leftP,leftD =self._calcDiffNodi(node.Lson,liv_att+1)
        rightP,rightD =self._calcDiffNodi(node.Rson,liv_att+1)

        if liv_att % 2 ==0:
            sommaPari = node.value + leftP + rightP
            sommaDispari = leftD+rightD

        else:
            sommaPari =leftP + rightP
            sommaDispari = node.value+leftD+rightD

        return sommaPari,sommaDispari
    

        
        
#13. Conta nodi con valore multiplo di k
#Traccia: Restituire il numero di nodi il cui valore è multiplo di un intero k fornito in input.

    def nodiMultiploDi(self,k):
        return self._contNodiMul(self.root,k)
    
    def _contaNodiMul(self,node,k):
        if node is None :
            return 0
        
        if node.value % k==0:
            return 1 + self._contaNodiMul(node.Rson,k) + self._contaNodiMul(node.Lson,k)
        else:
            return self._contaNodiMul(node.Rson,k) + self._contaNodiMul(node.Lson,k)
        

    
#14. Verifica se l’albero è un albero di ricerca binaria (BST)
#Traccia: Restituire True se l’albero rispetta la proprietà BST (per ogni nodo,
# valori a sinistra minori, valori a destra maggiori).

    def verificaBinarioRicerca(self):
        return self._verificaBinarioRicercaDa(self.root)
    
    def _verificaBinarioRicercaDa(self,node):
        if node is None:
            return True
        
        if node.Rson is None and node.Lson is None:
            return True
        
        if node.Rson is None or node.Lson is None:
            return self._verificaBinarioRicercaDa(node.Lson) and self._verificaBinarioRicercaDa(node.Rson)

        if node.value > self._verificaBinarioRicercaDa(node.Lson):
            return True
        
        if node.value < self._verificaBinarioRicercaDa(node.Lson):
            return True
        
#1) ContaNodiPosNeg
#Scrivi un metodo ricorsivo che, dato un albero binario di nodi contenenti valori interi, 
#restituisca True se il numero di nodi con valore strettamente positivo è uguale al numero di 
#nodi con valore strettamente negativo.
#Altrimenti restituisce False.

    def contaNodiPosNeg(self):
        nodiPos = self._contaNodiPos(self.root)
        nodiNeg = self._contaNodiNeg(self.root)
        return nodiPos == nodiNeg
    def _contaNodiPos(self,node):
        if node is None:
            return 0
        
        if node.value > 0:
            return 1 + self._contaNodiPos(node.Rson) + self._contaNodiPos(node.Lson)
        else:
            return self._contaNodiPos(node.Rson) + self._contaNodiPos(node.Lson)
        
    def _contaNodiNeg(self,node):
        if node is None:
            return 0
        
        if node.value < 0:
            return 1 + self._contaNodiNeg(node.Rson) + self._contaNodiNeg(node.Lson)
        else:
            return self._contaNodiNeg(node.Rson) + self._contaNodiNeg(node.Lson)
        
#SommaValoriPariDispari
#Scrivi un metodo ricorsivo che calcola e ritorna la differenza tra la somma dei valori 
#dei nodi con valori pari e la somma dei valori dei nodi con valori dispari.

    def sommaValoriPariDispari(self):
        sommaPari = self._sommaNodiPari(self.root)
        sommaDispari = self._sommaNodiDispari(self.root)
        return sommaPari - sommaDispari

    def _sommaNodiPari(self,node):
        if node is None:
            return 0
        if node.value % 2 == 0:
            return node.value + self._sommaNodiPari(node.Rson)+self._sommaNodiPari(node.Lson)
        else:
            return self._sommaNodiPari(node.Rson)+self._sommaNodiPari(node.Lson)
        
    def _sommaNodiDispari(self,node):
        if node is None:
            return 0
    
        if node.value % 2 != 0:
            return node.value + self._sommaNodiDispari(node.Rson)+self._sommaNodiDispari(node.Lson)
        else:
            return self._sommaNodiDispari(node.Rson)+self._sommaNodiDispari(node.Lson)
        
#VerificaNodiZeroNelCammino
#Dato un albero binario, scrivi un metodo che verifica se esiste almeno un cammino 
#dalla radice a una foglia in cui è presente almeno un nodo con valore zero.

    def VerificaNodiZeroNelCammino(self):
        return self._verificaZeriDa(self.root,False)
    
    def _verificaZeriDa(self,node,trovato):
        if node is None:
            return False
        
        if node.value == 0:
            trovato = True

        if node.Lson is None and node.Rson is None:
            return trovato
        
       
        
        return (self._verificaZeriDa(node.Rson,trovato) or self._verificaZeriDa(node.Lson,trovato))


#ContaFoglieConValore
#Scrivi un metodo ricorsivo che conti quante foglie dell'albero hanno un 
# valore maggiore di una soglia k passata come parametro.

    def contaFoglieConValore(self,k):
        return self._contaFoglieConValoreDa(self.root,k)
    
    def _contaFoglieConValoreDa(self,node,k):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            if node.value > k:
                return 1
            else:
                return 0
            
        foglieDx = self._contaFoglieConValoreDa(node.Rson,k)
        foglieSX = self._contaFoglieConValoreDa(node.Lson,k)

        return foglieDx + foglieSX
    
#5) VerificaUgualiFigli
#Scrivi un metodo ricorsivo che verifica se per ogni nodo interno i valori dei suoi figli sono uguali.
#Restituisci True se la condizione è verificata in tutto l'albero, False altrimenti.

    def verificaUgualiFigli(self):
        return self._verificaUgualiFigliDa(self.root)
    
    def _verificaUgualiFigliDa(self,node):
        if node is None:
            return True
        
        if node.Rson is None and node.Lson is None:
            return True
        
        if node.Rson is None or node.Lson is None:
            return False
        
        if node.Lson.value != node.Rson.value:
            return False
        
        verDx = self._verificaUgualiFigliDa(node.Rson)
        verSX = self._verificaUgualiFigliDa(node.Lson)

        return verDx and verSX
        

#3) Somma dei valori dei nodi foglia
#Scrivi un metodo che sommi tutti i valori che si trovano in foglia.

    def sommaNodiFoglia(self):
        return self._sommaNodiFogliaDa(self.root)

    def _sommaNodiFogliaDa(self,node) :
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return node.value
        
        valSx = self._sommaNodiFogliaDa(node.Lson)
        valDx = self._sommaNodiFogliaDa(node.Rson)

        return valDx + valSx
    
#1) Conta nodi con valore compreso in un intervallo [a, b]
#Scrivi un metodo ricorsivo che conti quanti nodi hanno valore >= a e <= b.
    def contaNodiTra(self,a,b):
        return self._contaNodiTraDa(self.root,a,b)
    
    def _contaNodiTraDa(self,node,a,b):
        if node is None:
            return 0
        
        if node.value >=a and node.value <= b:
            return 1 + self._contaNodiTraDa(node.Rson,a,b) + self._contaNodiTraDa(node.Lson,a,b)
        else:
            return self._contaNodiTraDa(node.Rson,a,b) + self._contaNodiTraDa(node.Lson,a,b)
        

#Conta il numero di nodi con solo un figlio
#Scrivi un metodo ricorsivo che restituisce quanti nodi hanno esattamente un solo figlio 
#(cioè hanno solo il figlio sinistro o solo il destro).

    def verificaNodiUnicoFiglio(self):
        return self._verificaNodiUnicoFiglioDa(self.root)
    
    def _verificaNodiUnicoFiglioDa(self,node):
        if node is None:
            return 0
        if (node.Lson is not None and node.Rson is None) or (node.Lson is None and node.Rson is not None):
            return 1 + self._verificaNodiUnicoFiglioDa(node.Lson) + self._verificaNodiUnicoFiglioDa(node.Rson)
        else:
            return self._verificaNodiUnicoFiglioDa(node.Lson) + self._verificaNodiUnicoFiglioDa(node.Rson)
        
#Verifica se esiste un percorso radice-foglia con somma dati valore target
#Scrivi una funzione che verifichi se esiste almeno un percorso dalla radice a una foglia 
#la cui somma dei valori dei nodi è pari a un valore target dato.

    def verificaPercorsoSomma(self,target):
        return self._verificaPercorsoSommaDa(self.root,target)
    
    def _verificaPercorsoSommaDa(self,node,target):
        if node is None:
            return False
        
        if node.Lson is None and node.Rson is None:
            if target - node.value == 0:
                return True
        
        return (self._verificaPercorsoSommaDa(node.Rson,target - node.value) or self._verificaPercorsoSommaDa(node.Lson,target - node.value) )


    def sommaMaxPercorso(self):
        return self._sommaMaxPercorso(self.root)
    
    def _sommaMaxPercorso(self,node):
        if node is None :
            return float("-inf")
        
        if node.Rson is None and node.Lson is None:
            return node.value
        
        maxL = node.value + self._sommaMaxPercorso(node.Lson)
        maxR = node.value + self._sommaMaxPercorso(node.Rson)
        
        return max(maxL,maxR)
    

    def contaPercorsiSomma(self, target):
        return self._contaPercorsiSommaDa(self.root,target)
    
    def _contaPercorsiSommaDa(self,node,target,somma_parz):
        if node is None:
            return 0
        somma_parz += node.value

        if node.Rson is None and node.Lson is None:
            if somma_parz == target:
                return 1
            
        return self._contaPercorsiSommaDa(node.Rson,target,somma_parz) + self._contaPercorsiSommaDa(node.Lson,target,somma_parz)



############# ESERCIZIO COMPLESSO #######################
#Esercizio:
#Trova se esiste un percorso radice-foglia in cui i valori dei nodi formano una sequenza di valori 
# con differenza costante k tra nodi consecutivi.
# Dettagli:
# Dato un intero k, devi verificare se esiste almeno un percorso dalla radice a una foglia in cui, 
# per ogni coppia di nodi consecutivi nel percorso, la differenza tra il valore del nodo figlio e quello 
# del nodo padre è esattamente k.
# Ad esempio, se il percorso è [5, 7, 9] e k = 2, allora il percorso è valido perché 7-5=2 e 9-7=2.
#Se il percorso è [5, 8, 10] e k=2, non è valido perché 8-5=3 ≠ 2.


    def verifica(self,k):
        if self.len == 0:
            raise Exception("albero vuoto")
        return  self._verificaDa(self.root,k)

    def _verificaDa(self,node,k):
        if node is None:
            return True
        costante = True
    
        if (node.Rson.value - node.value != k and node.Rson is not None ) or (node.Lson.value - node.value != k and node.Rson is not None):
            costante = False
        
        if node.Rson is None and node.Lson is None:
            return costante
        else:   
            return (self._verificaDa(node.Rson,k) or self._verificaDa(node.Lson,k))
        
#Esercizio 1
#Implementare un metodo altezzaMinima(self, soglia) che restituisce 
# True se l'altezza minima dell'albero (il percorso più breve dalla radice a una foglia) 
#è maggiore della soglia specificata. Se l'albero è vuoto, restituire False.

    def altezzaMinima(self,soglia):
        if self.root is None:
            return False
        altezzaMin = self._calcolaAltezzaMinDa(self.root,0)
        return altezzaMin > soglia
    
    def _calcolaAltezzaMinDa(self,node,liv_att):
        if node is None:
            return float('inf')
        
        if node.Rson is None and node.Lson is None:
            return liv_att 
        return min(self._calcolaAltezzaMinDa(node.Rson,liv_att +1),self._calcolaAltezzaMinDa(node.Lson,liv_att +1))


#Esercizio 2
#Implementare un metodo sottoinsieme(self, b) che restituisce True 
# se tutti i nodi dell'albero b sono contenuti nell'albero self. In altre parole, 
# verifica se b è un sottoinsieme di self in termini di valori contenuti nei nodi.

    def sottoinsieme(self,b):
        if self.root is None and b.root is None:
            return True
        return self._calcSottoInsiemeDa(b.root,self.root)
    
    def _calcSottoInsieme(self,nodeB,nodeSelf):
        if nodeSelf is None or nodeB is None:
            return False
        
        if nodeB.value == nodeSelf.value:
            return True
        
        verSx= self._calcSottoInsieme(nodeB.Rson ,nodeSelf.Lson) and self._calcSottoInsieme(nodeB.Lson ,nodeSelf.Lson)
        verDx= self._calcSottoInsieme(nodeB.Rson ,nodeSelf.Rson) and self._calcSottoInsieme(nodeB.Lson ,nodeSelf.Rson)

        return verSx and verDx
    

#Esercizio 3
#Implementare un metodo predecessoreSuccessore(self, valore) che restituisce una tupla 
#contenente il predecessore e il successore di un dato valore nell'albero binario di ricerca. 
#Se il predecessore o il successore non esistono, restituire None per quella posizione.

    def predecessoreSuccessore(self,valore):
        return self._calcPS(self.root,valore)
    

    def _calcPS(self,node,valore):
        if node is None:
            return None
        
        if node.value == valore:
            pred = self._trovaPredecessore(node.Lson)
            # ora ho creato la funzione che partendo dal sotto albero sinistro ne calcola il massimo valore più piccolo di node.value
            succ = self._trovaSuccessore(node.Rson)
            #stessa cosa per successore
            return pred,succ
        
        if valore > node.value:
            return self._calcPS(node.Rson,valore)
        else:
            return self._calcPS(node.Lson,valore)
        
    def _trovaSuccessore(self, node):
       if node is None:
           return float('inf')
       
       return min(node.value,self._trovaSuccessore(node.Lson),self._trovaSuccessore(node.Rson))

    def _trovaPredecessore(self,node):
        if node is None:
            return float('-inf')
        
        return max(node.value,self._trovaPredecessore(node.Lson),self._trovaPredecessore(node.Rson))
    

#Implementare un metodo verificaTreNodi(self) che restituisce True se esistono almeno 
# tre nodi che soddisfano la seguente proprietà: il prodotto tra l'informazione 
# contenuta nel nodo e la sua profondità è maggiore di 10.

    def verificaTreNodi(self):
        if self.len < 3:
            raise Exception("lista troppo corta o vuota")
        cont =  self._verificaTreNodiDa(self.root,0)
        return cont >= 3
    
    def _verificaTreNodiDa(self,node,liv_att,cont):
        if node is None:
            return 0
        
        if node.value * liv_att > 10:
            return 1 + self._verificaTreNodiDa(node.Rson,liv_att + 1) +  self._verificaTreNodiDa(node.Lson,liv_att + 1)
        else:
            return self._verificaTreNodiDa(node.Rson,liv_att + 1) +  self._verificaTreNodiDa(node.Lson,liv_att + 1)
        

#Implementare un metodo bilanciamentoPesato(self) che calcola la differenza tra il peso del 
# sottoalbero sinistro e quello destro, dove il peso di un sottoalbero è la somma di tutti 
#i valori moltiplicati per il loro livello. Restituire la differenza assoluta tra i due pesi.

    def bilanciamentoPesato(self):
        if self.root is None:
            return 0
        pesoSX = self._calcBilPesato(self.root.Lson,0)
        pesoDX = self._calcBilPesato(self.root.Rson,0)
        return abs(pesoDX-pesoSX)
    
    def _calcBilPesato(self,node,liv_att):
        if node is None:
            return 0
        peso = node.value*liv_att
        pesoSx = self._calcBilPesato(node.Lson,liv_att+1)
        pesoDx =self._calcBilPesato(node.Rson,liv_att+1)

        return peso+ pesoSx+pesoDx
    


#Implementare un metodo percorsoMassimo(self) che restituisce la somma massima ottenibile 
# seguendo un percorso dalla radice a una foglia qualsiasi dell'albero.

    def percorsoMassimo(self):
        if self.root is None:
            raise Exception("albero vuoto")
        return self._calcolaPercorsoMassimo(self.root)
    
    def _calcolaPercorsoMassimo(self,node):
        if node is None:
            return 0
        
        if  node.Lson is  None and node.Lson is  None:
            return node.value
        
        percorso_sin = self._calcolaPercorsoMassimo(node.Lson)
        percorso_des= self._calcolaPercorsoMassimo(node.Rson)

        return node.value + max(percorso_sin,percorso_des)
        

#Implementare un metodo verificaProprietaLivello(self, k) che restituisce True se tutti i
#  nodi che si trovano al livello k hanno valori positivi. Se non esistono nodi al livello k, 
# restituire False.

    def verificaProprietaLivello(self,k:int):
        verifica =  self._verificaDa(self.root,k,0)
        if verifica == -1:
            return False
        return verifica
    def _verificaDa(self,node,k,liv_att):
        if node is None:
            return True
        
        if liv_att == k:
            return node.value > 0
        else:
            return self._verificaDa(node.Rson,k,liv_att+1) and self._verificaDa(node.Lson,k,liv_att+1) 
        
#Implementare un metodo contaNodiFoglia(self, min_val, max_val) che conta quante 
#foglie dell'albero hanno valori compresi nell'intervallo [min_val, max_val] 
#(estremi inclusi).

    def contaNodiFoglia(self, min_val, max_val):
        return self._contaDa(self.root,min_val,max_val)
    
    def _contaDa(self,node,min_val,max_val):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            if node.value >= min_val and node.value <= max_val:
                return 1
            else:
                return 0
        
        contaSx =  self._contaDa(node.Lson,min_val,max_val)
        contaDx = self._contaDa(node.Rson,min_val,max_val)
        return contaDx+contaSx
    
#Implementare un metodo sommaProdotto(self) che calcola la somma di tutti i prodotti 
# tra ogni nodo e la sua profondità, ma solo per i nodi che hanno almeno un figlio. 
# I nodi foglia vengono ignorati.

    def sommaProdotto(self):
        return self._sommaProdottoDa(self.root,0)
    
    def _sommaProdottoDa(self,node,liv_att):
        if node is None:
            return 0
        if node.Rson is None and node.Lson is None:
            return 0
        
        sum = node.value *liv_att
        
        sumSx = self._sommaProdottoDa(node.Lson,liv_att+1)
        sumDx = self._sommaProdottoDa(node.Rson,liv_att+1)

        return sum +sumSx + sumDx
        
        
        
#Implementare un metodo bilanciamentoAlternato(self) che calcola la differenza 
# tra la somma dei valori ai livelli pari e la somma dei valori ai livelli dispari, 
# ma considerando solo i nodi che hanno esattamente un figlio.

    def bilanciamenoAlternativo(self):
        pari,dispari = self._calcolaDa(self.root,0,)
        return pari-dispari
    
    def _calcolaDa(self,node,liv_att):
        if node is None:
            return 0 ,0 
        if node.Rson is None and node.Lson is None:
            return 0,0
        
        sommapari = sommadispari = 0
        if (node.Rson is  None) != (node.Lson is None):
            if liv_att % 2 == 0:
                sommapari += node.value
            else:
                sommadispari += node.value


        sumPariDx, sumDispariDx = self._calcolaDa(node.Rson,liv_att + 1)
        sumPariSx, sumDispariSx = self._calcolaDa(node.Lson,liv_att + 1) 

        sommapari += sumPariDx+sumPariSx
        sommadispari += sumDispariDx+ sumDispariSx

        return sommapari,sommadispari



#Implementa un metodo altezzaNodo(self, valore) che, dato un valore contenuto in un nodo 
# dell'albero, restituisce la sua altezza (numero di nodi nel cammino più lungo da quel 
# nodo fino a una foglia). Se il nodo non esiste, restituisci -1.

    def altezzaNodo(self,valore):
        altezza = self._calcola(self.root,valore)
        return -1 if altezza == 0 else altezza
    def _calcola(self,node,valore):

        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return 0

        if node.value == valore:
            return self._calcolaProfNodo(node)
        else:
            return (self._calcola(node.Rson,valore) + self._calcola(node.Lson,valore))

    def _calcolaProfNodo(self,node):
        if node is None:
            return 0
        
        if node.Rson is None and node.Lson is None:
            return 0
        
        profDX= 1 + self._calcolaProfNodo(node.Rson) 
        profSx = 1+ self._calcolaProfNodo(node.Lson)

        return max(profDX,profSx)
        

        
#Conta i nodi in un intervallo
#Scrivi una funzione che restituisce quanti nodi hanno valori compresi tra low e high (inclusi) in un BST.  

    def contaNodiInIntervallo(self,a,b):
        return self._contaNodiDa(self.root,a,b)
    
    def _contaNodiDa(self,node,a,b):
        if node is None:
            return 0
        
        if node.value <= b and node.value >= a:
            return 1 + self._contaNodiDa(node.Rson,a,b)+ self._contaNodiDa(node.Lson,a,b)
        return self._contaNodiDa(node.Rson,a,b)+ self._contaNodiDa(node.Lson,a,b)


#Implementa una funzione listaInOrdine() che restituisce una lista ordinata crescente con 
# tutti i valori del BST.

    def listaInOrdine(self):
        l=[] 
        self._listaOrdinata(self.root,l)
        return l
    
    def _listaOrdinata(self,node,lista):
        if node is None:
            return 
        
        self._listaOrdinata(node.Lson,lista)
        lista.append(node.value)
        self._listaOrdinata(node.Rson,lista)


#Trova il nodo con valore più vicino a un dato k
    def trovaNodoVicini(self,k):
        max = self._trovaNodoDa(self.root,k,None)
        if max < k:
            return max
        
    def _trovaNodoDa(self,node,k,nodoVicino):
        if node is None:
            return nodoVicino
        
        if nodoVicino is None or abs(nodoVicino.value-k) > abs(node.value-k):
            nodoVicino = node.value

        if node.value > k:
            return self._trovaNodoDa(node.Lson,k,nodoVicino)
        if node.value < k:
            return self._trovaNodoDa(node.Rson,k,nodoVicino)
        else:
            return node.value

        
#Verifica se un valore k è il nodo con valore minimo nel suo sottoalbero
#Scrivi una funzione che, dato un nodo con valore k, verifichi se è il valore più piccolo a partire da lì.
        
    def verificaMinoreSottoalbero(self,k):
        minSottoAlbero = self._trovaMinSottoAlbero(self.root,k)
        if minSottoAlbero is not None and minSottoAlbero== k:
            return True
        else:
            return False
    
    def _trovaMinSottoAlbero(self,node,k):
        if node is None:
            return None
        
        if node.value == k:
            return self._checkminimo(node)
        else:
            return self._trovaMinSottoAlbero(node.Lson,k) or self._trovaMinSottoAlbero(node.Rson,k)

    def _checkminimo(self,node):
        if node is None:
            return float('inf')
        
        checkMinSx = self._checkminimo(node.Lson)
        checkMinDx = self._checkminimo(node.Rson)

        return min(node.value,checkMinSx,checkMinDx)
    
#Controlla se esiste un percorso con somma S
#Esiste almeno un percorso dalla radice a una foglia in cui la somma dei valori è esattamente S?
    
    def sommaPercorso(self,s):
        return self._sommaPercorsoDa(self.root,s)
    
    def _sommaPercorsoDa(self,node,s):
        if node is None:
            return 0
        
        s -= node.value

        if node.Rson is None and node.Lson is None:
            return s == 0
        else:
            return self._sommaPercorsoDa(node.Rson,s) or self._sommaPercorsoDa(node.Lson,s)

#5. Profondità massima e minima
#Scrivi due funzioni che calcolano:
#la profondità massima (cioè la lunghezza del percorso più lungo radice-foglia)
#la profondità minima (cioè il percorso più corto radice-foglia)

    def calcolaProf(self):
        profMax = self._calcolaProfMax(self._radice,0)
        profMin = self._calcolaProfMin(self._radice,0)
        #continuo del codice
    def _calcolaProfMax(self,nodo,prof_att):
        if nodo is None:
            return float('-inf')

        profSx=self._calcolaProfMax(nodo.figlio_sinistro,prof_att+1) 
        profDx=self._calcolaProfMax(nodo.figlio_destro,prof_att+1)

        if nodo.figlio_sinistro is None and nodo.figlio_destro is None:
            return prof_att
        else:
            return max(profSx,profDx)
        
    def _calcolaProfMin(self,nodo,prof_att):
        if nodo is None:
            return float('+inf')
        
        profSx = self._calcolaProfMin(nodo.figlio_sinistro,prof_att+1)
        profDx = self._calcolaProfMin(nodo.figlio_destro,prof_att +1)

        if nodo.figlio_sinistro is None and nodo.figlio_destro is None:
            return prof_att
        else:
            return min(profSx,profDx)
        
#4. Verifica presenza di valore solo su un lato
#Scrivi una funzione che verifica se un certo valore k si trova esclusivamente 
#nel sottoalbero sinistro oppure esclusivamente nel sottoalbero destro della radice.

    def verificaEsclusivaSottoalbero(self,k):
        if self._radice._info == k:
            return True
        checkSx = self._verificaAsinistra(self._radice.figlio_sinistro,k)
        checkDx = self._verificaAdestra(self._radice.figlio_destro,k)
        if checkSx == checkDx:
            return False #se tutte e due sono true vuol dire che k si trova in entrambi i sotto alberi quindi returna false
        return True
    def _verificaAsinistra(self,node,k):
        if node is None:
            return False
        if node.value==k:
            return True
        return self._verificaAsinistra(node.figlio_sinistro,k) or self._verificaAsinistra(node.figlio_destro,k)
    
    def _verificaAdestra(self,node,k):
        if node is None:
            return False
        if node.value==k:
            return True
        return self._verificaAdestra(node.figlio_sinistro,k) or self._verificaAdestra(node.figlio_destro,k)

    
#che restituisce la profondità (distanza dalla radice) del nodo con valore k. Se il nodo non è presente, restituisce -1.#
    def profonditaNodo(self, k):
        prof = self._calcProfNodoDa(self._radice,k,0)
        if prof is not False:
            return prof
        return -1
    def _calcProfNodoDa(self,node,k,liv_att):
        if node is None:
            return False
        
        if node._info == k:
            return liv_att
        else:
            return self._calcProfNodoDa(node.figlio_sinistro,k,liv_att +1 ) or self._calcProfNodoDa(node.figlio_destro,k,liv_att +1 )
        
#che restituisce il valore massimo tra tutte le foglie dell’albero.

    def fogliaValMax(self):
        return self._calcolaFogliaMaxDa(self._radice)
    
    def _calcolaFogliaMaxDa(self,node):
        if node is None:
            return float('-inf')
        
        valoreSinistra = self._calcolaFogliaMaxDa(node.figlio_sinistro)
        valoreDestra = self._calcolaFogliaMaxDa(node.figlio_destro)

        if node.figlio_sinistro is None and node.figlio_destro is None:
            return max(node.value, valoreDestra, valoreSinistra)
        else:
            return max(valoreDestra,valoreSinistra)


#che ritorna True se esiste un percorso dalla radice a una foglia in cui il prodotto dei valori dei nodi è esattamente p.

    def percorsoProdottoEsatto(self,p):
        return self._calcPercorso(self._radice,p,1)
    
    def _calcPercorso(self,node,p,prodotto_att):
        if node is None:
            return False
        
        prodotto_att *= node.value

        if node.figlio_sinistro is None and node.figlio_destro is None:
            if prodotto_att == p:
                return True
        return self._calcPercorso(node.figlio_sinistro,p,prodotto_att) or self._calcPercorso(node.figlio_destro,p,prodotto_att)

#Implementa un metodo esistePercorsoSomma(self, s) nella tua classe albero binario, che restituisce True 
# se esiste almeno un percorso dalla radice a una foglia il cui valore sommato è esattamente s, 
# False altrimenti.
#Vincoli:
#Il percorso deve partire dalla radice e terminare a una foglia (nodo senza figli).
#Puoi usare la ricorsione.
#Attenzione ai casi base: albero vuoto, somma negativa, somma 0, nodi con valore negativo.

    def esistePersorsoSomma(self,s):
        return self._sommaPercorsoDa(self._radice,s)
    
    def _sommaPercorsoDa(self,node,s):
        if node is None:
            return False
        
        s -= node.value
        if node.figlio_sinistro is None and node.figlio_destro is None:
            return s == 0
        
        return (self._sommaPercorsoDa(node.figlio_destro,s) or self._sommaPercorsoDa(node.figlio_sinistro,s))

    def contaNodiFoglia(self):
        return self._contaDA(self._radice)
    
    def _contaDA(self,node):
        if node is None:
            return 0
        if node.figlio_sinistro is None and node.figlio_destro is None:
            return 1
        
        return self._contaDA(node.figlio_destro) + self._contaDA(node.figlio_sinistro)
    

    def verifica(self):
        return self._verificaDa(self.root)
    
    def _verificaDa(self,node):
        if node is None:
            return False
        if node.figlio_sinistro is not None and node.figlio_destro is not None:
            if node.value % 2 ==0:
                if not self._verificaSx(node.figlio_sinistro):
                    return False
            else:
                if not self._verificaDx(node.figlio_destro):
                    return False
        
        return self._verificaDa(node.figlio_destro) and self._verificaDa(node.figlio_sinistro)
    
    def _verificaSx(self,node):
        if node is None:
            return False
        
        if node.value % 2 == 0:
            return True
        
        return self._verificaSx(node.figlio_destro) or self._verificaSx(node.figlio_sinistro)

    def _verificaDx(self,node):
        if node is None:
            return False
        
        if node.value % 2 != 0:
            return True
        
        return self._verificaDx(node.figlio_destro) or self._verificaDx(node.figlio_sinistro)
    
#🔸 2. Verifica se tutti i nodi con valore pari hanno almeno un figlio con valore dispari
    def verificaFiglioDispari(self):
        return self._verificaDa(self._radice)
    
    def _verificaDa(self,node):
        if node is None:
            return True
        if node.value %2 == 0:
            if not ((node.figlio_destro is not None and node.figlio_destro.value % 2 != 0) or (node.figlio_sinistro is not None and node.figlio_sinistro.value %2 != 0)) :
                return False
        return self._verificaDa(node.figlio_sinistro) and self._verificaDa(node.figlio_destro)
    
#5. Verifica se ogni valore dispari ha un antenato pari (non necessariamente il padre diretto)
#Per ogni nodo dispari, verifica che esista almeno un nodo antenato con valore pari.

    def antenatoPari(self):
        if self._radice.value % 2 == 0:
            return True #poichè la radice è antenato di tutti i nodi dell'albero
        return self._esisteAntenatoPari(self._radice,False)
    
    def _esisteAntenatoPari(self,node,antenatoPari):
        if node is None:
            return True
        
        if node.value % 2 == 0:
            scorriSX = self._esisteAntenatoPari(node.figlio_sinistro,True)
            scorriDX = self._esisteAntenatoPari(node.figlio_destro,True)
            
        if not( node.value %2 != 0 and antenatoPari):
            return False

        else:
            return scorriSX and scorriDX          

    def ricercaVal(self,valore):
        if self._radice is None:
            raise Exception("albero vuoto")
        if self._radice._info == valore:
            return True
        return self._cercaValDa(self._radice,valore)
    
    def _cercaValDa(self,node,val):
        if node is None:
            return False
        
        if node._info < val and node.figlio_destro is not None:
            return self._cercaValDa(node.figlio_destro,val)
        elif node._info> val and node.figlio_sinistro is not None:
            return self._cercaValDa(node.figlio_sinistro,val)
        elif node._info == val:
            return True
        else:
            return False
        
    ###funzione che conta i nodi ad una cerca prof

    def contaNodiProf(self,k):
        if self._radice is None:
            raise Exception("albero vuoto")
        if k == 0 and self._radice is not None:
            return 1 #l'unico nodo a prof=0 è la radice
        return self._contaNodiProfDa(self._radice,k,0)

    def _contaNodiProfDa(self,node,k,liv_att):
        if node is None:
            return 0

        if liv_att == k and node is not None:
            return 1
        
        contaDx = self._contaNodiProfDa(node.figlio_destro,k,liv_att+1)
        contasx = self._contaNodiProfDa(node.figlio_sinistro,k,liv_att+1)

        return contaDx + contasx
    
    #### trova il k-esimo valore più piccolo
    def is_valid_BST(self):
        if self._radice is None:
            return False
        return self._checkValid(self._radice,float('-inf'),float('inf'))
    
    def _checkValid(self,node,min_val,max_val):
        if node is None:
            return True
        
        if node.figlio_destro is None and node.figlio_sinistro is None:
            return True

        if not (node._info > min_val and node._info<max_val):
            return False
        return (self._checkValid(node.figlio_sinistro,float('-inf'),node._info) and self._checkValid(node.figlio_sinistro,node._info,float('inf')))

