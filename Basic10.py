from tkinter import *
from tkinter.filedialog import *
# Create screen.
root = Tk()

# Setting main screen.
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)

def selectFile():
    fileOpen=askopenfilename(title="Open file", initialdir="./", filetypes=(("Text Files", "*.txt"), ("All Files", "*"))) # initialdir is set location to open file.
    print(fileOpen)
    
btn1=Button(root, text="Select file", command=selectFile)
btn1.pack()
root.mainloop()