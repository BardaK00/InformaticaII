import copy
import ll

class Fattura:
    def __init__(self, id : int, cliente : str, data : int, prodotti : list[str], quantita : list[int]):
        self.id = id
        self.cliente = cliente
        self.data = data
        self.prodotti = prodotti
        self.quantita = quantita

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{id}, {self.cliente}, {self.data}, {self.prodotti}, {self.quantita}"

    def getId(self):
        return self.id
    def getCliente(self):
        return self.cliente
    def getData(self):
        return self.data
    def getProdotti(self):
        return copy.deepcopy(self.prodotti)
    def getQuantita(self):
        return copy.deepcopy(self.quantita)


class Prodotto:
    def __init__(self, nome : str, marca : str, prezzo : float):
        self.nome = nome
        self.marca = marca
        self.prezzo = prezzo
    def __eq__(self, other):
        return self.nome == other.nome and self.marca == other.marca
    def __str__(self):
        return f"{self.nome} {self.marca} {self.prezzo}"

    def getNome(self):
        return self.nome
    def getMarca(self):
        return self.marca
    def getPrezzo(self):
        return self.prezzo
    
class Sistema:
    def __init__(self,fatture :LinkedList ,prodotti:linkedList):
        self.prodotti = prodotti
        self.fatture = fatture

    def numeroEsemplariMarca(self,m : str):
        cont = 0
        iterFatture = iter(self.fatture)
        
        while not iterFatture.finito():
            #prende la fattura
            fattura = next(iterFatture)

            #prodotti e iteratore
            listaProd = fattura.getProdotti()
            iterProd = iter(listaProd)

            #estrae le quantità
            listaquant = fattura.getQuantita()
            iterQuant = iter(listaquant)

            while not iterProd.finito():
                prodCorr = next(iterProd)
                quantCorr = next(iterQuant)
                if prodCorr.getMarca() == m:
                    cont += quantCorr
        return cont
    def _marcheAquistateCliente(self,nome_cliente):
        ret = linkedList()
        iterFatture = iter(self.fatture)
        while not iterFatture.finito():
            fattura = next(iterFatture)
            if nome_cliente == iterFatture.getCliente():
                listaProd = fattura.getProdotti()
                iterProd = iter(listaProd)
                while not iterProd.finito():
                    prodCorr=next(iterProd)
                    ret.AggiungiInCoda(prodCorr.getMarca())
        return ret

    def marcaInComune(self,nome_cliente):
        ret = linkedList()
        iterFatture = iter(self.fatture)
        lista_marche=self._marcheAquistateCliente(nome_cliente)
        
        while not iterFatture.finito():
            fattura=next(iterFatture)
            listaProd = fattura.getProdotti()
            iterProd = iter(listaProd)

            while not iterProd.finito():
                prodotto = next(iterProd)
                iterlista = iter(lista_marche)

                while not iterlista.finito():
                    marca = next(iterlista)
                    if prodotto.getMarca() == marca:
                        ret.AggiungiInCoda(fattura.getCliente())
        return ret
    

    







            
