from ll import Linkedlist
class Utente:
    def __init__(self,cf,citta):
        self.cf = cf
        self.citta= citta
    
    def getCf(self):
        return self.cf

    def getCitta(self):
        return self.citta
    
class Tweet:
    def __init__(self,codice,codiceUtente,data,citta,tag:Linkedlist):
        self.codice = codice 
        self.codiceUtente = codiceUtente
        self.data = data
        self.citta = citta
        self.tag = tag

    def getCodice(self):
        return self.codice
    def getCodiceUtente(self):
        return self.codiceUtente
    def getData(self):
        return self.data
    def getCitta(self):
        return self.citta
    def getTag(self):
        return self.tag
    
class Sistema:
    def __init__(self,listaUtenti:Linkedlist,listaTweet:Linkedlist):
        self.listaUtenti = listaUtenti
        self.listaTweet = listaTweet

    def _getTagToCF(self,cf):
        for tweet in self.listaTweet:
            if tweet.getCodiceUtente == cf:
                return tweet.getTag()
            
    def _getUtentiPiùTweet(self):
        lista = []
        cont = 0
        for utente in self.listaUtenti:
            for tweet in self.listaTweet:
                if utente.getCf() == tweet.getCodiceUtente():
                    cont += 1
                    pass
            if cont >= 2:
                lista.append(utente)
        return lista
    
    def _createDict(self):
        d = {}
        listaUsers = self._getUtentiPiùTweet()
        for u in listaUsers:
            cf = u.getCf()
            if not cf in d:
                d[cf]=[]
            d[cf].append(self._getTagToCF(cf))
        
    def funCheNonSoFarFunzionare(self):
        ut = Linkedlist()
        d = self._createDict()
        keys = d.keys()
        for utente in self.listaUtenti:
            if utente.getCf in keys:
                values=d[utente.getCf].values()
                for i in range(0,len(values)-1):
                    it1=iter(values[i])
                    it2 = iter(values[i+1])
                    while not it1.finito():
                        val1 = next(it1)
                        while not it2.finito():
                            val2 = next(it2)
                            if val1 == val2:
                                pass
                    ut._aggiungiCoda(utente.getCf)
        return ut

    #metodo 3
    def TagOfTheDay(self,data):
        
        d = {}
        for tweet in self.listaTweet:
            if tweet.getData()==data:
                for tags in tweet.getTag():
                    if not tags in d:
                        d[tags]=0
                    d[tags]+=1
        value = list(d.values())
        max = max(value)
        items = d.items()
        for it in items:
            if it[1]==max:
                return it[0]

    def _listAutori(self,autore1,autore2):
        ll=Linkedlist()
        for pub in self.listaPubblicazioni:
            autori = pub.getAutori() #questo metodo ritorna una linkedlist con gli autori della pubb
            if autore1 in autori and autore2 in autori:
                ll._aggiungiCoda(pub)

        return ll
    
    def coautori(self,autore1,autore2):
        out = Linkedlist()
        dates=[]
        pubb = self._listAutori(autore1,autore2)
        it=iter(pubb)
        while not it.finito():
            dates.append(next(it).getData())
        dates=sorted(dates)
        for i in range (0,len(pubb)):
            for pub in pubb:
                if dates[i]==pub.getData():
                    out.AggiungiInCoda(pub)
        return out