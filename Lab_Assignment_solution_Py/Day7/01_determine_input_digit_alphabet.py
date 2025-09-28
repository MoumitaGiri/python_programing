# write a program to accept 10 charcaters and to display whether each input character is a digit or a lower case alphabet or an upper case alphabet using function

class characters:
  def __init__(self, n, l):
    self.n = n
    self.l = l

  def checkInput(self):
    self.l.append(self.n)
    for ch in self.l:
      if('A'<= ch <= 'Z'):
        print(f"the alphabet is in upper case: {ch}")
      elif('a' <= ch <= 'z'):
          print(f"the alphabet is in lower case: {ch}")
      elif('0' <= ch <= '9'):
          print(f"the input is digit: {ch}")
      else:
        print("input is special character") 

if __name__ =="__main__":
  n = input("the enter number: ")
  a = characters(n, [])
  a.checkInput() 


