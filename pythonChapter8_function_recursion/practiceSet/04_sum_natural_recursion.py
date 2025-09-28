# write a recursion function to calculate the sum of first n natural numbers
'''
sum_natural_number(1) = 1
sum_natural_number(2) = 1 + 2
sum_natural_number(3) = 1 + 2 + 3
sum_natural_number(4) = 1 + 2 + 3 + 4 
sum_natural_number(5) = 1 + 2 + 3 + 4 + 5
.
.
sum_natural_number(n) = sum(n-1) + n
'''

def sum(n):
    if(n == 1): # base codition  other wise it will go to zero  and -1 and so on
        return 1
    sumOfNatural = sum(n-1) + n
    return sumOfNatural

print(sum(5))

