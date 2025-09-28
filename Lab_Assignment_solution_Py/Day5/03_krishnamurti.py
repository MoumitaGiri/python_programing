# write a program to check whether a number is krishnamurti number or not

'''
A Krishnamurthy number is a number that is equal to the sum of the factorials of its digits.

Factorial of a digit d = product of all positive integers from 1 to d.
(Example: 4! = 4 x 3 x 2 x 1 = 24)
'''

class Number:
  def __init__(self, n):
    self.n = n 
  
  def factorial(self, rem):
    self.result = 1
    for i in range(self.rem, 0, -1):
      self.result =  self.result * self.rem
    return self.result

  def krishnamurtiNumber(self):
    self.sum = 0
    while(self.n != 0):
      self.rem = (self.n % 10)
      self.sum = self.sum + self.factorial(self.rem)
      self.n = self.n // 10
    return self.sum


      

if __name__ == "__main__":
  n = int(input("enter the number: "))
  a = Number(n)
  r = a.krishnamurtiNumber()
  if(r == n):
    print("krishnamurti")
  else:
    print("not krishnamurti")

