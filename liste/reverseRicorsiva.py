

def reverseRic(l):
    if len(l)>0:
        print(l[len(l)-1])
    n=l[len(l)-1]
    l.pop(len(l)-1)
    reverseRic(l)
    l.insert(len(l)-1,n)
    

l=[1,2,3,4,5,6]
reverseRic(l)
