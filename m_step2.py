from PIL import Image
import requests
from io import BytesIO
from m_step1 import addon_icon_url
from playsound import *

playsound("/usr/share/sounds/freedesktop/stereo/suspend-error.oga")

def is_color_present_from_url(image_url, target_color):
    """
    Check if the given color is present in the image from URL.

    Args:
    image_url (str): The URL of the image.
    target_color (tuple): The RGB color to find (R, G, B).

    Returns:
    bool: True if the color is present, False otherwise.
    """
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        pixels = img.getdata()

        # Check each pixel
        for pixel in pixels:
            if pixel == target_color:
                return True
        return False
    else:
        print("Failed to download image.")
        return False
playsound("/home/yehors/Pobrane/sound.wav")
print(len(addon_icon_url))
colordata = {}
# Example usagee
for i in range(len(addon_icon_url)):
    image_url = addon_icon_url[i]
    target_color = (117, 148, 240)  # Red color in RGB

    if is_color_present_from_url(image_url, target_color):
        print("Color is present in the image. "+image_url)
        colordata[i] = "True"
    else:
        print("Color is not present in the image. "+image_url)
        colordata[i] = "False"

import json 
with open('colordata.json', 'w') as convert_file: 
     convert_file.write(json.dumps(colordata))

playsound("/usr/share/sounds/freedesktop/stereo/suspend-error.oga")