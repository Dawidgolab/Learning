from tkinter import *
from center import center_window
from tkinter import messagebox


root = Tk()

# Modify the window
root.title("First GUI interface")
root.config(background='grey')
app_width = 500
app_height = 500
center_window(root, app_width, app_height)

def my_message_1(event):
    messagebox.showinfo(title="Event", message = "It works!")

def my_message_2(event):
    messagebox.showinfo(title="Event", message = "It works from the secound function!")

root.bind('<Button-1>',my_message_1) #This action works after click the screen
# we have e.g. <A> if we want it to work with the letter A 
root.bind("<a>",my_message_2, add="+") # this method help us to use the secound function after first one when the event is the same 

root.mainloop()