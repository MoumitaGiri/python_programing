'''
fibonacci_series(n) = [0, 1, 1, 2, 3, 5, 8, 13, 21 ... n]
.
let n3 = n1+n2
    n4 = n2+n3
fibonacci_series(n) = [n1, n2, (n1+n2), (n2+n1+n2) ... n]
fibonacci_series(n) = [n1, n2, n3, (n2+n3), (n3+n2+n3) ... n]
fibonacci_series(n) = [n1, n2, n3, n4 ... n]
'''
n = 5
f1 = 0
f2 = 1
data = []
data.append(f1)
data.append(f2)
print(data)
for i in range(n):
    f3 = f1 + f2
    data.append(f3)
    f1 = f2
    f2 = f3

print(data)

    
