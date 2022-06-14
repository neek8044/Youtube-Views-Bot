import os
import requests
import zipfile
import tkinter as tk
import tkinter.messagebox as msg

win = tk.Tk()
win.resizable(0,0)
win.title('Installer')
win.geometry('280x130')

cwd = os.getcwd() + '\\'

# Display message when installed
def message():
    msg.showinfo(title='Installer', message='Chromedriver installed in the local folder.')

# Call all the functions above
def setup():
    with zipfile.ZipFile(cwd + 'chromedriver_win32.zip', 'r') as zipped:
        zipped.extractall(cwd)
    message()

# Request driver 101
def get_latest():
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text
    
    # build the download url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
    
    # download and extract the zip file
    driver_zip = requests.get(download_url)
    open('chromedriver_win32.zip', 'wb').write(driver_zip.content)
    setup()

# Display window and buttons
lbl_1 = tk.Label(text='Download driver:').pack(pady=(4,0))
btn_1 = tk.Button(text='Get Latest', fg='white', bg='#108010', command=get_latest, padx=18, pady=6).pack(pady=1)
lbl_2 = tk.Label(text='Created by Neek8044', fg='magenta', pady=4).pack(side='bottom')

win.mainloop()