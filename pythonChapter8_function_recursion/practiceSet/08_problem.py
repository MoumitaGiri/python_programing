# write a python function to print multiplicaiontable of a given number

'''
multiplication(2) = 2 X 1
multiplication(2) = 2 X 2
multiplication(2) = 2 X 3
multiplication(2) = 2 X 4
multiplication(2) = 2 X 5
multiplication(2) = 2 X 6
multiplication(2) = 2 X 7
multiplication(2) = 2 X 8
multiplication(2) = 2 X 9
multiplication(2) = 2 X 10
.
.
multiplication(n) = n X (i)
'''

def multiplication(n):
    if (n == 0):
        return 0
    for i in range(1, 11):
        mul = n * i
        print(f"{n} X {i} = {mul}")
print(multiplication(5))