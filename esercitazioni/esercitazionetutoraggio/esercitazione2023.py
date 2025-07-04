from ll import Linkedlist
from Piatto import Piatto
from Ingrediente import Ingrediente

class Sistema:
    def __init__(self, listaPiatti : list[Piatto], listaIngredienti : list[Ingrediente]):
        self.listaPiatti = listaPiatti
        self.listaIngredienti = listaIngredienti

    def verificaVegPiatto(self,piatto):
        ingredienti = piatto.getIngredienti()
        iter = iter(ingredienti)
        while not iter.finito():
            ing = next(iter)
            for ingred in self.listaIngredienti:
                if ing.getNome() == ingred.nome:
                    if not(ing.getAdattoVegetariani()):
                        return False
        return True        
            



    def verificaVegetariano(self,n):
        c = 0
        for piatto in self.listaPiatti:
            if self.verificaVegPiatto(piatto):
                c += 1
        if c >= n:
            return True
        else:
            return False
    

    def piattiConIngredienti(self,nomeIng,k):
        
        ret = Linkedlist()
        for piatto in self.listaPiatti:
            dosi=piatto.getDosi()
            ingredienti = piatto.getIngredienti()
            iterD = iter(dosi)
            iterI=iter(ingredienti)
            while not iter.finito():
                ing=next(iterI)
                dose=next(iterD)
                if nomeIng == ing.getNome() and k <= dose:
                    ret._aggiungiTesta(piatto.getNome())

                    


        