class Numerotelefonico:
    def __init__(self,tipo,numero):
        self.tipo=tipo
        self.numero=numero
        #eq str repr

    def __eq__(self,obj):
        return self.tipo == obj.tipo and self.numero==obj.numero
    
    def __str__(self):
        return "tipo:"+self.tipo+" numero:"+str(self.numero)
    
    def __repr__(self):
        return ""+self.tipo+""+str(self.numero)

class Contatto:
    def __init__(self,nome,cognome,numero=None):
        self.nome=nome
        self.cognome=cognome
        self.numero=numero
    
    def __eq__(self,obj):
        return self.nome==obj.nome and self.cognome==obj.cognome and self.numero==obj.numero
    
    def __str__(self):
        return "nome:"+self.nome+"\n"+"cognome:"+self.cognome+"\n"+"numero:"+str(self.numero)
    
    def __repr__(self):
        return ""+self.nome+""+self.cognome+""+str(self.numero)
    
    def _aggiungiNumero(self):
        a=input("inserisci il tipo di numero che vuoi aggiungere:")
        b=int(input("inserisci il numero di telefono:"))
        self.numero=Numerotelefonico(a,b)
        return Numerotelefonico(a,b)

    def _estraiNumero(self):
        return self.numero
    
    def _eliminaNumero(self):
        del(self.numero)
        self.numero=None

    def _copiaNumero(self,obj):
        a=self._estraiNumero()
        obj.numero=Numerotelefonico(a.tipo,a.numero)
       

        #eq str repr aggiungi numero elimina estrai e copia

class Rubrica(Contatto):
    def __init__(self):
        pass
    
    def _aggiungiContatto(self):
        a=input("inserisci il nome del nuovo contatto:")
        b=input("inserisci il cognome del nuovo contatto:")
        c=self._aggiungiNumero()
        return Contatto(a,b,c)
    
    def _rimuoviContatto(self):
        n=int(input("dimmi il numero del contatto da rimuovere"))


    
