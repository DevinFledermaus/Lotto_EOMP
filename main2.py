# Devin Fledermaus Class 1
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import random


# Creating the window
root = Tk()
root.geometry("950x700")
root.resizable(False, False)
root.title("Lottery")
root.config(bg="blue")


# Defining my buttons
# Play Button
def verify():
    try:
        root.destroy()
        import main2
    except:
        pass


def submit():
    root.destroy()
    import main3


# Clear Button
def clear():
    playsound("clear.mp3")
    spnbox1.delete(0, END)
    spnbox2.delete(0, END)
    spnbox3.delete(0, END)
    spnbox4.delete(0, END)
    spnbox5.delete(0, END)
    spnbox6.delete(0, END)


# Exit Button
def exit_btn():
    playsound("exit.mp3")
    msg_box = messagebox.askquestion("Termination", "Are you sure you want to terminate the program?")
    if msg_box == "yes":
        root.destroy()


# Label
lbl = Label(root, text="Please select your numbers between 1 and 49", font=("Arial", 20), bg="blue")
lbl.place(x=200, y=50)


# Spinboxes
spnbox1 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox1.place(x=50, y=120)
spnbox2 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox2.place(x=200, y=120)
spnbox3 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox3.place(x=350, y=120)
spnbox4 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox4.place(x=500, y=120)
spnbox5 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox5.place(x=650, y=120)
spnbox6 = Spinbox(root, from_=1, to=49, width=2, font=("Arial", 40))
spnbox6.place(x=800, y=120)


# Randomly Generated Lotto Numbers using Entries
num1 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num1.place(x=70, y=420)
num2 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num2.place(x=220, y=420)
num3 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num3.place(x=370, y=420)
num4 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num4.place(x=520, y=420)
num5 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num5.place(x=670, y=420)
num6 = Entry(root, width=2, font=("Arial", 40), state="readonly")
num6.place(x=820, y=420)


# Buttons
btn = Button(root, text="Play", width=10, bg="green", command=verify, borderwidth=5)
btn.place(x=290, y=300)
btn2 = Button(root, text="Play Again", width=10, bg="green", command=verify, borderwidth=5)
btn2.place(x=550, y=300)
claimbtn = Button(root, text="Claim Prize", width=10, bg="green", command=submit, borderwidth=5)
claimbtn.place(x=420, y=550)
clrbtn = Button(root, text="Clear", width=10, bg="green", command=clear, borderwidth=5)
clrbtn.place(x=150, y=550)
extbtn = Button(root, text="Exit", width=10, bg="green", command=exit_btn, borderwidth=5)
extbtn.place(x=700, y=550)


# Run Program
root.mainloop()
