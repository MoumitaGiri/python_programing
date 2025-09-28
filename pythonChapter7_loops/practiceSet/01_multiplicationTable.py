# print multiplication of table given number using for loop

n = 10
number = int(input("enter the number from user input: "))
for i in range(1, n+1):
    multiplicationTable =  (number * i)
    print(str(number) + "X" +  str(i) + "=" +  str(multiplicationTable))

