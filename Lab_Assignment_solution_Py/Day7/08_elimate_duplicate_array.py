'''
Write a program to eliminate duplicates from an array using function.
'''

class program:
  def __init__(self, arr):
    self.arr = arr
  def eliminations(self):
    new_array = []
    for i in self.arr:
      if  i not in new_array:
        new_array.append(i)
    print(f"final array: {new_array}")

if __name__ == "__main__":
  arr = [1, 2, 9, 8, 3, 7, 4, 6, 5, 3, 1, 2]
  print(f"input array: {arr}")
  a = program(arr)
  a.eliminations()
