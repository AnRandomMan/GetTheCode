import platform
import subprocess
from tkinter import Tk, Text, Button
def close_app():
    root.quit()
result = subprocess.run(["wmic path softwarelicensingservice get OA3xOriginalProductKey"], capture_output=True, text=True) #get Win license key
root = Tk()
root.title("GetTheKey")
text_widget = Text(root, height=5, width=50, wrap="Hi! :3")
text_widget.pack(padx=10, pady=10)
if platform.system() == "Windows" and platform.release() == "10":
    text_widget.insert("1.0", f"Key found! ({result.stdout})")
else:
    text_widget.insert("1.0", f"Error! This program only works on Windows 10!")
text_widget.config(state="disabled")
close_button = Button(root, text="Nice!", command=close_app)
text_widget.pack(padx=10, pady=10)
close_button.pack(pady=10)
root.mainloop()