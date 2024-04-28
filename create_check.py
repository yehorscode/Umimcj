from index import addon_names, addon_project_ids, addon_downloads, addon_short_descriptions, addon_versions, addon_categories, addon_icon_url, addon_followers, addon_slug
from time import sleep
from index import debug, critical_error, error
import json

key = "create"
data = {}

for i in range(len(addon_names)):
    if key in addon_names[i].lower() or key in addon_short_descriptions[i].lower():
        data[i] = "True"
    else:
        data[i] = "False"
json.dump( data, open( "addons.json", 'w' ) )
        