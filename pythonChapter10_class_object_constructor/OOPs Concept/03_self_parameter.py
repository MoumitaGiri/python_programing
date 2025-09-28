class Emp():
  lang = 'Py'  # This is class attribute
  salary = 1200
  Id = 'girim'
  def get_info(self):
    print(f"This the language: {self.lang}. This is salary: {self.salary}")

raja = Emp()
raja.lang = "javascript" # This is instance attribute
raja.get_info() # converted automatically to this Emp.get_info(harry)