from tkinter import *

#create main screen
root = Tk()

#modify the window
root.title("First GUI interface")
root.geometry("500x500")

# launch loop
# root.mainloop()

# create the frame as a container for the other widgets
app = Frame(root)
app.grid()

# label in the frame
lbl = Label(app, text= "I'm Label")
lbl.grid()


#Buttons
button1 = Button(app , text="I'm doing nothing")
button1.grid()

button2 = Button(app)
button2.grid()

# modify the value 
button2.configure(text="i'm doing nothing too")

button3 = Button(app)
button3.grid()

button3["text"] = "This is the same"
root.mainloop()