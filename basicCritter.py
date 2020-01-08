""" basicCritter.py
    most basic OOP example
"""

class Critter(object):
  name = "Anonymous"

c = Critter()
print(c)
print(c.name)
c.name = "George"
print(c.name)