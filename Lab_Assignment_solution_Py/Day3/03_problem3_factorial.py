# write a program to calculate factorial value of a number

class Factorial:
  def __init__(self, number, factorial):
    self.number = number
    self.factorial = factorial
  def Value(self):
    for i in range(1,self.number):
      self.factorial = self.number * i
      self.number = self.factorial
    print(f"Factorial of the number: {self.number}")  

if __name__ == "__main__":
  number = int(input("enter the number: "))
  n = Factorial(number, 1)
  n.Value()

      