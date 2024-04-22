# This is a sample Python script.
from time import sleep

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import qrcode
import base64

from PIL import ImageTk, Image
import tkinter as tk
import sys
first = True
size = 2800
# Open the file in binary mode and read it
with open("works.zip", 'rb') as file:
    binary_content = file.read()

# Convert the binary content to a string using base64 encoding
string_content = base64.b64encode(binary_content).decode('utf-8')

# Split the string content into chunks of 1000 characters
chunks = [string_content[i:i + size] for i in range(0, len(string_content), size)]

# Create a fullscreen window
window = tk.Tk()
i = 0
cmd = ""
while cmd != "q":
    missing_blocks = [14504, 14605, 14630, 14676, 14713, 14743, 14749, 14815, 14825, 14841, 15034, 15060, 15073, 15085, 15126, 15130, 15207, 15265, 15272, 15285, 15353, 15358, 15369, 15401, 15424, 15451, 15473, 15489, 15514, 15524, 15575, 15605, 15615, 15619, 15628, 15636, 15677, 15678, 15683, 15727, 15729, 15794, 15809, 15828, 15846, 15890, 15910, 15913, 15999, 16005, 16016, 16028, 16138, 16164, 16178, 16223, 16388, 16419, 16438, 16446, 16520, 16556, 16593, 16747, 16776
]
    for idx, missing_block in enumerate(missing_blocks):
        chunk = chunks[missing_block]
        print(f"\r{idx}/{missing_block}/{len(missing_blocks)}\r")
        # Create the QR code
        qr = qrcode.QRCode(
                version=40,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=2,
                border=1,
        )
        qr.add_data(f"{missing_block} {chunk}")
        qr.make(fit=True)

        # Generate the image
        img = qr.make_image(fill='black', back_color='white')

        # Convert the QR code to a Tkinter-compatible image
        tk_image = ImageTk.PhotoImage(img)

        # Create a label and add the image to it
        label = tk.Label(window, image=tk_image)
        label.pack()

        # Display the window and wait for a short period
        window.update_idletasks()
        window.update()
        # window.after(round(1000/100))  # wait for 1 second

        # Clear the window for the next QR code
        label.pack_forget()
    cmd = input("finished?")

# Close the window
window.destroy()

