""" useCritter
    illustrates default namespace
    requires 'critter.py' to be in same directory

"""

import critter


#from critter import Critter
c = critter.Critter()
#there's only one critter defined here, with a default name
print(c.name)
#however, you'll see two print statements!

#importing critter.py causes its main() function to run