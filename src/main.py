import pyautogui
import time
from bs4 import BeautifulSoup

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
timeout = time.time() + 75

with open("../data.txt", 'r') as dataFile:
    data = dataFile.read()

soup = BeautifulSoup(data, 'html.parser')

for i in range(10):
    print("{}/10".format(i + 1))
    time.sleep(1)

for i in soup.find_all('span'):
    pyautogui.typewrite(i.text + " ", pause=0.3, interval=0)
    print(i.text)
    if time.time() > timeout:
        break
