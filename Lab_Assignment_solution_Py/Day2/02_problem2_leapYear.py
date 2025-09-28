class LeapYear:
  def __init__(self, year):
    self.year = year
  def leap(self):
    if(self.year%400 == 0):
      print("Year is a Leap year")

    elif(self.year%4 == 0 and self.year%100 != 0):
        print("Year is  a leap year")
    else:
      print("Year is not a leap year")

if __name__ == "__main__":
  year = int(input("enter the year: "))
  yr = LeapYear(year)
  yr.leap()
