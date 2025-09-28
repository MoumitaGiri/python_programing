# Create a class `pets` from a class `Animals` and further create a class `Dog` from `Pets`. Add a method `bark` to class Dog

class Animals:
  eat = "food"
  drink = "water"
  sleep = "on time"
  def habits(self):
    print(f"tell animal habits: eat: {self.eat} drink {self.drink} sleeps {self.sleep}")

class Pets(Animals):
  play = "games"
  def play(self):
    print(f"eat {self.eat} play {self.play} sleeps {self.sleep}")

class Dog(Pets):
  @staticmethod
  def bark():
    print("Barks when seeing unknown person")

habit = Dog()
habit.bark()
habit.play() 
habit.habits()
