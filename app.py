import tkinter as tk  # GUI create
# filedialog: picks the app, Text: display text
from tkinter import filedialog, Text
import os  # run the app

root = tk.Tk()
#   some CSS on the GUI
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attach the canva
canvas.pack()
# attach divs to this canvas
frame = tk.Frame(root, bg="white")
# relx and rely  willput the div in  the  center
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add buttons : fg: color of the text,
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42")
# attach the button
openFile.pack()
# NB: the root is the squeleton (in grey), the frame is the div inside
# add another button
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42")
# run the GUI interface
# root.mainloop()
