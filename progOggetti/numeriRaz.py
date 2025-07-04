class Razionale:
    
    def __init__(self,num,denom):
        if denom == 0:
            raise ZeroDivisionError()

        self._num=num
        self._denom=denom

        if denom < 0:
            self._num*=-1
            self._denom*=-1

        self._mdc()

    def _mdc(self):
        temp = 1
        if self._denom<self._num:
            max = abs(self._num)
        else:
            max = abs(self._denom)
        for i in range (1,max):
            if abs(self._num)%i==0 and abs(self._denom)%i==0:
                temp = i

        self._num//=temp
        self._denom//=temp  
    
    def __eq__(self,obj):
        if obj is None or not(isinstance(obj,Razionale)):
            return False
        
        if self is obj:
            return True
        
        return self._num==obj._num and self._denom == obj._denom
    
    def __repr__(self):
        return str(self._num) +"/"+str(self._denom)
    
    #riscrivere somma,sottrazione,prodotto,maggiore,maggiore uguale,minore,minore uguale
    def _mcdEntrambi(self,obj):
        temp = 1
        if self._denom<obj._denom:
            max = abs(self._denom)
        else:
            max = abs(obj._denom)
        for i in range (1,max+1):
            if abs(obj._denom)%i==0 and abs(self._denom)%i==0:
                temp = i
        return temp
    
    def _mcm(self,obj):
        return abs(self._denom*obj._denom)//self._mcdEntrambi(obj)
    
    def __add__(self,obj):
       mcm = self._mcm(obj)
       return Razionale(((mcm//self._denom)*self._num)+((mcm//obj._denom)*obj._num),mcm)

    def __sub__  (self,obj):
        mcm = self._mcm(obj)
        return Razionale(((mcm//self._denom)*self._num)-((mcm//obj._denom)*obj._num),mcm)
    
    def __mul__(self,obj):
        return Razionale(self._num * obj._num,self._denom*obj._denom)
    
    def __truediv__(self,obj):
        if obj._num == 0:
            raise ZeroDivisionError("Divisione per zero non consentita")
        else:
            return self.__mul__(Razionale(obj._denom,obj._num))
        

    #implementazione maggiore,maggiore uguale,minore,minore uguale
    #dovrebbero essere funzioni booleane che returnano True e false

    #un numero razionale è maggiore di un altro se la divisione tra num e denum di self sono maggiori
    #della disione di num e denum di obj

    #maggiore stretto

    def __gt__(self, obj):  # maggiore
        return (self._num * obj._denom) > (obj._num * self._denom)

    def __ge__(self, obj):  # maggiore uguale
        return (self._num * obj._denom) >= (obj._num * self._denom)

    def __lt__(self, obj):  # minore
        return (self._num * obj._denom) < (obj._num * self._denom)

    def __le__(self, obj):  # minore uguale
        return (self._num * obj._denom) <= (obj._num * self._denom)

         
    
#r=Razionale(4,3)
#q=Razionale(1,2)

#print(r)
#print(q)

#if r==q:
 #   print("sono uguali")
#else:
#print("diversi")   

