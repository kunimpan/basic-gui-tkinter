from tkinter import *

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)
root.config(bg="blue")

# Create button
btn1 = Button(root, text="Button one")
btn1.pack(side=TOP)

btn2 = Button(root, text="Button two", bg="red", fg="white")
btn2.pack(side=LEFT)

btn3 = Button(root, text="Button three", bg="black", fg="white")
btn3.pack(side=RIGHT)

btn4 = Button(root, text="Button four", bg="green", fg="white", activebackground="red", activeforeground="green")
btn4.pack(side=BOTTOM)


root.mainloop()