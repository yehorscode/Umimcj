import json
from m_step1 import debug, critical_error, error
import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
from tqdm import tqdm

# VERY IMPORTANT THINGIES
addon_slug = {}
addon_names = {}
addon_project_ids = {}
addon_downloads = {}
addon_short_descriptions = {}
addon_versions = {}
addon_categories = {}
addon_icon_url = {}
addon_followers = {}
addon_authors = {}

with open("./data/final_data.json", 'r') as final_file_file:
    data = json.loads(final_file_file.read())

# END OF VERY IMPORTANT THINGIES

thingy = "---------"
debug(thingy*2)
debug(f"Data load successful with {len(data)} entries")
debug(thingy*2)


# Importing data
count = 0
for i in tqdm(range(300)):
    try:
        addon_slug[count] = data[str(count)]["addon_slug"]
        addon_names[count] = data[str(count)]["addon_name"]
        addon_project_ids[count] = data[str(count)]["addon_project_id"]
        addon_downloads[count] = data[str(count)]["addon_downloads"]
        addon_short_descriptions[count] = data[str(count)]["addon_short_descriptions"]
        addon_versions[count] = data[str(count)]["addon_versions"]
        addon_categories[count] = data[str(count)]["addon_categories"]
        addon_icon_url[count] = data[str(count)]["addon_icon_url"]
        addon_followers[count] = data[str(count)]["addon_followers"]
        addon_authors[count] = data[str(count)]["addon_authors"]
        debug(f"Added {addon_names[count]} to addon_names and it is now {len(addon_names)} entries long")
        count += 1
    except KeyError:
        error("KeyError: ")
        critical_error("Something went wrong")
        count += 1

# WINDOW INFO
root = tk.Tk()
root.title("Addon Label Maker 3000")

# Function to load addon data into the window
def load_addon(index):
    try:
        # Get image URL
        url = addon_icon_url[index]
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((100, 100), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        # Update image
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Update short description
        short_desc_label.config(text=addon_short_descriptions[index])

        # Update addon name
        addon_name_label.config(text=addon_names[index])
    except Exception as e:
        error(f"Error loading addon data: {e}")
        critical_error("Something went wrong")

# Function to handle label submission
def submit_label():
    label = label_entry.get()
    debug(f"Label submitted: {label}")
    # Here you can handle the label (e.g., save it to a file or a database)

# Create and place widgets
image_label = tk.Label(root)
image_label.pack()

addon_name_label = tk.Label(root, text="Addon Name", font=("Arial", 16))
addon_name_label.pack()

short_desc_label = tk.Label(root, text="Short Description", wraplength=300)
short_desc_label.pack()

label_entry = tk.Entry(root)
label_entry.pack()

submit_button = tk.Button(root, text="Submit Label", command=submit_label)
submit_button.pack()

# Load the first addon
load_addon(0)

root.mainloop()
