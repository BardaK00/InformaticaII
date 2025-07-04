###esercizio 1
from ll import Linkedlist,Iteratore
from Prenotazione import Prenotazione
from Cliente import Cliente

class Sistema:
    def __init__(self,listaClienti,listaPrenotazioni):
        self.listaClienti = listaClienti
        self.listaPrenotazioni = listaPrenotazioni
    ##inizio primo metodo
    def selezione_cliente(self,codice_pren):
        for prenotazione in self.listaPrenotazioni:
            if prenotazione.get_codice()== codice_pren:
                clienti = prenotazione.get_clienti()
                it = iter(clienti)
                cliente = next(it)
                if len(clienti) == 1 and self._checkS(cliente):
                    return cliente
    def _checkS(self,nome_c):
        for c in self.listaClienti:
            if c.get_nome()== nome_c:
                clienteScelto = c
                break
        listaServPref = clienteScelto.get_servizi_preferiti()
        for cliente in self.listaClienti:
            if cliente == clienteScelto:
                continue
            listaser = cliente.get_servizi_preferiti()
            for servizi in listaServPref:
                it = iter(listaser)
                while not it.finito():
                    if servizi == next(it):
                        return False
        return True
    ## fine primo metodo

    ##inizio secondo metodo
    def _createdic(self,d):
        diz = {}
        for p in self.listaPrenotazioni:
            if p.get_data() > d:
                servizi = p.get_servizi_prenotati()
                for s in servizi:
                    if not s in diz:
                        diz[s]=0
                    diz[s]+=1
        return diz
    
    def servizio_frequente(self,d):
        diz = self._createdic(d)
        max = max(diz.values())
        items = diz.items()
        for it in items:
            if it[1] == max:
                return it[0]
            
    ##fine secondo metodo

    ##inizio terzo metodo
    def servizi_essenziali(self,nome_c):
        ll = Linkedlist()
        for c in self.listaClienti:
            if c.get_nome() == nome_c:
                servizi = c.get_servizi_preferiti()
                break
        tutte = True
        for s in servizi:
            for p in self.listaPrenotazioni:
                clienti = p.get_clienti()
                it = iter(clienti)
                while not it.finito():
                    if nome_c == next(it):
                        serviziPren = p.get_servizi_prenotati()
                        its = iter(serviziPren)
                        while not its.finito():
                            if s == next(it):
                                contenuto = True
                                break
                            else:
                                contenuto = False
                if not contenuto:
                    tutte=False
            if tutte:
                ll.aggiungiInCoda(s)
        return ll
    
    ##fine terzo metodo

    ##esercizio 2 ricorsione linkedlist
    def verifica(self):
        a,b= self._verificaDa(self.testa)
        if a==b:
            return True
        return False
    
    def _verificaDa(self,node):
        if node is None:
            return 0 ,0 
        if node.value == 0:
            return 0, 0
        
        if node.value > 0:
            a = 1+self._verificaDa(node.succ)
        if node.value < 0:
            b = 1+self._verificaDa(node.succ)

        return a ,b