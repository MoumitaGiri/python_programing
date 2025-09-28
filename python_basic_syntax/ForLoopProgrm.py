'''n= []
m=[]

def even_odd():
    start = int(input())
    end = int(input())
    for i in range(start,end+1,1):
        if (i%2 == 0):
            n.append(i)
        elif (i%2 == 1):
            m.append(i)   
even_odd()
print(n,m) '''


def calculator():
    n=0
    L = [1,2]
    for i in L:
        n = L[0] + L[1]
        return n
calculator()
print(n)