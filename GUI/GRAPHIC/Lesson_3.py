from tkinter import *


#create main screen
root = Tk()

#modify the window
root.title("First GUI interface")
root.config(background='grey')
root.geometry('500x500')

# another way to create a label
my_label = Label(root, text="This is my label")
my_label.pack()

my_label.config(
    background="light blue",
    fg="black",
    font=("Arial", 20),
    padx=20,
    pady=20
)


root.mainloop()


