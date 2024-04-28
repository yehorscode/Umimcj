from index import *
import json
import requests
from IPython.display import Image, display
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
import requests
from io import BytesIO

def display_image_from_url(image_url):
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    # Resize the image to 100x100 pixels
    resized_image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()
# Create the main window
root = tk.Tk()
root.title("Addon Confirmation App")

data = open("data/cert_data.json", 'r')
data = json.load(data)

manual_data = {}
current_addon_index = 0

def display_next_addon():
    global current_addon_index
    while current_addon_index < len(data):
        if data[str(current_addon_index)] == "No" or data[str(current_addon_index)] == "Maybe":
            display_addon_info(current_addon_index)
            current_addon_index += 1
            break  # Exit the loop after displaying an addon
        else:
            manual_data[current_addon_index] = "True"
            current_addon_index += 1
    else:
        root.quit()  # Quit the application when all addons are displayed

def confirm(i):
    print(f"Addon {i} confirmed")
    manual_data[i] = "True"  # Update manual_data directly here
    display_next_addon()

def reject(i):
    print(f"Addon {i} rejected")
    manual_data[i] = "False"  # Update manual_data directly here
    display_next_addon()

print(data)
def display_addon_info(i):
        # Clear previous content
        for widget in root.winfo_children():
            widget.destroy()

        # Addon Name
        addon_name = addon_names[i]
        addon_label = tk.Label(root, text=addon_name, font=("Arial", 16))
        addon_label.pack()

        # Addon Logo
        image_url = addon_icon_url[i]
        display_image_from_url(image_url)

        # Buttons
        confirm_button = tk.Button(root, text="Confirm", command=lambda: confirm(i))
        confirm_button.pack(side=tk.LEFT, padx=20)

        reject_button = tk.Button(root, text="Reject", command=lambda: reject(i))
        reject_button.pack(side=tk.RIGHT, padx=20)
# Display the first addon info initially
display_next_addon()

# Call main loop
root.mainloop()

# Assuming manual_data is a dictionary containing your data
with open("manual_data.json", 'w') as file:
    json.dump(manual_data, file)