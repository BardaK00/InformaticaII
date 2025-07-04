from ll import Linkedlist,Iteratore
class Sistema:
    def __init__(self,lista_studenti:Linkedlist,lista_corsi:Linkedlist):
        self.lista_studenti = lista_studenti
        self.lista_corsi = lista_corsi

    def promossi_in_tutti(self,soglia):
        ll = Linkedlist()
        for studente in self.lista_studenti:
            matricola = studente.get_matricola()
            corsiFatti = studente.get_corsi()
            superatiTutti = True
            for corso in corsiFatti:
                corsoSuperato=True
                valutazioni = corso.get_valutazioni()
                for val in valutazioni:
                    if val[0] == matricola and val[1] < soglia:
                        corsoSuperato = False
                        break
                if not corsoSuperato:
                    superatiTutti = False
                    break
            if superatiTutti:
                ll._aggiungiCoda(studente.get_nome())
        return ll
    
    def _calcolaMediaCorso(self,c):
        sum = 0
        valutazioni = c.get_valutazioni()
        len = len(valutazioni) #fattibile perche linkedlist contiene __len__
        it = iter(valutazioni)
        while not it.finito():
            tupla = next(it)
            sum += tupla[1]
        
        return sum / len
    
    def corso_con_media_massima(self):
        d = {}
        it = iter(self.lista_corsi)
        while not it.finito():
            corso = next(it)
            d[corso]=self._calcolaMediaCorso(corso)
        maxValue = max(d.values())
        items = d.items()

        for item in items:
            if item[1] == maxValue:
                return item[0]
            
    def _getCorsiDaNonAvereInComune(self,codice_corso):
        for corso in self.lista_corsi:
            if corso.get_codice() == codice_corso:
                valutazioni = corso.get_valutazioni()
                break
        listaMatricole = []
        it = iter(valutazioni)
        while not it.finito():
            val = next(it)
            listaMatricole.append(val[0]) #prende tutte le matricole che hanno frequentato il corso con codice_corso
        
        listaCorsiDaNonAvereInComune=[]
        for matricola in listaMatricole:
            for studente in self.lista_studenti:
                if matricola == studente.get_matricola():
                    listaCorsiDaNonAvereInComune.append(studente.get_corsi())

        return listaCorsiDaNonAvereInComune
    #listaCorsiDaNonAvereInComune avrà struttura [ll1,ll2,ll3,ll4] con ll una linkedlist

    def studenti_non_comuni(self,codice_corso):
        ll = Linkedlist()
        corsiNonComuni = self._getCorsiDaNonAvereInComune(codice_corso)
        
        for s in self.lista_studenti:
            aggiungi = True
            corsoS = s.get_corsi()
            it = iter(corsoS)
            trovato = True
            for i in range(0,len(corsiNonComuni)):
                itCNC = iter(corsiNonComuni[i])
                corsoDaControllare = next(it)
                while not itCNC.finito():
                    if corsoDaControllare == next(itCNC):
                        trovato=False
                        break
                if not trovato:
                    aggiungi = False
                    break
            if aggiungi :
                ll._aggiungiCoda(s.get_nome())

        return ll
            
                    