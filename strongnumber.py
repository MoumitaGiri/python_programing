#l = [int(x) for x in input().split(' ')]


'''start = int(input())
end = int(input())
n= list()
m= list()
for i in range(start,end+1,1):
    if (i%2 == 0):
        n.append(i)
    elif (i%2 == 1):
        m.append(i)
        
print(n,m) '''    

'''start = int(input())
end = int(input())
for i in range(start, end+1, 1):
       n0 = n1 + n2
       n2 = n0 + n3
       n3 = n2'''
       


#L = [0 1 1 2 3 5 8 13 21]

#L = [int(x) for x in input().split(' ')]

'''start = int(input())
end = int(input())
n3 =list()
n3.append(0)
n3.append(1)
n1 = n3[0]
n2 = n3[1]
   
for i in range(1, end-1, 1):
    c= n1 + n2 
    n3.append(c)
    n1 = n2
    n2 = c
    
print(n3)'''


'''start = int(input())
end = int(input())
n = list()

for i in range(start, end+1, 1):
    count = 0
    for m in range(1, i+1, 1):
        if (i%m == 0):
            count = count+1
    if (count ==2):
        n.append(m)
        
print(n)'''
        
#fact =1
def func(y):
    fact =1
    
    for i in range(0,y,1):
        fact = fact * y 
        y = y - 1
    return fact
    #print(fact)
        
def strong():
    s=0
    x= int(input())
    temp = x
    le = len(str(x))
    for i in range(0,le,1):
        rem = x%10
        s =s + func(rem)
        x = x//10
    print(s)
      
    if (temp == s):
        print("it is strong number")
    else:
        print("it is not strong number")

strong()

   
   
   
   
   
   
   
   
   
      