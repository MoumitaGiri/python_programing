# create a list of all odd numbers between 1-20 using comprehension


# without comprehension
# l1 = [] # take a empty list lets say l1
# i = 1
# for i in range(21):
#     if i % 2 != 0: # condition check odd number or not
#         l1.append(i) # adding method odd numbers between 1-20

# print(l1) # print the list

#with comprehension
# i = 1
# l2 = [int(i) for i in range(21) if i %2 != 0] # type casting i to int and using list comprehension to create a list of odd numbers
# print(l2)

input = [int(i) for i in input().split(",")]
print(input)

num = [int(y) for y in input().split(" ")]
print(num)

variable = [float(z) for z in input.split("\n")]
print(variable)