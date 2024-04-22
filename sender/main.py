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
size = 2950
# Open the file in binary mode and read it
with open("main.py", 'rb') as file:
    binary_content = file.read()

# Convert the binary content to a string using base64 encoding
string_content = base64.b64encode(binary_content).decode('utf-8')

# Split the string content into chunks of 1000 characters
chunks = [string_content[i:i + size] for i in range(0, len(string_content), size)]

# Create a fullscreen window
window = tk.Tk()
i = 0
for chunk in chunks:
    print(f"\r{i}/{len(chunks)-1}\r")
    # Create the QR code
    qr = qrcode.QRCode(
            version=40,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=1,
    )
    qr.add_data(f"{i} {chunk}")
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
    if first:
        input("start?")
        first = False

    i += 1
    # Clear the window for the next QR code
    label.pack_forget()
cmd = ""
while cmd != "q":
    missing_blocks = [9988, 10135, 10200, 10233, 10251, 10284, 10303, 10330, 10384, 10412, 10501, 10536, 10559, 10622, 10628, 10638, 10653, 10696, 10814, 10828, 10850, 10855, 10961, 10967, 11034, 11077, 11108, 11156, 11186, 11246, 11308, 11312, 11459, 11473, 11475, 11489, 11586, 11604, 11715, 11717, 11855, 11930, 11982, 12058, 12108, 12271, 12318, 12348, 12355, 12358, 12390, 12420, 12427, 12510, 12539, 12591, 12620, 12621, 12660, 12717, 12749, 12763, 12771, 12810, 12829, 12876, 12903, 12917, 12950, 12953, 13029, 13035, 13059, 13077, 13133, 13214, 13221, 13228, 13244, 13283, 13292, 13313, 13319, 13532, 13570, 13624, 13685, 13762, 13822, 13824, 13853, 13883, 13902, 13988, 14034, 14039, 14059, 14061, 14072, 14107, 14148, 14157, 14164, 14168, 14210, 14232, 14268, 14320, 14382, 14399, 14434
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

