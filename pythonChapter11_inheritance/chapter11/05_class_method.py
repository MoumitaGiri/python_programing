class Employee:
  a = 1 # class attribute
  def grow(self):
    print(f"Print the class attribute {self.a}")

e = Employee()
e.a = 45

e.grow() # it will print 45 as instance attribute(between class and instance --> instance attribute gets more priority)

# # class method is a method which is bound to class not the class object of the class
# class emp():
#   a = 1
#   @classmethod #(decorator is used to create a class method)
#   def grow(cls):
#     print(f"print class attribute {cls.a}")

# e = emp()
# e.a = 56
# e.grow()