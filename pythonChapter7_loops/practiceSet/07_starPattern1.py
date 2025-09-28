n = 3

for row in range(1, n+1):
    spaces = (n - row)
    stars = (2 * row - 1)
    print(" " * spaces + "*" * stars)