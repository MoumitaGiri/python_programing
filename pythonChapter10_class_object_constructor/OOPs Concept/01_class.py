
class Emp():
  lang = 'Py'  # This is class attribute
  salary = 1200
  Id = 'girim'

obj1 = Emp()
print(obj1.lang, obj1.salary, obj1.Id)

raja = Emp()
raja.name = "Raja" # This is instance attribute
print(raja.name, raja.salary, raja.lang)
 

# Here name is instance attribute and salary and language attributes as they directly belong to the class

