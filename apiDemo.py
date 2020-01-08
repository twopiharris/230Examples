import requests

# The highest form of the internet - getting random Chuck Norris jokes


url = "https://rapidapi.p.rapidapi.com/jokes/random"

headers={
    "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.https://rapidapi.p.rapidapi.com",
    "X-RapidAPI-Key": "522e8adcb4mshe30485d9ca7e91dp1480abjsn841b00d1f0f1",
    "accept": "application/json"
}

r = requests.get(url, headers = headers)
#print(r.json())


j = r.json()
print (j["value"])

