number = int(input("enter the input: "))

if(number <= 0):
    print("invalid input")

for i in range(2, number):
    
    if(number%i == 0):
        print("this number is not a prime numeber")
        break
else:
    print("this number is prime number")
 
