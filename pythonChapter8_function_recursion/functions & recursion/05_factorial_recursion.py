# solve factorial problem with recursion
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
.
.
.
factorial(n) = n x (n-1) x . . . x 3 x 2 x 1

factorial(n) = n * factorial(n-1)

'''

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n * fact(n-1)

n = int(input("enter the factorial number: "))
print(f"the factorial of that number: {fact(n)}")
