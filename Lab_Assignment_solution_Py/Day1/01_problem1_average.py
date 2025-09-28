# write a program to compute avg of three floating point numbers which may be poistive and negative

class Average:

  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def compute(self):
    print(f"Print average of two numbers: {self.num1 + self.num2}")

if __name__ == "__main__":
  num1 = float(input("enter the floating first number: "))
  num2 = float(input("enter the floating second number: "))
  avg = Average(num1, num2)
  avg.compute()


