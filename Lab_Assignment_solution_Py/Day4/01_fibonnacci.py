# write a program in C to generate first N fibbonacci series number

class FibbonacciSeries:
  def __init__(self,num1, num2, l):
    self.num1 = num1
    self.num2 = num2
    self.l = l

  def series(self):
    for i in range(2, 10):
      result = self.num1 + self.num2
      self.l.append(result)
      print(result)
      self.num1 = self.num2
      self.num2 = result

if __name__ == "__main__":
  num1 = int(input("enter the number1: "))
  num2 = int(input("enter the number2: "))
  a = FibbonacciSeries(num1, num2, [])
  print(f"{num1}")
  print(f"{num2}")
  a.series()