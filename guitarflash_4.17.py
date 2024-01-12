import pyautogui
import keyboard
from time import sleep

sleep(5)

while keyboard.is_pressed("1") == False:
    if not pyautogui.pixelMatchesColor(1091,814,(20,20,20)):
        pyautogui.press("a")
        sleep(0.1)

    if not pyautogui.pixelMatchesColor(1182,813,(20,20,20)):
        pyautogui.press("s")
        sleep(0.1)

    if not pyautogui.pixelMatchesColor(1271,814,(20,20,20)):
        pyautogui.press("j")
        sleep(0.1)
    if not pyautogui.pixelMatchesColor(1359,813,(20,20,20)):
        pyautogui.press("k")
        sleep(0.1)
    if not pyautogui.pixelMatchesColor(1449,814,(20,20,20)):
        pyautogui.press("l")
        sleep(0.1)