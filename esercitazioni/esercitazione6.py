
class Abbonamento:
    def __init__(self,cod,mese,settimana):
        self.cod = cod
        ##sett è definita come una matrice booleana 12 x 4
        self.mese = mese
        self.settimana = settimana

class Tesserato:
    def __init__(self,nome,cognome,codFisc,codTessera,scadenza,abbonamenti : list[Abbonamento]):
        self.nome= nome
        self.cognome = cognome
        self.codFisc = codFisc
        self.codTessera = codTessera
        self.scadenza = scadenza
        self.abbonamenti = abbonamenti

class Servizio:
    def __init__(self,codice,postiDisp,turno,costoSett):
        self.codice = codice 
        self.postiDisp = postiDisp
        self.turno = turno
        self.costoSett = costoSett
    
    

class CentroSportivo:
    def __init__(self,tesserati : list[Tesserato],servizi :list[Servizio]):
        if self._uniqueTes():
            self.tesserati = tesserati
        else:
            raise Exception
        
        if self._uniqueSer():
            self.servizi = servizi
        else:
            raise Exception
    
    def _uniqueTes(self,codFisc):
        for item in self.tesserati:
            if item.codFisc == codFisc:
                return True
        return False
    
    def _uniqueSer(self,cod):
        for item in self.servizi:
            if item.codice == cod:
                return True
        return False

    ###implementazione metodi della classe###
    def _verificaPresenza(self,codice_fiscale):
        for item in  self.tesserati:
            if item.codFisc == codice_fiscale:
                return True
        return False
    
    def _verificaPostoServizio(self,cod):
        for item in self.servizi:
            if item.codice == cod:
                if item.postiDisp >=1 :
                    return True
        return False
    
    def aggiorna(self,codice_fiscale,cod_servizio,mese,settimane):
        if self._verificaPresenza(codice_fiscale) and self._verificaPostoServizio(cod_servizio):
            NewAbb = Abbonamento(cod_servizio,mese,settimane)
            for item in self.tesserati:
                if item.codFisc == codice_fiscale:
                    item.abbonamenti.append(NewAbb)
            for item in self.servizi:
                if item.codice == cod_servizio:
                    item.postiDisp -=1

    def _ordinaPerPrezzo(self,turns):
        for i in range(0, len(turns)):
            for j in range(0,len(turns)-i-1):
                if turns[j+1].costoSett < turns[j].costoSett:
                    temp=turns[j]
                    turns[j]=turns[j+1]
                    turns[j+1]=temp
        return turns


    def servizi_ordinati(self):
        senior = []
        advanced = []
        junior=[]
        for item in self.servizi:
            if item.turno == "senior":
                senior.append(item)
            elif item.turno == "advanced":
                advanced.append(item)
            else:
                junior.append(item)

        senior = self._ordinaPerPrezzo(senior)
        advanced = self._ordinaPerPrezzo(advanced)
        junior = self._ordinaPerPrezzo(junior)

        return senior + advanced + junior
    
    def _getCostoByCod(self,cod):
        for item in self.servizi:
            if cod == item.cod:
                return item.costoSett
            
    def report_iscritti(self,mese):
        ret = []
        for item in self.tesserati:
            for abb in item.abbonamenti:
                if abb.mese == mese:
                    input=[]
                    input.append(item.codTessera)
                    input.append(abb.sett * self._getCostoByCod(abb.cod))
                    ret.append[input]
        return ret
            

            
        

    
