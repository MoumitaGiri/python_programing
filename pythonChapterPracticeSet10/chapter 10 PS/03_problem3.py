


class Demo:
  a = "moumita" # class attribute

obj = Demo() # object creation
print(obj.a) # print class attribute because instance attribute is not present
obj.a = 0 # instance attribute is set
print(obj.a) # print instance attribute because instance attribute s present
print(Demo.a) # print class attribute 

#note : Answer: (class attribute wont change)