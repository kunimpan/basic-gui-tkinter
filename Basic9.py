from tkinter import *

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)

def selectChoice():
    result = choice.get()
    if result == 1:
        root.config(bg="green")
    elif result == 2:
        root.config(bg="pink")
    else:
        root.config(bg="purple")

choice = IntVar()
# Radio button
Radiobutton(root, text="Green", value=1, variable=choice, command=selectChoice).grid(row=0, column=0)
Radiobutton(root, text="Pink", value=2, variable=choice, command=selectChoice).grid(row=0, column=1)
Radiobutton(root, text="Purple", value=3, variable=choice, command=selectChoice).grid(row=0, column=2)

root.mainloop()