from tkinter import *
from center import center_window
import datetime

root = Tk()

# Modify the window
root.title("First GUI interface")
root.config(background='grey')
app_width = 500
app_height = 500
center_window(root, app_width, app_height)





root.mainloop()