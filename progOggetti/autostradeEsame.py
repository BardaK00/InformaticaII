class Citta:
    citta_db=[]
    def __init__(self,nome,provincia,regione):
        if self._unique(Citta.citta_db,nome,provincia):
            raise Exception( "la città esista già, non è stata aggiunta")
        else:
            self.nome = nome
            self.provincia = provincia
            self.regione = regione
        
        Citta.citta_db.append(self)

    def _getCittàPerNome(self,nome):
        if nome == self.Nome:
            return self
    
    def _unique(self,db,nome,provincia):
        for citta in db:
            if citta.nome == nome and citta.provincia == provincia :
                return True
        return False
    
class Tratta:
    tratta_db=[]
    def __init__(self,cod,nome,citta_partenza,citta_arrivo,distanza):
        if self._unique(Tratta.tratta_db,cod):
            raise Exception("la tratta con codice:"+cod+" esiste già nel database")
        else:
            self.cod = cod
            self.nome = nome
            self.citta_partenza = Citta._getCittàPerNome(citta_partenza)
            self.citta_arrivo = Citta._getCittàPerNome(citta_arrivo)
            self.distanza = distanza
        Tratta.tratta_db.append(self)

    def _unique(self,db,cod):
        for tratta in db:
            if tratta.cod == cod:
                return True
        return False
    
    def _getMaxD(self,db):
        max = db[0].distanza
        for tratte in db:
            if tratte.distanza > max:
                max = tratte.distanza
        return max


class Autoveicolo:
    auto_db = []
    def __init__(self,targa,marca,cilindrata):
        if self._unique(Autoveicolo.auto_db,targa):
            raise Exception( "autoveicolo con targa:"+targa+" già presente nel database")
        else:
            self.targa = targa
            self.marca = marca
            self.cilindrata = cilindrata
        Autoveicolo.auto_db.append(self)

    def _unique(self,db,targa):
        for car in db:
            if car.targa == targa:
                return True
        return False
    
    def __repr__(self):
        return "l'autoveicolo è così composto:\ntarga:"+str(self.targa)+"\nmarca:"+self.marca+"\ncilindata:"+str(self.cilindrata)
    
class Percorrenza:
    perc_db = []
    def __init__(self,tratta,autoveicolo,data):
        if isinstance(tratta,Tratta):
            raise Exception("la tratta inserita non fa parte del db")
        if isinstance(autoveicolo,Autoveicolo):
            raise Exception ("l'auto inserita non fa parte del db ")
        else:
            self.tratta = tratta
            self.autoveicolo = autoveicolo
            self.data = data
        Percorrenza.perc_db.append(self)


class GestioneReteAS:
    def __init__(self):
        self.tratte = Tratta.tratta_db
        self.autoveicoli = Autoveicolo.auto_db
        self.citta = Citta.citta_db
        self.percorrenze= Percorrenza.perc_db

    def accessi(self,c):
        cont = 0
        if isinstance(c,Citta):
            for percorrenze in self.percorrenze:
                if percorrenze.tratta.citta_arrivo == c:
                    cont+=1
            return cont
        else:
            raise Exception("la città inserita non esiste nel database o non è una città")
        
    def trova_autoveicoli(self,x):
        autoveicoli = []
        for percorrenze in self.percorrenze:
            if percorrenze.tratta.distanza<x:
                autoveicoli.append(percorrenze.tratta.autoveicolo)
        return autoveicoli
    
    def trova_auto_frequente(self,d1,d2):
        auto= None
        maxd=Tratta._getMaxD(self.tratte)
        for percorrenze in self.percorrenze:
            if d1 <=percorrenze.data <= d2:
                if percorrenze.tratta.distanza == maxd:
                    auto= percorrenze.autoveicolo
        return auto