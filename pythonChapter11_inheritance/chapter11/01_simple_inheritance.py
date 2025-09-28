class Employee:
  company = "Microsoft"
  language = "py"

  def grow(self):
    print(f"employee in {self.company} good at {self.language}")

class Programmer(Employee):
  company = "ITC infotech"

  def printPolicy(self):
    print(f"this is also good company for who knows {self.language}")

comp = Programmer() # object creation
comp.grow() # method/function calling
comp.printPolicy()

