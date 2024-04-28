from tkinter import *
from PIL import ImageTk, Image
from center import center_window
import datetime

root = Tk()

# Modify the window
root.title("First GUI interface")
root.config(background='grey')
app_width = 800
app_height = 800
center_window(root, app_width, app_height)

img = ImageTk.PhotoImage(Image.open('landscape.jpg'))
labelImage = Label(image=img)
labelImage.pack()

entry_w = Entry(root, width=50)
entry_w.pack()

def get_input(event):
    my_label = Label(root, text=entry_w.get())
    my_label.pack()

entry_w.bind("<Return>", get_input)









root.mainloop()