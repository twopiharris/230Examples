""" Critter.py
    Basic critter class
    includes a constructor
"""

#import pdb

print("In critter.py, namespace is {}".format(__name__))

class Critter(object):
  def __init__(self):
    object.__init__(self)
    self.name = "Anonymous"

  def sayHi(self):
    print("Hi, my name is {}!".format(self.name))


def main():
  #pdb.set_trace()
  print("I'm in critter.py main")
  c = Critter()
  c.name = "George"
  c.sayHi()

#main()


#run main if I was not imported

if __name__ == "__main__":
  main()
