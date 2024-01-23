from tkinter import *  
from PIL import ImageTk, Image # pip install pillow

# Create screen.
root = Tk()

# Setting main screen.
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)

# Read image

img1=ImageTk.PhotoImage(Image.open("image/programmer.png"))
Label(root, image=img1).pack()

root.mainloop()