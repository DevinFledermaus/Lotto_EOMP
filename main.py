# Devin Fledermaus Class 1
import uuid
from tkinter import *
from tkinter import messagebox
import re
from datetime import date, datetime
from playsound import playsound
from uuid import uuid4


# Creating the window
root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Login Page")
root.config(bg="blue")

now = datetime.now()


# Defining my button commands
# Enter Button
def next_window():
    root.destroy()
    import main2


# Verifying Age
def age_check():
    # player ID
    player_id = uuid.uuid4()

    # text file
    w = open("user_details.txt", "a+")
    w.write(ent1.get() + " " + " " + ent2.get() + " " + " " + ent3.get() + " " + " " + "Player-ID: " + str(player_id) + " " + " " + "Logged in at " + str(now) + "\n")
    w.close()

    id_num = ent3.get()
    year = id_num[:2]
    if year >= "22":
        year = "19" + year
    else:
        year = "20" + year
    month = id_num[2:4]
    day = id_num[4:6]
    dob = year, month, day
    today = date.today()
    age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
    if age >= 18:
        playsound("enter.mp3")
        messagebox.showinfo("Status Feedback", "Let's Play")
        next_window()
    elif age < 18:
        messagebox.showerror("ERROR", "You are too young bud, try again next year")


def enter():
    # variables
    idnum = ent3.get()
    email_ad = ent2.get()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # conditions
    if ent1.get() == "":
        playsound("sheesh_falcetto.mp3")
        messagebox.showerror("ERROR", "Please enter your name")
    elif len(ent3.get()) > 13 or len(ent3.get()) < 13:
        playsound("sheesh_falcetto.mp3")
        messagebox.showerror("ERROR", "ID Number must contain 13 numbers")
    elif not idnum.isdigit():
        playsound("sheesh_falcetto.mp3")
        messagebox.showerror("ERROR", "ID Number only contains numbers")
    elif not re.search(regex, email_ad):
        playsound("sheesh_falcetto.mp3")
        messagebox.showerror("ERROR", "Please check if the email is correct")
    else:
        age_check()


# Defining My Clear Button
def clear():
    playsound("clear.mp3")
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)


# Defining my Exit Button
def exit_btn():
    playsound("exit.mp3")
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# Labels
img = PhotoImage(file="index.png")
Label(root, image=img).place(x=360, y=10)
lbl1 = Label(root, text="Full Name", bg="blue", font=("Arial", 20))
lbl1.place(x=115, y=200)
lbl2 = Label(root, text="Email Address", bg="blue", font=("Arial", 20))
lbl2.place(x=440, y=200)
lbl3 = Label(root, text="ID Number", bg="blue", font=("Arial", 20))
lbl3.place(x=290, y=300)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=50, y=240)
ent2 = Entry(root, width=30)
ent2.place(x=400, y=240)
ent3 = Entry(root, width=30)
ent3.place(x=230, y=340)


# Buttons
btn = Button(root, text="Enter", width=10, bg="green", command=enter, borderwidth=5)
btn.place(x=300, y=430)
clrbtn = Button(root, text="Clear", width=10, bg="green", command=clear, borderwidth=5)
clrbtn.place(x=100, y=430)
extbtn = Button(root, text="Exit", width=10, bg="green", command=exit_btn, borderwidth=5)
extbtn.place(x=500, y=430)


# Run Program
root.mainloop()

