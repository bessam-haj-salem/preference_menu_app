import tkinter as tk  # GUI create
# filedialog: picks the app, Text: display text
from tkinter import filedialog, Text
import os  # run the app
import subprocess
import sys


root = tk.Tk()
# create a list and append all the files created in it
apps = []

# this is the case where you open and dont add a file it will in save.txt text like that : ,,
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        # strip up all the empty spaces
        apps = [x for x in tempApps if x.strip()]


# initialdir: working place where we want navigate from


def addApp():
    # widget all the things attached to the frame (labels)
    for widget in frame.winfo_children():
        # destroy everything and attach the updated version of it
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    # give us the path  of the file
    print(filename)
    # looping over the apps
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# run the apps


def runApps():
    for app in apps:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, app])


#   some CSS on the GUI
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attach the canva
canvas.pack()
# attach divs to this canvas
frame = tk.Frame(root, bg="white")
# relx and rely  willput the div in  the  center
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# function for the button
# add buttons : fg: color of the text,
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
# attach the button
openFile.pack()
# NB: the root is the squeleton (in grey), the frame is the div inside
# add another button
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# loading tha app on the frame
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
# run the GUI interface
root.mainloop()

# save tht apps
with open('save.txt', 'w') as f:
    for app in apps:
        #  when you close the  file, it will all the apps created on the list
        f.write(app + ',')
