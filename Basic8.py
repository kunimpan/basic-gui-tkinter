from tkinter import *
import tkinter.messagebox

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)

def quitProgram():
    confirm = tkinter.messagebox.askquestion("Confrim", "Do you want to close the program ?")
    if confirm == "yes":
        root.destroy()
    else:
        pass
        

def showName():
    name = userName.get() # Get data form userName.
    if name == "":
        tkinter.messagebox.showerror("Detail", "Please fill in your name.") # title, content
    else:
        myText.delete(0, END) # Clear text(start, end).
        tkinter.messagebox.showinfo("Detail", "Users = " + name) # title, content



# Entry Widget
userName = StringVar() # This part keeps data from Entry Widget
myText=Entry(root, width=40, font=('Arial', 30), textvariable=userName) # Part display
myText.pack(padx=5, pady=10)
btnSave=Button(root, text="save", fg="white", bg="blue", command=showName)
btnSave.pack(ipadx=30, ipady=10)

# Create a button for exiting the program.
btnQuit = Button(root, text="Exit the program", fg="white", bg="purple", command=quitProgram)
btnQuit.pack(ipadx=30, ipady=10, pady=5)

root.mainloop()