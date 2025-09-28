# write a program to print even and odd numbers between 1 and N

class number:
  def __init__(self, n):
    self.n = n
  def CheckOddEven(self):
    for i in range(1, self.n+1):
      if(i % 2 != 0):
        print(f"is odd number: {i}")
      else:
        print(f"not even number: {i}")

if __name__ == "__main__":
  n = int(input("enter the range: "))
  a = number(n)
  a.CheckOddEven()





  