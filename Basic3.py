from tkinter import *

# Create screen
root = Tk()

# Setting main screen
root.title("My program")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0, 0)
root.config(bg="pink")

# Show message
label1=Label(root) # Create lable1 and put it at root.
label1.config(text="Hello")
label1.config(font=("Arial", 30, "bold")) # font-name, size, style
label1.config(bg="red")
label1.config(fg="white")
label1.pack() # Show label1 at the top center.

# Show message(no use config)
label2=Label(root, text="Python", font=("Arial", 30, "bold"), bg="blue", fg="white") 
label2.pack()

label3=Label(root, text="Tkinter", font=("Arial", 30, "bold"), bg="green", fg="white") 
label3.pack()

label4=Label(root, text="GUI", font=("Arial", 30, "bold"), bg="black", fg="white") 
label4.pack()

root.mainloop()