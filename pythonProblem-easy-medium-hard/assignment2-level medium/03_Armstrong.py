# check armstrong number

digit = "153"
print(type(digit))
sum = 0
for dg in digit:
    print(dg)
    # squareOfDigits = int(dg)**2
    # sum = sum + squareOfDigits/
    cubeOfDigits = int(dg)**3
    sum = sum + cubeOfDigits
print(sum)