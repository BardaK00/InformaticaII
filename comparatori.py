#comparare il contenuto di 2 liste
l1 =[1,2,3]
l2=[1,2,3]
if l1==l2:
    print("si")
else:
    print("No")
#compara gli indirizzi di memoria delle 2 liste
if l1 is l2:
    print("sisi")
else:
    print("nono")

#quando si comparano tipi di base bisogna usare == poichè è possibile che con l'is gli indirizzi siano diversi
#is si usa solo per sapere se la locaaione di memoria in cui è contenuta la rappresentazione dell'oggetto è la 
#stessa