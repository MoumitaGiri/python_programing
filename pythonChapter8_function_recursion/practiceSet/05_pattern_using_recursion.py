# write a py func() to print n lines of the following pattern

def pattern_1(n):
    if(n == 0):
        return
    print("*" * n)
    pattern_1(n-1) # not understand this line

pattern_1(3)

# not using recursion
n = 3

def pattern(n):
    print("*" * n + "\n" + "*" * (n-1) + "\n" "*" * (n-2))

print(pattern(n))
