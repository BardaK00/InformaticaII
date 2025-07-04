##auto presenti in una concessionaria

class Automobile:
    auto_db=[]
    def __init__(self,modello,marca,casaProd,cilindrata,prezzo,numTelaio):
        self.modello = modello
        self.marca = marca
        self.casaProd=casaProd
        self.cilindrata=cilindrata
        self.prezzo = prezzo

        ##controllo unicità del numero di telaio
        if self._unique(numTelaio):
            self.numTelaio = numTelaio
        
        
    def __str__(self):
        return "modello:"+self.modello+"\n"+"marca:"+self.marca+"\n"+"Casa Produttrice:"+self.casaProd+"\n"+"Cilindrata:"+self.cilindrata+"\n"+"Prezzo:"+self.prezzo+"\n"+"Numero di telaio:"+str(self.numTelaio)

    def _unique(self,telaio):
        for auto in Automobile.auto_db:
            if auto.numTelaio == telaio:
                raise Exception("Auto con numero di telaio:"+str(telaio)+" già presente in magazzino")
        return True

class Concessionaria:
    def __init__(self):
        self.magazzino=Automobile.auto_db
    
    def aggiungiInMagazzino(self,modello,marca,casaProd,cilindrata,prezzo,numTelaio):
        temp = Automobile(modello,marca,casaProd,cilindrata,prezzo,numTelaio)
        self.magazzino.append(temp)
        print("Auto aggiunta con successo")
    
    def stampaMacchine(self):
        if len(self.magazzino)==0:
            print( "Non ci sono auto presenti in magazzino!")
            return
        else:
            print("le auto presenti in magazzino sono:")
            for auto in self.magazzino:
                print(auto)

    def rimuovereDaMagazzino(self,telaio):
        for auto in self.magazzino:
            if auto.numTelaio == telaio:
                self.magazzino.remove(auto)
                print("l'auto con numero di telaio:"+str(telaio)+" è stata rimossa dal magazzino") 
                return 0  
    
    def stampaSommaPrezzi(self):
        prezzoTot = 0
        for auto in self.magazzino:
            prezzoTot += int(auto.prezzo)
        return prezzoTot

    ##per trovare la casa produttrice servono 2 funzioni
    #1.conta occorrenze del dato inserito
    #2.quella che verifica e controlla

    def _getCaseProd(self):
        caseProduttrici = []
        for auto in self.magazzino:
            caseProduttrici.append(auto.casaProd)
        return caseProduttrici
    
    def _contaOcc(self,casaProd):
        case = self._getCaseProd()
        cont = 0
        for i in range(0,len(case)):
            if case[i]== casaProd:
                cont +=1
        return cont
    
    def CasaPiuFrequente(self):
        caseProduttici = self._getCaseProd()
        casaFinale = caseProduttici[0]
        for i in range (0,len(caseProduttici)-1):
            if self._contaOcc(caseProduttici[i])>self._contaOcc(caseProduttici[i+1]):
                casaFinale = caseProduttici[i]
            else:
                casaFinale=caseProduttici[i+1]
        return casaFinale    


    def autoPiuBassa10k(self):
        ret = None
        for auto in self.magazzino:
            if int(auto.prezzo) < 10000:
                minCil = float(auto.cilindrata)
                ret = auto
                break
        for auto in self.magazzino:
            if int(auto.prezzo) < 10000 and float(auto.cilindrata) < minCil:
                ret = auto
                minCil = float(auto.cilindrata)
        
        return ret

    def _mediaPrezzi(self):
        cont = 0
        for auto in self.magazzino:
            cont +=1
        return self.stampaSommaPrezzi()//cont
    
    def autoPiuAltaMedia(self):
        ret = None
        for auto in self.magazzino:
            if int(auto.prezzo)>self._mediaPrezzi():
                maxCil = float(auto.cilindrata)
                ret = auto
        for auto in self.magazzino:
            if int(auto.prezzo)>self._mediaPrezzi() and float(auto.cilindrata) > maxCil:
                ret = auto

        return ret
    
    def CaseProdSottoMedia(self):
        caseprodFinale = []
        caseProduttrici = self._getCaseProd()
        for i in range(0,len(caseProduttrici)):
            for auto in self.magazzino:
                if auto.casaProd == caseProduttrici[i] and int(auto.prezzo) < self._mediaPrezzi():
                    if caseProduttrici[i] in caseprodFinale:
                        pass
                    else:
                        caseprodFinale.append(caseProduttrici[i])
        return caseprodFinale

        

            
            

            


c = Concessionaria()
c.aggiungiInMagazzino("grande punto","fiat","stellantis","1.1","12000",1213)
c.aggiungiInMagazzino("grande punto","fiat","stellantis","1.2","12000",1216)
c.aggiungiInMagazzino("grande punto","fiat","rca","0.9","12000",1214)
c.aggiungiInMagazzino("grande punto","fiat","clio","1.1","1200",1215)
c.aggiungiInMagazzino("grande punto","fiat","clio","1.2","1200",12123)
c.aggiungiInMagazzino("grande punto","fiat","rca","0.9","1200",1218)
c.aggiungiInMagazzino("grande punto","fiat","rca","0.9","9800",12110)
c.stampaSommaPrezzi()
print(c.CasaPiuFrequente())

print(c.autoPiuBassa10k())
print(c._mediaPrezzi())
print(c.autoPiuAltaMedia())

print(c.CaseProdSottoMedia())