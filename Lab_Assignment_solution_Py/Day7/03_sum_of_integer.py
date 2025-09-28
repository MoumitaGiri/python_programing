'''
Write a program to find the sum of all integers greater than 100 and less than 200 that are divisible by 7 using function.
'''

class NumInteger:
  def __init__(self, n, l, sum_result):
    self.n = n
    self.l = l
    self.sum_result = sum_result

  def GreaterInteger(self):
    for i in range(100, 201):
      self.n = i
      if(self.n % 7 == 0):
        self.l.append(self.n)
    print(f"{self.l}")
    for x in self.l:
      self.sum_result = self.sum_result + x
    print(f"sum_result: {self.sum_result}")

if __name__ == "__main__":

  a = NumInteger(0, [], 0)
  a.GreaterInteger()
