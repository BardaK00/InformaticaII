#scrivere una funzione ricorsiva che scriva la stringa s senza vocali
voc="aeiouAEIOU"
s="mentalita"
def noVocali(s):
    if len(s)==0:
        return s
    noVocaliRic(s)

def noVocaliRic(s_corr):
    if s_corr[0] in voc:
        return noVocaliRic(s_corr[1:])
    return s_corr[0] + noVocaliRic(s_corr[1:])

print(noVocaliRic(s))