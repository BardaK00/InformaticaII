def palindromo(s):
    for i in range (0,len(s)//2):
        #si usano // per le divisioni perchè arrotonda alla parte intera
        if(s[i]!=s[len(s)-1-i]):
            print("la stringa non è palindroma!")
            return 0
    print("stringa palindroma")

m=input("inserisci una parola:")
palindromo(m)