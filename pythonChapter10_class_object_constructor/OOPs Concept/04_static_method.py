class employee():
  lang = 'py'
  salary = 1200

  def getInfo(self):
    print(f"which language you know {self.lang}")
  
  # def greet(self):
  #   print("Good morning") # as there were no attribute calling we can write it in differnt form

  @staticmethod  # staticmethod is a decorator, no obj needed, no obj property needed
  def greet():
    print("Good morning!")

data = employee()
data.getInfo()
data.greet()
employee.getInfo(data)
