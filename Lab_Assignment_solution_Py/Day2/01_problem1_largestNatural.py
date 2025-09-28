#write a problem to print largest among N numbers
# N natural number means only positive number

class NaturalNumber:

  def __init__(self, n, l):
    self.n = n
    self.l = l
  def Number(self):
    if(self.n <= 0):
      print("invalid input")
    for i in range(1, self.n+1):
      self.l.append(i)
    self.l.sort()
    print(f"print the largest N number: {self.l[self.n-1]}")

if __name__ == "__main__":
  n = int(input("enter the number of range"))
  obj = NaturalNumber(n, [])
  obj.Number()
