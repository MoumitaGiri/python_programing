#write a program to generate factorial of a number using function

class Factorial:
  def __init__(self, n, result):
    self.n = n
    self.result = result
  def generateFactorial(self):
    
    for i in range(1, self.n):
      self.result = self.n * i
      self.n = self.result
    print(f"{self.result}")

if __name__ == "__main__":
  n = int(input("enter the number: "))
  a = Factorial(n, 1)
  a.generateFactorial()

