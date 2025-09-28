# write a program to determine whether a number is a prime or not

class Number:
  def __init__(self, number):
    self.number = number
  def checkPrime(self):
    if(self.number%2 != 0):
      print(f"The {self.number} is a prime number")
    else:
      print(f"The {self.number} is not a prime number")

if __name__ == "__main__":
  try:
    number = int(input("enter the number: "))
    num = Number(number)
    num.checkPrime()
  # except Exception as e:
  #   print(e)
  except ValueError:
    print("check the input it is not correct")



