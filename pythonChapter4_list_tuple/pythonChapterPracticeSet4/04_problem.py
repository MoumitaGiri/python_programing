a = [3, 5, 7, 9]
sum = 0
temp = 0

for n in range(4):
    sum = sum + a[n]

for item in a:
    temp = temp + item
    
print(sum)
print(temp)
print(sum(a))



