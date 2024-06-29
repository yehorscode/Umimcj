from m_step1 import *

with open("manual_data.json", 'r') as file_data:
    data = json.load(file_data)

final_data = []

for i in range(len(data)):
    if data[str(i)] == "True":
        item = {}
        item["addon_name"] = addon_names[i]
        print(item["addon_name"])
        print(addon_slug[i])
        print("-----------")
        item["addon_slug"] = addon_slug[i]
        item["addon_icon_url"] = addon_icon_url[i]
        item["addon_project_id"] = addon_project_ids[i]
        item["addon_downloads"] = addon_downloads[i]
        item["addon_short_descriptions"] = addon_short_descriptions[i]
        item["addon_versions"] = addon_versions[i]
        item["addon_categories"] = addon_categories[i]
        item["addon_icon_url"] = addon_icon_url[i]
        item["addon_followers"] = addon_followers[i]
        item["manual_check"] = data[str(i)]
        item["addon_authors"] = addon_authors[i]
        final_data.append(item)

with open('data/final_data.json', 'w') as outfile:
    json.dump(final_data, outfile, indent=4)

print(len(final_data))