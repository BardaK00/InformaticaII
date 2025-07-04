from ll import Linkedlist
from out import Messaggio
from out import Utente
class Sistema:
    def __init__(self,messaggi:Linkedlist, utenti:Linkedlist):
        self.listaMessaggi = messaggi
        self.listaUtenti = utenti
    
    def nessunaLettura(self,nomeDestinatario):
        nonLetti = []
        
        for messaggio in self.listaMessaggi:
            if messaggio.getNomeDestinatario() == nomeDestinatario and not messaggio.letto():
                nonLetti.append(messaggio.getNomeMittente())
        return set(nonLetti)

    def cittaUnica(self,dataInizio,dataFine):
        for messaggio in self.listaMessaggi:
            Citta = None
            if messaggio.getData >= dataInizio and messaggio.getData <= dataFine:
                if self._contaCardMessaggio(messaggio.getNomeMittente(),messaggio.getNomeDestinatario()) >= 2:
                    if not messaggio:
                        pass



    def _contaCardMessaggio(self,nomeMitt,nomeDest):
        cont = 0
        for messaggio in self.listaMessaggi:
            if messaggio.getNomeMittente()==nomeMitt and messaggio.getNomeDestinatario()==nomeDest:
                cont += 1
        return cont
    
    