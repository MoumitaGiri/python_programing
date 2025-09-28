a = 2
b = 9
c = 6

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>a and c>b):
        return c
    
print(f"Greatest Number: {greatest(a,b,c)}")