# write a program to convert centigrde to Fahrenheit and vice versa

class Temperature:
  def __init__(self, centigrade):
    self.centigrade = centigrade

  def convert(self):
    return f"Convert centigrade to fahrenheit: {self.centigrade * (9/5) + 32} °F"

if __name__ == "__main__":
  centigrade = int(input("enter the centigrade: "))
  con = Temperature(centigrade)
  print(con.convert())