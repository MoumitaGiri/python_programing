# write a program to print all perfect numbers between 1 to N

class Number:
  def __init__(self, n, sum, l):
    self.n = n
    self.sum = sum
    self.l = l
  def ProperDivisor(self):
    for i in range(1, self.n):
      if(self.n % i == 0):
        print(f"this is a proper divisor {i}")
        self.l.append(i)
    print(f"print list of proper number {self.l}")
    for x in self.l:
      self.sum = self.sum + x
      print(self.sum)
    if(self.sum == self.n):
        print("this is a perfect number")
    else:
        print("this number is abundant not perfect")

if __name__ == "__main__":
  n = int(input("enter the number"))
  a = Number(n, 0, [])
  a.ProperDivisor()