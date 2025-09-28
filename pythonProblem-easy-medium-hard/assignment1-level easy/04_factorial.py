inp = int(input("enter the number which you want to get factorial value: "))
if (inp <= 0):
    print("invalid input") # cover edge case check 0 and -1
result = 1
for i in range(inp, 1, -1):
    result = result * i 
print(result) # cover positive value
