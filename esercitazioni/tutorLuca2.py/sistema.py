from ll import Linkedlist,Iteratore

class Sistema:
    def __init__(self,listaInterventi:Linkedlist,listaPersonale:Linkedlist):
        self.lista_interventi = listaInterventi
        self.lista_personale = listaPersonale

    def verifica(self):
        for personale in self.lista_personale:
            sotto = personale.get_unita_sotto_controllo()
            for unita in sotto:
                obj = self._get_object_from_name(unita)
                if obj.get_tipo()==False and personale.get_tipo():
                    return False
                elif obj.get_tipo() and personale.get_tipo()== False:
                    return False
        return True
    
    def _get_object_from_name(self,name):
        for personale in self.lista_personale:
            if personale.get_nome() == name:
                return personale
            
    #fine prima richiesta

    def _conta_interventi(self,unita,ruolo):
        cont = 0
        for intervento in self.lista_interventi:
            equipe = intervento.get_equipe()
            roles = intervento .get_ruoli()
            it_equipe = iter(equipe)
            it_roles = iter(roles)
            while not it_equipe.finito():
                nome = next(it_equipe)
                role = next(it_roles)
                if nome == unita.get_nome() and role == ruolo:
                    cont += 1 
        return cont
    
    def medico_frequente_con_ruolo(self,ruolo):
        personale_max = None
        it = iter(self.lista_personale)
        primo_personale = next(it)
        if primo_personale.get_tipo():
            max_operazioni = self._conta_interventi(primo_personale,ruolo)
            personale_max = primo_personale
        while not it.finito():
            new_pers = next(it)
            if new_pers.get_tipo():
                n_interventi = self._conta_interventi(new_pers,ruolo)
                if n_interventi > max_operazioni:
                    max_operazioni = n_interventi
                    personale_max=new_pers

        return personale_max.get_nome()

    #fine secondo metodo

    def durata_media(self,lp:Linkedlist):
        cont_durata = 0
        cont_interventi = 0
        for interventi in self.lista_interventi:
            equipe = interventi.get_equipe()
            for p in lp:
                if p.get_nome() in equipe and p.get_tipo()==True:
                    cont_durata += interventi.get_durata()
                    cont_interventi +=1
        if cont_interventi != 0:
            return cont_durata/cont_interventi
        else:
            return -1
        
        #fine terzo metodo
        