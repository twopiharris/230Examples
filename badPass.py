""" password attempt """

correct = "Python"
guess = ""

numTries = 0

keepGoing = True

while keepGoing:
    guess = input("Password: ")
    if guess == correct:
        keepGoing = False
    numTries += 1
    if numTries >= 3:
        keepGoing = False
    print ("Tries: {}".format(numTries))


