# write a program to print all armstrong numbers between 1 to N

class Number:
  def __init__(self, n, rem, sum):
    self.n = n
    self.rem = rem
    self.sum = sum
  def amrstrong(self):
    while(self.n<=0):
      self.rem = self.n % 10
      self.sum = self.sum + ((self.rem)**3)
    print(f"{self.sum}")
    if(self.sum == self.n):
      print(f"The number is armstrong: {self.n}")
    else:
      print("the number is not armstrong")

if __name__ == "__main__":
  n = int(input("enter the number"))
  a = Number(n, 1, 1)
  a.amrstrong()

