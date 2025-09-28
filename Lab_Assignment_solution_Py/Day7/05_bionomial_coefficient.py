'''
Write a program in C  to generate bionomial coefficients using function.

'''

class Bionomial_Coeffiecient:
  def __init__(self, n, k):
    self.n = n
    self.k = k
    # n = total number of elements
    # k = number of selections


  def factorial(self, number):
    fact = 1
    for i in range(1, number+1):
      fact = fact * i # (fact *= i)
    return fact

  def expression(self):
    result = self.factorial(self.n)//(self.factorial(self.k)* (self.factorial(self.n-self.k)))
    print(f"binomial coefficient: {result}")

if __name__ == "__main__":
  n = int(input("enter the total number of the elements: "))
  k = int(input("enter the number of selections: "))
  a = Bionomial_Coeffiecient(n, k)
  a.expression()

