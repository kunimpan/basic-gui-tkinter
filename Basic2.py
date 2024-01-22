#Create main display. (root)
from tkinter import *

root = Tk() # Create main windows.

root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200") # width x height + X axis + Y axis.
root.resizable(0, 0) # Set the size of the X-Y axis(0 1).
root.config(bg="pink") # Can use color name or color code.

root.mainloop() # Run program.