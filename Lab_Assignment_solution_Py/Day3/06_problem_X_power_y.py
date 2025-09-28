# write a program in C to calculate X power y without using pow() function

class Power:
  def __init__(self, X, y):
    self.X = X
    self.y = y

  def checkPower(self):
    print(f"{self.X ** self.y}")

if __name__ == "__main__":
  X = int(input("enter the number: "))
  y = int(input("enter the power number: "))
  p = Power(X, y)
  p.checkPower()