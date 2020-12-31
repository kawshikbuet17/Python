#pip install pyautogui
import pyautogui
import time 

cnt = 0
while True:
    time.sleep(3)
    pyautogui.typewrite('Happy New Year 2021, times ' + str(cnt))
    cnt+=1
    pyautogui.press('enter')


#keep your cursor there where to type your automated message