# write a program to greet all the person names stored in a list 'l' and which starts with S

l = ["Harry", "Soham", "Sachin", "Rahul", "Sonam", "Puri"]
 
for name in l:
    if(name.startswith("S")): # startswith function
        print(f"Hello GDmorning {name}")
    else:
        print(f"Hello GdNight {name}")
