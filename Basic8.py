from tkinter import *

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)

def showName():
    name = userName.get() # Get data form userName.
    print(name)
    myText.delete(0, END) # Clear text(start, end).

# Entry Widget
userName = StringVar() # This part keeps data from Entry Widget
myText=Entry(root, width=40, font=('Arial', 30), textvariable=userName) # Part display
myText.pack(padx=5, pady=10)
btnSave=Button(root, text="save", fg="white", bg="blue", command=showName)
btnSave.pack(ipadx=30, ipady=10)

root.mainloop()