""" accessMethods.py
    demonstrates getters and setters
"""

class Critter(object):
  def __init__(self, name = "Anonymous"):
    self.__name = name

  def getName(self):
    return self.__name

  def setName(self, name):
    self.__name = name

def main():
  c = Critter()
  c.setName("Marge")
  print(c.getName())

if __name__ == "__main__":
  main()
