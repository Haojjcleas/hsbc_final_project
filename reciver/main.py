import cv2
import pyautogui
import numpy as np
from pyzbar.pyzbar import decode
import json
file_name = input("File name: ")
last_block = input("last_block index: ")
try:
    with open(f"./{file_name}.raw", "r") as fo:
        data_dict = json.load(fo)
except:
    pass
data_dict = {}
# Specify the region of the screen to capture (top left x, top left y, width, height)
region = (50, 50, 550, 550)
data = []

while True:
    # Capture a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Convert the screenshot to a numpy array
    frame = np.array(screenshot)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode the QR code
    decoded_objects = decode(gray)

    # Draw a rectangle on the frame
    cv2.rectangle(frame, (0, 0), (region[2], region[3]), (0, 255, 0), 2)

    # Print the decoded objects
    for obj in decoded_objects:
        print('Type: ', obj.type)
        data = obj.data.decode('utf-8').split(" ")
        print('Data: ', data)
        data_dict[data[0]] = data[1]


        # Display the frame
    cv2.imshow('QR Code Scanner', frame)

    # Wait for a while before the next screenshot

    # Close the window if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if data and data[0] == last_block:
        break

with open(f"./{file_name}.raw", "w") as fo:
    json.dump(data_dict, fo)
cv2.destroyAllWindows()

missing_block = []
for i in range(int(last_block)):
    try:
        data_dict[i]
    except KeyError:
        missing_block.append(str(i))
if missing_block:
    print(f"Missing blocks {', '.join(missing_block)}")
else:
    print("Success")
