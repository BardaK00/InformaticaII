#Scrivere una funzione ricorsiva che, data una stringa s, restituisce vero se la stringa 
# contiene solo coppie consecutive formate da una cifra numerica e un carattere alfabetico; 
# falso altrimenti.
s="a1b2v3c4"
s1="aab1v3ccb2"

def coppie_alternate_ric(s):
    if len(s)==0:
        return False
    elif len(s)==1:
        return True
    
print(coppie_alternate_ric(s))
print(coppie_alternate_ric(s1))