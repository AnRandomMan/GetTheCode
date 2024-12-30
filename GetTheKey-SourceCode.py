import platform
import subprocess  # imports
from tkinter import Tk, Text, Button

def close_app(): #function to close app
    root.quit()

result = subprocess.run(["wmic path softwarelicensingservice get OA3xOriginalProductKey"], capture_output=True, text=True) #get Win license key

root = Tk() #create a root thing
root.title("GetTheKey") #give name to root thing

text_widget = Text(root, height=5, width=50, wrap="Hi! :3") #make text widget
text_widget.pack(padx=10, pady=10)

if platform.system() == "Windows" and platform.release() == "10": #check if the system is good
    text_widget.insert("1.0", f"Key found! ({result.stdout})") # if it is then print key
else:
    text_widget.insert("1.0", f"Error! This program only works on Windows 10!")

text_widget.config(state="disabled") #this thing make You can't modify the result

close_button = Button(root, text="Nice!", command=close_app) #make a button that closes the popup

text_widget.pack(padx=10, pady=10) #pack everything
close_button.pack(pady=10)

root.mainloop() #make popup