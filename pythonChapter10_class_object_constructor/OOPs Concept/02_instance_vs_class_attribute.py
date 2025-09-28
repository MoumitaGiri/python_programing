
class Emp():
  lang = 'Py'  # This is class attribute
  salary = 1200
  Id = 'girim'

raja = Emp()
raja.lang = "javascript" # This is instance attribute
print(raja.Id, raja.salary, raja.lang)

# Note: instance attribute takes preferrence over class attributes during assignment & retrieval