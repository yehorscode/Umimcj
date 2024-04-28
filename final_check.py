from index import *

with open("data/all_data.json", 'r') as file_data:
    data = json.load(file_data)

final_data = {}
counter = 0

for i in range(len(data)):
    if data[str(i)] == "True":
        final_data[i] = {}
        final_data[i]["addon_name"] = addon_names[i]
        final_data[i]["addon_icon_url"] = addon_icon_url[i]
        final_data[i]["addon_project_id"] = addon_project_ids[i]
        final_data[i]["addon_downloads"] = addon_downloads[i]
        final_data[i]["addon_short_descriptions"] = addon_short_descriptions[i]
        final_data[i]["addon_versions"] = addon_versions[i]
        final_data[i]["addon_categories"] = addon_categories[i]
        final_data[i]["addon_icon_url"] = addon_icon_url[i]
        final_data[i]["addon_followers"] = addon_followers[i]
        final_data[i]["manual_check"] = data[str(i)]
        counter +=1
    else:
        continue

with open("data/final_data.json", 'w') as outfile:
    json.dump(final_data, outfile)