#sum of first n natural numbers
# positive integer number is natural number

n = 5
sum = 0
for i in range(0,n):
    if(i <= 0):
        continue
    sum = sum + i
print(sum)
