#demonstrate hashing as a secure way to handle passwords

import hashlib

#instantiate sha 256 algorithm
correct = hashlib.sha256(b'CS23000 rocks').digest()
#creates a list of bytes
print ("Correct: " + str(correct))

# you can store the hash in a database or file
# never compare or store password.  Just run guess
# against same hashing algorithm and compare hashes.

guess = input("password: ")
guess = hashlib.sha256(guess.encode("utf-8")).digest()
print ("Guess: " + str(guess))

if guess == correct:
    print("Correct")
else:
    print ("Incorrect")


