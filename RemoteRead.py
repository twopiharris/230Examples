""" note requests is not a built-in module
    It is included with pythonanywhere, but only addresses
    on the whitelist can be read
    http://www.pythonanywhere.com/whitelist"
"""

import requests

#url = 'https://www.google.com/search?q=monkey'
#url = "http://aharrisbooks.net/h5g"
url = "https://inventory.data.gov/dataset/032e19b4-5a90-41dc-83ff-6e4cd234f565/resource/38625c3d-5388-4c16-a30f-d105432553a4/download/postscndryunivsrvy2013dirinfo.csv"

r = requests.get(url)
for line in r:
    print(line)