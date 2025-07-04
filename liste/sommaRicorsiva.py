l=[1,2,3,4,5,6,7]
def somma4(l):
    s=0
    if len(l)==0:
        return 0
    #n diventa l'ultimo valore dell'array alla posizione len(l)-1
    n=l[len(l)-1]
    #elimina l'ultimo elemento dell'array
    l.pop(len(l)-1)
    #fa la somma ricorsiva degli elementi tranne l'ultimo
    s=somma4(l)
    #aggiunge in coda alla lista l'ultimo elemento salvato precedentemente
    l.append(n)
    #ritorna la somma ricorsiva fino a len(l)-2 (pen'ultimo elemento) 
    # e gli somma l'ultimo elemento aggiunto dopo la chiamata di append
    return s+l[len(l)-1]

print(somma4(l))