# Devin Fledermaus Class 1
import tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound


# Creating the window
root = Tk()
root.geometry("500x400")
root.resizable(False, False)
root.title("Banking Details")
root.config(bg="blue")


# Defining the buttons
def verify():
    pass


def check():
    sel = ent1.get()
    sel2 = ent2.get()

    if not sel.isalpha():
        messagebox.showerror('Account Holder Name', 'Please make sure account holder name is entered correctly')

    elif not sel2.isdigit():
        messagebox.showerror('Account Number', 'Please make sure account number is entered correctly')

    elif default_var.get() == "Select Bank":
        messagebox.showerror('Bank', 'Please select a bank')


def clear():
    playsound("clear.mp3")
    ent1.delete(0, END)
    ent2.delete(0, END)
    default_var.set(default_txt)


def exit_btn():
    playsound("exit.mp3")
    msg = messagebox.askquestion("Termination", "Are you sure you want to close the program?")
    if msg == "yes":
        root.destroy()


# Labels
lbl1 = Label(root, text="Banking Details", font=("Arial", 30))
lbl1.place(x=100, y=30)
lbl2 = Label(root, text="Account Holder Name", font=("Arial", 12))
lbl2.place(x=50, y=100)
lbl3 = Label(root, text="Account number", font=("Arial", 12))
lbl3.place(x=50, y=150)
lbl4 = Label(root, text="Bank", font=("Arial", 12))
lbl4.place(x=50, y=200)


# Entries
ent1 = Entry(root, width=20)
ent1.place(x=250, y=100)
ent2 = Entry(root, width=20)
ent2.place(x=250, y=150)


# OptionMenu
default_txt = "Select Bank"
default_var = tkinter.StringVar(value=default_txt)
optmenu = OptionMenu(root, default_var, "Absa Bank", "Capitec Bank", "Standard Bank", "First National Bank")
optmenu.place(x=250, y=200)


# Buttons
btn = Button(root, text="Submit", width=5, bg="green", command=check, borderwidth=5)
btn.place(x=220, y=300)
clrbtn = Button(root, text="Clear", width=5, bg="green", command=clear, borderwidth=5)
clrbtn.place(x=50, y=300)
extbtn = Button(root, text="Exit", width=5, bg="green", command=exit_btn, borderwidth=5)
extbtn.place(x=380, y=300)


# Run Program
root.mainloop()
