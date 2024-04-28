from tkinter import *
from tkinter import messagebox
from center import center_window
import datetime
from PIL import ImageTk, Image

root = Tk()

# Modify the window
root.title("First GUI interface")
root.config(background='grey')
app_width = 500
app_height = 500
center_window(root, app_width, app_height)




#Graph window
# img = ImageTk.PhotoImage(Image.open('landscape.jpg'))
img = Image.open('landscape.jpg')
img = img.resize((500, 100))
img = ImageTk.PhotoImage(img)

labelImage = Label(image=img)
labelImage.pack()






# Normal label 
my_label = Label(root, text="This is my label")
my_label.pack() #pack() - we use it in horizontal and vertical settings

my_label.config(
    background="light blue",
    fg="black",
    font=("Arial", 20),
    padx=20,
    pady=20
)




# warning/messagebox after click 
def display_prompt(msg):
    messagebox.showinfo(title = "Event", message = msg)

btn = Button(
    root, 
    text="Get info",
    padx = 20,
    pady = 10,
    command = lambda:display_prompt("It works")) # we use labda when we want to assign an argument to a function

btn.pack()




# function call with double click and key 'a'
def my_message_1(event):
    messagebox.showinfo(title="Event", message = "It works from message 1 as well!")

def my_message_2(event):
    messagebox.showinfo(title="Event", message = "It works from the secound function!")

root.bind('<Double-Button-1>',my_message_1) #This action works after double click the screen
# we have e.g. <A> if we want it to work with the letter A 
root.bind("<a>",my_message_2) 







#button time
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














img_bottom = Image.open('landscape.jpg')
img_bottom = img_bottom.resize((500, 100))
img_bottom = ImageTk.PhotoImage(img_bottom)

labelImage_bottom = Label(image=img_bottom)
labelImage_bottom.pack(side=BOTTOM) # Place the image label at the bottom of the window




root.mainloop()