# Microsoft teams auto join bot
# Will let the user set the time to join and what meeting to join
# It will then use image recognition and analysis to find the current meeting and then click the join button
# Once in the join screen, it will make sure that the microphone is turned off and then join.
# By Melon-Bowl


import pyautogui
from datetime import datetime
from time import *


# Sets everything up ready for the rest of the code to run and offers the user the option to delay the start of the code
def setup():
    # Makes sure that the script can be stopped by mousing to the top left corner in case of emergency
    pyautogui.FAILSAFE = True

    current_time = datetime.now()
    current_timestamp = datetime.timestamp(current_time)
    print("\u001b[34;1mUNIX timestamp: \u001b[0m ", current_timestamp)
    print("\u001b[34;1mDate:\u001b[0m ", current_time.day, "/", current_time.month, "/", current_time.year) # Prints the current date
    print("\u001b[34;1mTime:\u001b[0m ", current_time.hour, ":", current_time.minute, ":", current_time.second) # Prints the current time

    # Takes inputs for the date, hour, minute and second of the meeting
    target_date = int(input("Please enter the \u001b[32;1mdate\u001b[0m of your meeting: "))
    target_hour = int(input("Please enter the \u001b[32;1mhour\u001b[0m of your meeting: "))
    target_minute = int(input("Please enter the \u001b[32;1mminute\u001b[0m of your meeting: "))
    target_second = int(input("Please enter the \u001b[32;1msecond\u001b[0m of your meeting: "))

    target_time = datetime(current_time.year, current_time.month, target_date, target_hour, target_minute, target_second) # Combines all of the previously taken inputs into a datetime object
    target_timestamp = datetime.timestamp(target_time)
    print("\n\u001b[34;1mUNIX timestamp: \u001b[0m ", target_timestamp)
    
    timestamp_difference = target_timestamp - current_timestamp
    print("\u001b[34;1mTimestamp difference: \u001b[0m", timestamp_difference)

    difference = target_time - current_time

    print("\nYour meeting will take place in\u001b[32;1m", difference, "\u001b[0m")
    print("The program will now await the meeting. Please \u001b[31;1mdo not stop the script from running\u001b[0m otherwise the meeting will not be joined.\n")
    
    sleep(difference.seconds) # Sleeps until the meeting is about to start

    print("\n\u001b[33;1mThe time has come. Now running script\u001b[0m\n")



# This function is responsible for opening the Teams app, then going to calendar and then to the correct lesson window
# It is basically the prerequisite to the join() function
def navigate():
    # Opens Teams
    pyautogui.press('winleft')
    sleep(2)
    pyautogui.typewrite('Teams')
    sleep(1.5)
    pyautogui.press('enter')
    sleep(2)

    # Gets to the Calendar and the current day and time
    pyautogui.hotkey('ctrl', '5')
    pyautogui.hotkey('alt', '.')
    pyautogui.hotkey('ctrl', 'alt', '1')
    sleep(1)
    pyautogui.hotkey('alt', '.')

    # # Finds the orange line which is the current time
    # sleep(1)
    # orange_line_loc = pyautogui.locateOnScreen('img/time_now.png')
    # pyautogui.click(orange_line_loc)


# This function is responsible for joining the meeting from the correct page (Teams >> Calendar >> Your lesson)
def join():

    sleep(2)
    # Finds the join button of the current meeting in the calendar and clicks it
    calendar_join_button = pyautogui.locateOnScreen('img/calendar_join.png')
    if calendar_join_button != None: # Checks if the button is found
        calendar_join_center = pyautogui.center(calendar_join_button)
        pyautogui.click(calendar_join_center)
    else: # If it isn't, then it searches with the inverse coloured image
        calendar_join_button = pyautogui.locateOnScreen('img/calendar_join2.png')
        calendar_join_center = pyautogui.center(calendar_join_button)
        pyautogui.click(calendar_join_center)


    sleep(2)

    # Makes sure that the mic is turned off
    mic = pyautogui.locateOnScreen('img/mic_on.png')

    if mic != None:
        mic_center = pyautogui.center(mic)
        pyautogui.click(mic_center)
    else:
        print("Mic is already off. Joining meeting.")


    sleep(1)

    # Finds the join now button and clicks it to join meeting
    join_button_loc = pyautogui.locateOnScreen('img/join_now.png')
    join_button_center = pyautogui.center(join_button_loc)
    pyautogui.click(join_button_center)

    current_time = datetime.now() # Gets the time again
    print("Meeting was joined at:")
    print("\u001b[34;1mTime:\u001b[0m ", current_time.hour, ":", current_time.minute, ":", current_time.second) # Prints the current time again


setup()
navigate()
join()
