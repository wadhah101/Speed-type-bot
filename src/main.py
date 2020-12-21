import pyautogui
import time
from bs4 import BeautifulSoup

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def write_text(timeout, pause, interval):
    with open("../data.txt", 'r') as dataFile:
        data = dataFile.read()

    soup = BeautifulSoup(data, 'html.parser')

    for i in range(10):
        print("{}/10".format(i + 1))
        time.sleep(1)

    for i in soup.find_all('span'):
        pyautogui.typewrite(i.text + " ", pause=pause, interval=interval)
        print(i.text)
        if time.time() > timeout:
            break


if __name__ == "__main__":
    write_text(time.time() + 75, 0.3, 0)
