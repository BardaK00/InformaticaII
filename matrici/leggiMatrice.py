def leggiMatrix(r,c):
    m=[]
    for i in range(0,r):
        r=[]
        for j in range(0,c):
            n=int(input("inserisci il valore:"))
            r.append(n)
        m.append(r)
    return m

r=int(input("inserisci il valore delle righe:"))
c=int(input("inserisci il valore delle colonne:"))


print(leggiMatrix(r,c))