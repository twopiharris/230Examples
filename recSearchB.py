"""recipe search
   uses edamam free food database: whitelisted on pythonanywhere
"""

#requests or urllib to open the get request
import requests
#json to convert json text to python-native structures
import json

#apply for your own key on the api web site
appID = "your id here"
appKey = "your key here"

#this makes the api request.  Modify for what you are searching for
#don't forget to investigate for other parameters you can search for

searchTerm = "tuna"

r = requests.get("https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(
    searchTerm, appID, appKey))

#sometimes it's useful to begin with the full text so you can see
#how the data is organized.
#print(r.text)

# if you have limited free requests, make a sample request and save it to a
# local text file, then do your analysis on the text file.

#put the text in a python data structure for easier manipulation
result = json.loads(r.text)

# you always have to do digging and testing to see how the output data is
# organized.  This involves some trial and error.  Generally you'll be able
# to locate a key data element you want to work with.  In this case, it
# was the recipe object in the hits array.

recipes = result["hits"]


for rec in recipes:
  currentRec = rec["recipe"]
  #useful for investigating object.
  # print (currentRec.keys())

  print (currentRec["label"])
  print (currentRec["url"])

  #some data elements are other objects or lists
  #you'll want to parse them appropriately
  ingLines = currentRec["ingredientLines"]
  for i in ingLines:
      print(" * {}".format(i))
  print()

  print ("diet type: ")
  for d in currentRec["dietLabels"]:
      print (" * {}".format(d))
  print()

  print("health information:")
  for h in currentRec["healthLabels"]:
      print (" * {}".format(h))
  print()

  print()
  print ("=================================================")
  print()
