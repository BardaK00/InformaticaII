class Persona:
    def __init__(self,nome,età):
        self.nome=nome
        self.età=età
    #repr trasforma l'oggetto in una stringa e viene richiamato quandp ad esempio si utilizza il print
    #col nome dell'oggetto al suo interno
    def __repr__(self):
       return "nome:"+self.nome + ", età:"+str(self.età)
    
    #ridefinizione dell'== negli oggetti
    def __eq__(self,obj):
        #is istance verifica che obj appartiene alla classe persona, se non è così ritorna false
        #viene utilizzato per comparare solo lo stesso tipo di istanze appartenenti alla stessa classe
        #sennò l'interprete darà errore
        #esempio:isistance(oggetto,classe)
        if obj is None or not(isinstance(obj,Persona)):
            #is istance comunque restituisce 
            #false anche nel caso in cui obj sia un oggetto None
            return False
        
        #se self ha lo stesso indirizzo di obj e quindi è letteralmente lo stesso oggetto returno true
        #a prescindere
        if self is obj:
            return True
        
        #caso che compara ognuno degli attributi della classe
        return self.nome == obj.nome and self.età==obj.età
    
#è possibile anche ridefinire il not equal attraverso la scrittura del metodo __ne__
        
    #funzione che prende l'età
    def getEtà(self):
        return self.età
    
    #funzione che prende il nome
    def getNome(self):
        return self.nome
        
p1=Persona("manuel",15)

def LeggiPersona():
    nome = input("inserisci il nome:")
    età=int(input("inserisci l'età:"))
    return Persona(nome,età)


#nelle classi l'operatore == compara gli indirizzi,quindi può essere riscritto nella funzione __eq__ della classe
def cercaPersonaEtà(l,age):
    for p in l:
        if p.getEtà() == age:
            return p
        
def esisteGia(l,p):
    for pCor in l:
        if pCor == p:
            return True
    return False



l=[]
for i in range(0,3):
    p=LeggiPersona()
    l.append(p)



p2=Persona("manuel",13)


if(esisteGia(l,p2)):
    print("la persona:",p2,"si trova già in lista.")
else:
    print("la persona",p2,"non si trova in lista")

