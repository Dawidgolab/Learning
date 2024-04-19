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

def get_date():
    data = datetime.datetime.now()
    data_label = Label(root, text=data, fg="red")
    data_label.pack() 


btn = Button(root, 
    text="Get date",
    background = "pink",
    pady = 10,
    padx = 20,
    command=get_date)

btn.pack()









root.mainloop()
