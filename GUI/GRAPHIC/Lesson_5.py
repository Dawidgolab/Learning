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

def display_prompt(msg):
    messagebox.showinfo(title = "Event", message = msg)

btn = Button(
    root, 
    text="Get info",
    padx = 20,
    pady = 10,
    command = lambda:display_prompt("It works")) # we use labda when we want to assign an argument to a function

btn.pack()








root.mainloop()