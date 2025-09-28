class Programmer:
  emp_Name = "Paaji"# this is class attribute
  emp_Id = 20054
  company = "microsoft"

  def _init_(self, emp_Id):
    self.emp_Id = emp_Id
    print("calling")

  @staticmethod
  def hello():
    print("hello all")

info = Programmer()
print(info.emp_Id, info.emp_Name, info.company)
info.hello()

