import pyautogui
import keyboard
import time

print("Press 's' to start/stop autoclicking. Press 'q' to quit.")

clicking = False

while True:
    if keyboard.is_pressed("s"):
        clicking = not clicking 
        if clicking:
            print("Clicking:") 
        else: 
            print("Paused")
        time.sleep(0.3)  # debounce for toggle

    if keyboard.is_pressed("q"):
        print("Quitting.")
        break

    if clicking:
        pyautogui.click()
        time.sleep(0.1)  # change to adjust click speed

