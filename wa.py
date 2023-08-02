import pyautogui
import time


pyautogui.moveTo(1490,1054)
pyautogui.click()

for i in range(5):
    pyautogui.write("Maju Lo Sini")
    time.sleep(0.1)
    pyautogui.press("Enter")
