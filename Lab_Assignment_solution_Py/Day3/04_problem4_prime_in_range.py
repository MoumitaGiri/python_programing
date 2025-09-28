# Write a program to print all prime numbers between 1 and N

##### not solvable 
class Number:

  def Prime(num):
    if(num <=1):
      return False
    for i in range(2, num):
      if(num % i == 0):
        return False
    return True

if __name__ == "__main__":
  num = int(input("enter the value: "))
  p = Number()
  p.Prime()