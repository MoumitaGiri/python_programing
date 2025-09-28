'''
Write a menu driven program in C  to generate first N Fibonacci numbers and non Fibonacci numbers using functions
N = natural number(positive number)
'''

class Fibo:
  def __init__(self, num1, num2, result, l):
    self.num1 = num1
    self.num2 = num2
    self.result = result
    self.l = l

  def series(self):
    self.l.append(self.num1)
    self.l.append(self.num2)
    print(f"{self.l}")
    for i in range(2, 10):
      self.result = self.num1 + self.num2
      self.l.append(self.result)
      self.num1 = self.num2
      self.num2 = self.result
    print(f"Fibonacci series: {self.l}")

    

if __name__ == "__main__":

  a = Fibo(0, 1, 0, [])
  a.series()