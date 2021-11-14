# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui

def screenshot():
    # Take screenshot
    img = pyautogui.screenshot()
    # Convert to numpy array
    img = np.array(img)
    # Convert RGB to BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # Save image
    cv2.imwrite("screenshot.png", img)
screenshot()