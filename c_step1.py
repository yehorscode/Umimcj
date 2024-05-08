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
        import cursepy
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
from cursepy import *

print(Fore.CYAN+"""\nWelcome User!
This is Umimcj - an app made to scan popular mod sites like Modrinth and Curseforge
Data gathered is converted into JSON file
This app want to find all of the possible Create Mod addons and put it on one easy web-site
Happy using!\n"""+Fore.RESET)

# VERY IMPORTANT VALUES!
url_get_findrequest = "https://api.curseforge.com/v1/mods/search"


headers = {
    'User-Agent': 'https://github.com/yehorscode/CreateAddons-Site (create-addons@proton.me)',
    'x-api-key': '$2a$10$R5io95EuQkiR/VinRayi2ONdTuSfW.xzZ9j/TKVDwZ8dN1V4j3b/e',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

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
{Fore.CYAN}1. Curseforge Create Mod data gathering
2. nothing
C. Color check
L. Labrinth status check (old thingy){Fore.RESET}""")

# Action input
chosen_action = input(f"Input: ")

# Setting app an api

# Action running
global addon_names
global addon_project_ids
global addon_downloads
global addon_short_descriptions
global addon_versions
global addon_categories
global addon_icon_url
global addon_url
global addon_authors
addon_names = {}
addon_project_ids = {}
addon_downloads = {}
addon_short_descriptions = {}
addon_versions = {}
addon_categories = {}
addon_icon_url = {}
addon_url = {}
addon_authors = {}

headers = {
  'Accept': 'application/json',
  'x-api-key': '$2a$10$R5io95EuQkiR/VinRayi2ONdTuSfW.xzZ9j/TKVDwZ8dN1V4j3b/e'
}

if chosen_action == "1":
    debug("Chosen Action 1")

    url_api = "https://api.curseforge.com/"

    debug(f"Trying to request: {url_api+'v1/mods/search/'}\n With given parameters: gameId=432, searchFilter=create, classId=6")

    fmod_search = requests.get(url_api+'v1/mods/search/', params={'gameId': 432,
                                                                  'searchFilter': 'create',
                                                                  'classId': 6}, headers=headers)



    # Debugging stuff
    if fmod_search.status_code == 200:
        debug("Curseforge is working and it is avaible! " + str(fmod_search.status_code))
    else:
        critical_error("Curseforge is NOT working, stopping the app...")
        critical_error(f"The error message was: {fmod_search.status_code}")

    # Actually doing the work it needs to do
    fmod_search = fmod_search.json()
    fmod_search = fmod_search["data"]
    print(len(fmod_search))
    print("---------")
    counter = -1
    for i in range(len(fmod_search)):
        addon_names[i] = fmod_search[i]["name"]
        addon_project_ids[i] = fmod_search[i]["id"]
        addon_downloads[i] = fmod_search[i]["downloadCount"]
        addon_short_descriptions[i] = fmod_search[i]["summary"]
        addon_versions[i] = fmod_search[i]["latestFiles"]
        addon_categories[i] = fmod_search[i]["categories"]
        addon_icon_url[i] = fmod_search[i]["logo"]["url"]
        addon_url[i] = fmod_search[i]["links"]["websiteUrl"]
        addon_authors[i] = fmod_search[i]["authors"]
    print("-----")

    r = requests.get(url_api+'v1/categories', params={
  'gameId': '432',
    }, headers = headers)

    print(r)

    with open('categories.json', 'w') as f:
        try:
            json.dump(r.json(), f)
        except:
            f.write(r.text)


    with open('fmod_search.json', 'w') as f:
        try:
            json.dump(fmod_search.json(), f)
        except:
            f.write(str(fmod_search))

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
    debug("Nothing here for a moment")