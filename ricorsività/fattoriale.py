a=int(input("inserisci un numero di cui vuoi conoscere il fattoriale:"))

def fattoriale_ric(a):
    if a<2:
        return 1
    return a*fattoriale_ric(a-1)
    
print(fattoriale_ric(a))

