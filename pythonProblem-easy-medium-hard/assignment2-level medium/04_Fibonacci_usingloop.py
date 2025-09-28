n = 10
series = []
firstNumber = 0
secondNumber = 1
series.append(firstNumber)
series.append(secondNumber)
print(series)

for i in range(1, n+1):
    result = firstNumber + secondNumber
    series.append(result)
    firstNumber = secondNumber
    secondNumber = result

print(series)
