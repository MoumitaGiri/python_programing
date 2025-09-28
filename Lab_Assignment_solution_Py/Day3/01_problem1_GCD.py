# write a program to calculate GCD of two integer numbers
'''
Logic Dry run:
Find the GCD of example 60 and 48:

Step 1: Start with a = 60, b = 48.

Compute r = 60 % 48 = 12.
Update: a = 48, b = 12.
Step 2: Now a = 48, b = 12.

Compute r = 48 % 12 = 0.
Update: a = 12, b = 0.
Step 3: Since b = 0, stop.

The GCD is the current value of a, which is 12.

# Step 1: Store the current n2 in a temporary variable
    temp = self.n2  

    # Step 2: Update n2 to be the remainder of n1 divided by n2
    self.n2 = self.n1 % self.n2  

    # Step 3: Move the old n2 value into n1
    self.n1 = temp  

    # Debugging print (to see the process)
    print(f"Current values -> n1: {self.n1}, n2: {self.n2}")

'''



class GCD:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def HCF(self):
    while self.num2 != 0:
      temp = self.num2
      self.num2 = self.num1 % self.num2
      self.num1 = temp
      print(f"num1: {self.num1} , num2: {self.num2} ")
    print(f"GCD of the two number: {self.num1}")

if __name__ == "__main__":
  num1 = int(input("enter the first number: "))
  num2 = int(input("enter the second number: "))
  a = GCD(num1, num2)
  a.HCF()
















