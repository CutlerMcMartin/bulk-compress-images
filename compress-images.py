from tkinter import Tk
from PIL import Image
import PIL
import os

copied_files = Tk().clipboard_get()
copied_files = copied_files.splitlines()
copied_files = list(filter(lambda x: (('.JPG' in x) or ('.jpg' in x)), copied_files))

for element in copied_files:
    print(element)
    img_file = Image.open(element)
    img_file.save(element, optimize=True, quality=40)