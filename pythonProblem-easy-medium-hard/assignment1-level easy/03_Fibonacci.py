n = 5
list = []
firstNumber = 0
secondNumber = 1

list.append(firstNumber)
list.append(secondNumber)
print(list)

for i in range(2, n):
    result = firstNumber + secondNumber
    list.append(result)
    firstNumber = secondNumber
    secondNumber = result
    print(list)

