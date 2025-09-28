'''
Write a program in C to generate the following pattern:
        
  1
  2   3
  4   5   6
  7   8    9  10
  11  12  13 14 15

'''
#solution:

class Pattern2:
  def __init__(self, n):
    self.n = n
  def logicOfPattern(self):

    for row in range(1, self.n+1):
      self.space = self.n - row
      self.num = 2 * row - row
      print(f"{self.num} {" " * self.space}")

if __name__ == "__main__":
  n = int(input("enter the number: "))
  a = Pattern2(n)
  a.logicOfPattern()