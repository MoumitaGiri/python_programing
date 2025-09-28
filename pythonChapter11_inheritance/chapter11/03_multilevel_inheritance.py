class Employee:
  company = "microsoft"
  language = "py"

  def empskill(self):
    print(f"employee of {self.company} knows {self.language} language")

class Programmer(Employee):
  team = "abc team"
  def teamName(self):
    print(f"employee who knows {self.language} language they are a part of {self.team}")

class ProgramManager(Programmer):
  IDTag = "Developer"
  def group(self):
    print(f"tell me the ID: {self.IDTag} for the employees in  {self.company} company")

emp = ProgramManager() # object created and emp is object reference
emp.empskill()
emp.teamName()
emp.group() 
  