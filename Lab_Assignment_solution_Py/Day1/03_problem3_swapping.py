# # write a program to swap two numbers
# # i) with using third variable
class Numbers:
  def __init__(self, num1, num2, result):
    self.num1 = num1
    self.num2 = num2
    self.result = result
    print(f"before swap {self.num1} {self.num2}")
  def swap(self):
    self.result = self.num1
    self.num1 = self.num2
    self.num2 = self.result
    print(f"after swap: {self.num1} {self.num2}")

if __name__ == "__main__":
  num1 = int(input("enter the num1: "))
  num2 = int(input("enter the num2: "))
  n = Numbers(num1, num2, 0)
  n.swap()

# ii) without using third variable

class Number:
  def __init__(self, n1, n2):
    self.n1 = n1
    self.n2 = n2
    print(f"before swap: {self.n1} {self.n2}")

  def swapping(self):
    self.n1, self.n2 = self.n2, self.n1
    print(f"after swap: {self.n1} {self.n2}")

if __name__ == "__main__":
  n1 =  int(input("enter the number n1: "))
  n2 =  int(input("enter the number n2: "))
  m = Number(n1, n2)
  m.swapping()
