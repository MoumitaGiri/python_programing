class Employee:
  salary = 234
  increament = 20

  @property
  def salaryAfterIncrement(self):
    return (self.salary + self.salary * (self.increment / 100))

  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self, salary):
    self.increament = salary/(self.salary-1)*100
    
e = Employee()
e.salaryAfterIncrement = 280
# e.grow()
print(e.salary,e.increament)





# e = Employee()

# e.salary = 6789 # instance attribute
# e.increment = 21

# print(e.salary, e.increment)
