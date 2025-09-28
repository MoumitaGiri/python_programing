#find the factorial of user inut number

num = int(input("enter the number: "))
fact =1
if(num <= 0):
    print("input invalid")
for i in range(num, 1, -1):
    fact = fact * i
print(fact)
