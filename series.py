n = list()
m =list()

def series():
    start = int(input())
    end = int(input())
    #n = list()
    for i in range(start,end,1):
        if (i%2 ==1):
            n.append(i)


    n1=0
    n2=1
    m.append(n1)
    m.append(n2)
    fibo_end = int(input())
    #m = list()
    for x in range(6,fibo_end-1,1):
        c = n1 + n2 
        m.append(c)
        n1 = n2
        n2 = c
  
series()
print(n)
print(m)
x=0
y=0
L=[]
for i in range(0,10,1):
    if (i%2 != 0):
        L.append(m[x])
        x = x+1
    else:
        L.append(n[y])
        y = y+1

print(L)
