import time

from bs4 import BeautifulSoup
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

with open("data.txt", 'r') as dataFile:
    data = dataFile.read()

soup = BeautifulSoup(data, 'html.parser')

time.sleep(10)
timeout = time.time() + 70  # 5 minutes from now

for i in soup.find_all('span'):
    pyautogui.write(i.text + " ", pause=0.5)
    print(i.text)
    if time.time() > timeout:
        break
