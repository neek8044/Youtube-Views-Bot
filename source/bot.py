import os
from time import sleep
from random import randint
from colorama import Fore

os.system('cls')

cwd = os.getcwd() # Gets current working directory path
driver_path = cwd + '\chromedriver.exe' # Sets local driver path

if os.path.exists(driver_path): # Checks if a chromedriver is installed
    try:
        from selenium import webdriver
    except ImportError:
        print("• Installing selenium...")
        os.system('pip install --upgrade selenium >nul')
        print("• Selenium installed.")
        from selenium import webdriver

    ###################################

    print(f'{Fore.MAGENTA}Created by Neek8044{Fore.RESET}\n')
    #print('Make sure Google Chrome is installed with the latest update\n')
    video_url = input("Video URL: ")

    # Configuring drivers to work with C:\chromedriver.exe
    driver_1 = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver_2 = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver_3 = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver_4 = webdriver.Chrome(executable_path="C:\chromedriver.exe")

    # Starts drivers
    driver_1.get(video_url)
    driver_2.get(video_url)
    driver_3.get(video_url)
    driver_4.get(video_url)

    while True:
        sleep(randint(10,15))
        driver_1.refresh()
        driver_2.refresh()
        driver_3.refresh()
        driver_4.refresh()

else: # If any chromedriver cannot be found, show error.
    print(f'{Fore.LIGHTRED_EX}ERROR: Chromedriver not found in the current working directory.\nLaunch installer and restart the program.')
input() # Keep the screen alive by waiting for any input