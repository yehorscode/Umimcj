# Welcome to Umimcj
# Script made by my which is a fork-ish of my other project Umimc
# It is used to automate creating huge json files with all of create addons
# Contact me here: create-addons@proton.me
# Made with ♥ by yehors_code

def import_test():
    try:
        import requests
        from colorama import Fore, Back, Style
        import json
        from time import sleep
        import tqdm
    except ImportError:
        print("[CRITICAL] You don't have libraries needed to run the app! Install them!")
        print("Needed to install: requests, colorama, json, tqdm")
        quit()

# import_test (checks import libraries)    
import_test()
import requests
from colorama import Fore, Back, Style
import json
from time import sleep
from tqdm import *

print(Fore.CYAN+"""\nWelcome User!
This is Umimcj - an app made to scan popular mod sites like Modrinth and Curseforge
Data gathered is converted into JSON file
This app want to find all of the possible Create Mod addons and put it on one easy web-site
Happy using!\n"""+Fore.RESET)

# VERY IMPORTANT VALUES!
url_get_findrequest = "https://api.modrinth.com/v2/search?query="
url_get_findrequest_string_type_mod = "&facets=[[%22project_type:mod%22]]"
url_get_findproject = "https://api.modrinth.com/v2/project/"

# VERY IMPORTANT LISTS/DICTIONARIES!
addon_names = {}
addon_project_ids = {}
addon_downloads = {}
addon_short_descriptions = {}
addon_versions = {}
addon_categories = {}
addon_icon_url = {}
addon_followers = {}
# Headers for requests
headers = {
    'User-Agent': 'https://github.com/yehorscode/CreateAddons-Site (create-addons@proton.me)'}

# DEBUG MODE (Default: True)
debug_mode = True

# To ignore debug_mode use ,1 at the end for example. debug("Modrinth", 1)
def debug(debug_text, ignore=0):
    if debug_mode == True:
        print(f"{Fore.GREEN}[DEBUG] {debug_text}{Fore.RESET}")
    elif ignore == 1:
        print(f"{Fore.GREEN}[DEBUG] {debug_text}{Fore.RESET}")

def critical_error(critical_error_text):
    print(f"{Back.RED}[CRITICAL] {critical_error_text}{Back.RESET}")

def error(error_text):
    print(f"{Back.LIGHTYELLOW_EX}[ERROR] {error_text}{Back.RESET}")

# Action selection menu
print(f"""\n{Back.CYAN}Choose an action:{Back.RESET}
{Fore.CYAN}1. Modrinth Create Mod data gathering
2. Curseforge Create Mod data gathering
C. Color check
L. Labrinth status check{Fore.RESET}""")

# Action input
chosen_action = input(f"Input: ")

# Action running
if chosen_action == "1":
    debug("Chosen Action 1", 1)
    
    # Search parameters
#    fmod_search_query = input(f"{Fore.CYAN}What query you want to find for?{Fore.RESET}")
#    fmod_search_limit = int(input(f"{Fore.CYAN}How many hits to make? (30'000/manual) "))

    # Search limit
    fmod_search_limit = 30000
    # Default search input
    fmod_search_query = "create"
    # Labrinth search request
    fmod_search_mods = requests.get(f"https://api.modrinth.com/v2/search?query={fmod_search_query}&facets=[[%22project_type:mod%22]]&limit={fmod_search_limit}", headers=headers)
    file = open("data.txt", "w")
    file.write("")
    file.write(str(fmod_search_mods.json()))
    file.close()
    # Debug messages
    debug(f"Trying to request: https://api.modrinth.com/v2/search?query={fmod_search_query}&facets=[[%22project_type:mod%22]]&limit={fmod_search_limit}")

    # Response messages
    if fmod_search_mods.status_code == 200:
        debug("Request finished succesfully")
    else:
        critical_error("Something is wrong with the request")
    
    # Converting the response to json
    json_fmod_response = fmod_search_mods.json()
    hits = json_fmod_response["hits"]
    # Searching throught the response and adding it to the python dictionary
#addon_names = {}
#addon_project_ids = {}
#addon_downloads = {}
#addon_short_descriptions = {}
#addon_versions = {}
#addon_categories = {}
#addon_icon_url = {}
#addon_followers = {}
    count = -1
    for addon in tqdm(hits):
        count +=1
        addon_names[count] = addon["title"]
        addon_project_ids[count] = addon["project_id"]
        addon_downloads[count] = addon["downloads"]
        addon_short_descriptions[count] = addon["description"]
        addon_versions[count] = addon["versions"]
        addon_categories[count] = addon["categories"]
        addon_icon_url[count] = addon["icon_url"]
        addon_followers[count] = addon["follows"]
    debug(f"Total data length is: {len(addon_names)+len(addon_project_ids)+len(addon_downloads)+len(addon_short_descriptions)+len(addon_categories)+len(addon_icon_url)+len(addon_followers)}")

    print("\n",addon_names[1],"\n",addon_project_ids[1],"\n",addon_downloads[1],"\n",addon_short_descriptions[1],"\n",addon_versions[1],"\n",addon_categories[1],"\n",addon_icon_url[1],"\n",addon_followers[1],"\n")
elif chosen_action == "2":
    debug("Chosen Action 2", 1)

elif chosen_action.lower() == "c":
    print("Beggining color check...\n")
    sleep(0.2)
    # Color test
    for i in tqdm(range(10)):
        debug("This is what a debug text looks like", 1)
        sleep(0.3)
        critical_error("This is what critical error looks like")
        sleep(0.3)
        error("This is what error looks like")
        sleep(0.3)
        print()
    print("Color check completed")

elif chosen_action.lower() == "l":
    print("Beggining manual Labrinth API check...")
    # Labrinth check
    debug("Connecting to: https://api.modrinth.com/v2/statistics for statistics", 1)
    labrinth_status = requests.get("https://api.modrinth.com/v2/statistics")

    # Debug mode thingies
    if labrinth_status.status_code == 200:
        debug("Labrinth is working and it is avaible!", 1)
    else:
        critical_error("Labrinth is NOT working, stopping the app...")
        quit()
    # Convering labrinth status to json
    labrinth_status_json = labrinth_status.json()
    # Modrinth statictics
    print("")
    for i in labrinth_status_json:
        print(f"There are: {labrinth_status_json[i]} {i}")
    print("On Modrinth")