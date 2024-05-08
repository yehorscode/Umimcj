import json
from m_step1 import *

with open("manual_data.json", 'r') as manual_data:
    check_data = json.load(manual_data)

with open("data/cert_data.json", 'r') as cert_data:
    all_data = json.load(cert_data)

corrected_data = {}

# Merging the data
for i in range(len(all_data)):
    if str(i) in check_data:
        corrected_data[i] = check_data[str(i)]
    else:
        corrected_data[i] = all_data[str(i)]

# Save the corrected data
with open("data/all_data.json", 'w') as outfile:
    json.dump(corrected_data, outfile)