""" Guido.py
    Illustrates if statement
    Say something nice if the user's name
    is Guido """

firstName = input("What is your first name? ")
print("Nice to meet you, {}.".format(firstName))

if firstName == "Guido":
    print("Hey, thanks for inventing Python!")

print("That was fun")