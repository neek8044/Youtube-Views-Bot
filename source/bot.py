import os, time
from colorama import Fore

try:
    from selenium import webdriver
except ImportError:
    print("• Installing selenium...")
    os.system("pip install --upgrade selenium >nul")
    print("• Selenium installed.")
    from selenium import webdriver


cwd = os.getcwd() # Gets current working directory path
browser = ""


while True:
    browser = input(f"{Fore.LIGHTYELLOW_EX}Enter browser (chrome / edge): {Fore.RESET}").lower()
    if browser == "edge" or browser == "chrome":
        print(f"Browser set to {Fore.LIGHTGREEN_EX}%s{Fore.RESET}" % browser.capitalize())
        break

if browser == 'chrome':
    driver_path = cwd + "\\chromedriver.exe"
else:
    driver_path = cwd + "\\edgedriver.exe"


if os.path.exists(driver_path): # Checks if a chromedriver is installed
    print(f"{Fore.LIGHTMAGENTA_EX}Created by Neek8044{Fore.RESET}\n")
    print("Make sure Chrome / Edge is installed with the latest update\n")
    video_url = input("Video URL: ")

    Loop = False
    while Loop:
        try:
            duration = int(input("Video Duration (seconds): ")) - 3
            Loop = True
        except:
            continue

    if browser.lower() == 'chrome':
        # Configuring drivers to work with C:\chromedriver.exe
        driver_1 = webdriver.Chrome(executable_path = cwd + "\\chromedriver.exe")
        driver_2 = webdriver.Chrome(executable_path = cwd + "\\chromedriver.exe")
        driver_3 = webdriver.Chrome(executable_path = cwd + "\\chromedriver.exe")
        driver_4 = webdriver.Chrome(executable_path = cwd + "\\chromedriver.exe")
    else:
        # Configuring drivers to work with C:\chromedriver.exe
        driver_1 = webdriver.Edge(executable_path = cwd + "\\edgedriver.exe")
        driver_2 = webdriver.Edge(executable_path = cwd + "\\edgedriver.exe")
        driver_3 = webdriver.Edge(executable_path = cwd + "\\edgedriver.exe")
        driver_4 = webdriver.Edge(executable_path = cwd + "\\edgedriver.exe")

    # Starts drivers
    driver_1.get(video_url)
    driver_2.get(video_url)
    driver_3.get(video_url)
    driver_4.get(video_url)

    while True:
        time.sleep(duration)
        driver_1.refresh()
        driver_2.refresh()
        driver_3.refresh()
        driver_4.refresh()


else: # If no driver can be found, show error.
    print(f"{Fore.LIGHTRED_EX}ERROR: No driver could be found in the current working directory.\nLaunch installer and restart the program.")


input(f"\n\n{Fore.LIGHTBLUE_EX}Press enter key to exit...{Fore.RESET}") # Keep the screen alive by waiting for any input
