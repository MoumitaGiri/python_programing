class Employee:
  company = "Microsoft"
  language = "py"

  def grow(self):
    print(f"employee in {self.company} good at {self.language}")

class coder:
  language = "javascript"
  def printLang(self):
    print(f"print the language: {self.language}")

class Programmer(Employee, coder):
  company = "ITC infotech"

  def printPolicy(self):
    print(f"this is also good company who knows {self.language}")

comp = Programmer() # object creation
comp.grow() # method/function calling
comp.printPolicy()
comp.printLang()

