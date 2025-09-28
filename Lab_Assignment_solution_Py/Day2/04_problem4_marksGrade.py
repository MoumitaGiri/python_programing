class Student:
  def __init__(self, mark):
    self.mark = mark
  def grade(self):
    if(self.mark >= 90 and self.mark <= 100):
      print("Student achieve: O Grade ")
    elif(self.mark >= 80 and self.mark <= 89):
      print("Student achieve: E Grade ")
    elif(self.mark >= 70 and self.mark <= 79):
      print("Student achieve: A Grade ")
    elif(self.mark >= 60 and self.mark <= 69):
      print("Student achieve: B Grade ")
    elif(self.mark >= 50 and self.mark <= 59):
      print("Student achieve: C Grade ")
    elif(self.mark >= 40 and self.mark <= 49):
      print("Student achieve: D Grade ")
    elif(self.mark >= 30 and self.mark <= 39):
      print("Student achieve: F Grade ")
    else:
      print("invalid input")
    

if __name__ == "__main__":
  
  try:
    mark = int(input("enter the number: "))
    inputmarks =  Student(mark)
    inputmarks.grade()
  except ValueError:
    print("Check your input number properly")