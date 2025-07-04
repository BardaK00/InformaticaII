def estraiColonna(m,c):
    res =[]
    for i in range(0,len(m)):
        res.append(m[i][c])
    return res

m=[[1,2,3],[1,2,3],[1,2,3]]
print(estraiColonna(m,1))