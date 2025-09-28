n = 10
number = int(input("enter the number: "))

for i in range(n, 0, -1):
    mul = number * i
    print(str(number) + "X" + str(i) + "=" + str(mul))
