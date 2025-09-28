a = (4, "Harry", 20.0, True)

a[1] = str(type(a)) #ouput: TypeError: 'tuple' object does not support item assignment
print(a) # once tuple created cannot change

