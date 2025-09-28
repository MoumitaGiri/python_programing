class Employee:
  
  def __init__(self, name, age, salary, companyName):
    self.name = name
    self.age = age
    self.salary = salary
    self.companyName = companyName

  @property # getter method property write using property annotation which is called as prfoperty decorators
  def company(self):
    return self.companyName
  
  @company.setter
  def company(self, companyName):
    self.companyName = companyName

dev_info = Employee("Rohan", 22, 65400, "ITC")
print(dev_info.company)

dev_info.company = "TCS"
print(dev_info.company)

