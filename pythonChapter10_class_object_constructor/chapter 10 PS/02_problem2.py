# write a class "calculator" capable of finding square, cude and square root of a number

class calculator:
  
  def __init__(self, number):
    self.number = number

  def square(self):
    print(f"square of numbers: {self.number}*{self.number}")

obj = calculator(5)
obj.square()

