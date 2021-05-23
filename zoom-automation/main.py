import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser

print("""
    
 __    __                                                                  .__  .__ 
|  | _|  | ________           ____________   ____   _____             ____ |  | |__|
|  |/ /  |/ /\____ \   ______ \___   /  _ \ /  _ \ /     \   ______ _/ ___\|  | |  |
|    <|    < |  |_> > /_____/  /    (  <_> |  <_> )  Y Y  \ /_____/ \  \___|  |_|  |
|__|_ \__|_ \|   __/          /_____ \____/ \____/|__|_|  /          \___  >____/__|
     \/    \/|__|                   \/                  \/               \/         

    """)


keyboard = Controller()

isStarted = False

for i in lst:
    currentMeeting = i[3]
    currentStart = i[1]
    currentEnd = i[2]
    print()
    print("Current Meeting : " + currentMeeting)
    print("Current Meeting Start : " + currentStart)
    print("Current Meeting End : " + currentEnd)
    
    while True:
        
        if isStarted == False:
            if datetime.now().hour >= int(i[1].split(':')[0]) and datetime.now().minute >= int(i[1].split(':')[1]):
                if datetime.now().hour <= int(i[2].split(':')[0]) and datetime.now().minute <= int(i[2].split(':')[1]):
                    webbrowser.open(i[0])
                    isStarted = True
                    print("Meeting Started ... (" + i[3] +")\n")  
                    print()
                else:
                    break
            else:
                break

        elif isStarted == True:
            if datetime.now().hour >= int(i[2].split(':')[0]) and datetime.now().minute >= int(i[2].split(':')[1]):
                keyboard.press('w')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False
                print("Meeting Ended ...(" + i[3] +")\n")
                print()
                break
