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
    missing_blocks = [int(i) for i in input("missing block: ").split(",")]
    for idx, missing_block in enumerate(missing_blocks):
        chunk = chunks[idx]
        print(f"\r{idx}/{missing_block}/{len(missing_blocks)}\r")
        # Create the QR code
        qr = qrcode.QRCode(
                version=40,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=2,
                border=1,
        )
        qr.add_data(f"{idx} {chunk}")
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

