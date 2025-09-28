# write a class "Programmer" for storing information of few programmers working in microsoft

class Programmer:
  emp_Name = "Paaji"# this is class attribute
  emp_Id = 20054
  company = "microsoft"

  def __init__(self, emp_Id): # current class object reference self == this in java
    self.emp_Id = emp_Id
    print("calling")

info = Programmer("8976", "name", "microsof")
print(info.emp_Id, info.emp_Name, info.company)


