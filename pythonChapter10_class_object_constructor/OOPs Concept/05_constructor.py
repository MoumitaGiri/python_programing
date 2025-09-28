# "dunder" method "_init_" call automatically no need to call separately for init method only

class Employee:
  language = "py"
  salary = "1200"

  def _init_(self, name, last_name):
    self.name = name
    self.last_name = last_name
    print("I am here")

info_emp = Employee("moumita", "giri")
print(info_emp.name)
print(info_emp.last_name)
