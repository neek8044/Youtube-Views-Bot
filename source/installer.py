import os
import requests
import zipfile
import webbrowser
import tkinter as ttk
import tkinter.messagebox as msg


win = ttk.Tk()
win.resizable(0,0)
win.title('Installer')
win.geometry('280x130')

cwd = os.getcwd() + '\\'


# Display message when installed
def message(browser:str):
    msg.showinfo(title='Installer', message='%sdriver installed in the local folder.' % browser)


# Call all the functions above
def setup():
    with zipfile.ZipFile(cwd + 'chromedriver_latest.zip', 'r') as zipped:
        zipped.extractall(cwd)
    message("Chrome")


# Request chrome driver
def chrome():
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text
    
    # build the download url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_latest.zip"
    
    # download and extract the zip file
    driver_zip = requests.get(download_url)
    open('chromedriver_latest.zip', 'wb').write(driver_zip.content)
    setup()


# Request edge driver
def edge():
    # open new tab
    webbrowser.open("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")

# Display window and buttons
lbl_1 = ttk.Label(text = 'Download driver:')
lbl_1.pack(pady = (4,0))

btn_1 = ttk.Button(text = 'Chrome [auto download]', fg = 'white', bg = '#30b030', command = chrome, padx = 18, pady = 6)
btn_1.pack(pady = 1)
btn_1 = ttk.Button(text = 'Edge [open link]', fg = 'white', bg = '#30b030', command = edge, padx = 18, pady = 6)
btn_1.pack(pady = 1)

lbl_2 = ttk.Label(text = 'Created by Neek8044', fg = 'magenta', pady = 4)
lbl_2.pack(side = 'bottom')

win.mainloop()
