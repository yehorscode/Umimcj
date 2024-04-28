import json
from index import *

data = open("colordata.json", 'r')
data = json.load(data)

cert_data = {}

for i in data:
    if data[i] == "True":
        cert_data[i] = "Yes"
    else:
        cert_data[i] = "No"

json.dump( cert_data, open( "cert_data.json", 'w' ) )