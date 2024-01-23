from tkinter import *

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)
root.config(bg="green")

# Create frame
frame1=Frame(root, bg="pink")
frame2=LabelFrame(root, text="Frame Title") # This frame has a label.

# Show frame
frame1.pack(fill=BOTH, expand=True)
Button(frame1, text="Button 1").pack()
Button(frame1, text="Button 2").pack()
Button(frame1, text="Button 3").pack()

frame2.pack(fill=BOTH, expand=True)
Button(frame2, text="Button 4").grid(row=0, column=0)
Button(frame2, text="Button 5").grid(row=0, column=1)
Button(frame2, text="Button 6").grid(row=0, column=3)

root.mainloop()