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
{Fore.CYAN}1. Modrinth Create Mod data gathering
2. Curseforge Create Mod data gathering
C. Color check
L. Labrinth status check{Fore.RESET}""")

# Action input
chosen_action = input(f"Input: ")

# Setting app an api
import selenium
from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common import by
driver = webdriver.Firefox()
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
# Action running
if chosen_action == "1":
    debug("Chosen Action 1")

    driver.get("https://www.curseforge.com/minecraft/search?page=1&pageSize=50&sortBy=relevancy&class=mc-mods&categories=create")
    sleep(5)

    with open('curseforge.html', 'w') as outfile:
        outfile.write(driver.page_source)

    driver.close()

    bs = BeautifulSoup(open("curseforge.html"), "html.parser")
    find_names = bs.findAll("span", "ellipsis")
    print(bs.find("span", "ellipsis"))
    print(find_names[1])
    with open('curseforge.txt', 'w') as outfile:
        outfile.write(str(find_names))

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