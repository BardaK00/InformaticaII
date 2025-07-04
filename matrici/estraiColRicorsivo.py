m=[[1,2,3],
   [1,2,3],
   [1,2,3]]

#i indica la riga 
def estraiColRic(m,c,i):
    if i==len(m):
        return []
    
    return [m[i][c]]+estraiColRic(m,c,i+1) #CREA UNA NUOVA LISTA con primo elemento m[i][c] e gli altri
    #affianco attraverso la ricorsività
    

print(estraiColRic(m,1,0))