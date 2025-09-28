
list = ["pineapple", "orange", "cherry", "apple", "mango"]
list[0:6:5] = ["apple"]
list[-1:6:5] = ["pineapple"]
print(list)


list = [str(x) for x in input().split()]
list[0:6:5] = ["apple"] 
list[-1:6:5] = ["pineapple"]
print(list)