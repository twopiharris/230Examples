""" readFile.py
    read the contents of a text file
"""

groceries = []
file = open("groceries.txt", "r")
for line in file:
  line = line.strip()
  groceries.append(line)

print(groceries)

output = "We need "
for item in groceries:
     output += item + ", "

output += "dude."

print(output)

file.close()