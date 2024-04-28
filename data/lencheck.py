import json
with open("data/final_data.json", 'r') as file_data:
    data = json.load(file_data)

print(len(data))