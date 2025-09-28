# create a class (2 D vector)and use it to create another class representaing a 3 D vector

class TwoDVector:
  def __init__(self, i , j):
    self.i = i
    self.j = j

  def show(self):
    print(f"{self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
  def __init__(self,i, j, k):
    super().__init__(i, j) # use of super keyword because to inherit parent class
    self.k = k

  def show(self):
    print(f"{self.i}i + {self.j}j + {self.k}k")

vector2 = TwoDVector(1, 2)
vector3 = ThreeDVector(12, 3, 9)
vector2.show()
vector3.show()

