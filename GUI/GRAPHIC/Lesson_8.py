from tkinter import *
from center import center_window
import pyshorteners
from tkinter import messagebox


def shorten():
    shortener = pyshorteners.Shortener()
    shortUrl = shortener.tinyurl.short(longLabelEntry.get())
    print(shortLabelEntry.insert(0, shortUrl))
    print(shortUrl)




root = Tk()
root.title("First GUI interface")
root.config(bg='grey')
app_width = 500
app_height = 500
center_window(root, app_width, app_height)





longLabel = Label(root, text="Enter long URL",bg='grey',padx = 50)
longLabelEntry = Entry(root)
shortLabel = Label(root, text="Output shortened URL",bg='grey')
shortLabelEntry = Entry(root)
button = Button(root, text="Shorten URL",command=shorten)

longLabel.pack()
longLabelEntry.pack()
shortLabel.pack()
shortLabelEntry.pack()
button.pack(padx=20, pady=20)








root.mainloop()