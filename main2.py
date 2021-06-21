# Devin Fledermaus Class 1
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import random
from datetime import datetime


# Creating the window
root = Tk()
root.geometry("950x700")
root.resizable(False, False)
root.title("Lottery")
root.config(bg="blue")

now = datetime.now()


# Defining my buttons
# Play Button
def roll():
    try:
        # Spinbox Error
        if int(spnbox1.get()) < 50 and int(spnbox2.get()) < 50 and int(spnbox3.get()) < 50 and int(spnbox4.get()) < 50 and int(spnbox5.get()) < 50 and int(spnbox6.get()) < 50:
            # generating random numbers
            playsound("roll.mp3")
            nums = list(range(1, 49))
            random.shuffle(nums)
            lotto_draw = nums[:6]
            # inserting the random numbers generated into the entry boxes
            # Inserting number into entry 1
            num1['state'] = "normal"
            num1.delete(0, END)
            num1.insert(0, lotto_draw[0])
            num1['state'] = "readonly"
            # Inserting number into entry 2
            num2['state'] = "normal"
            num2.delete(0, END)
            num2.insert(0, lotto_draw[1])
            num2['state'] = "readonly"
            # Inserting number into entry 3
            num3['state'] = "normal"
            num3.delete(0, END)
            num3.insert(0, lotto_draw[2])
            num3['state'] = "readonly"
            # Inserting number into entry 4
            num4['state'] = "normal"
            num4.delete(0, END)
            num4.insert(0, lotto_draw[3])
            num4['state'] = "readonly"
            # Inserting number into entry 5
            num5['state'] = "normal"
            num5.delete(0, END)
            num5.insert(0, lotto_draw[4])
            num5['state'] = "readonly"
            # Inserting number into entry 6
            num6['state'] = "normal"
            num6.delete(0, END)
            num6.insert(0, lotto_draw[5])
            num6['state'] = "readonly"

            # comparing the two lists
            my_list = (int(spnbox1.get()), int(spnbox2.get()), int(spnbox3.get()), int(spnbox4.get()), int(spnbox5.get()), int(spnbox6.get()))
            my_list1 = list(my_list)
            my_list2 = lotto_draw
            comparison = (set(my_list1).intersection(set(my_list2)))
            results = len(comparison)
            messagebox.showinfo("Winnings", "You have " + str(results) + " winning balls")
            prizes = {6: "10 000 000.00", 5: "8 584.00", 4: "2 384.00", 3: "100.50", 2: "20.00", 1: "0", 0: "0"}
            x = (prizes.get(results))

            # text file
            w = open("user_details.txt", "a+")
            w.write("The Lotto Numbers are: " + str(lotto_draw) + "\n" )
            w.write("Your Numbers are: " + str(my_list1) + "\n")
            w.write("prize is: R" + str(x) + "" + "&" + "\n")
            w.write("Lotto Played at: " + str(now) + "\n")
            w.close()

            # Winnings
            if results <= 1:
                playsound("wasted.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You do not win anything")
            elif results == 2:
                playsound("mr_bean_magic.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You win R20.00, Please refer to Godwin and Thapelo for your Winnings")
                msg = messagebox.askquestion("Claim Prize", "Do you want to claim your prize??")
                if msg == "yes":
                    claim()
            elif results == 3:
                playsound("mr_bean_magic.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You win R100.50, Please refer to Godwin and Thapelo for your Winnings")
                msg = messagebox.askquestion("Claim Prize", "Do you want to claim your prize??")
                if msg == "yes":
                    claim()
            elif results == 4:
                playsound("mr_bean_magic.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You win R2 384.00, Please refer to Godwin and Thapelo for your Winnings")
                msg = messagebox.askquestion("Claim Prize", "Do you want to claim your prize??")
                if msg == "yes":
                    claim()
            elif results == 5:
                playsound("mr_bean_magic.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You win R8 584.00, Please refer to Godwin and Thapelo for your Winnings")
                msg = messagebox.askquestion("Claim Prize", "Do you want to claim your prize??")
                if msg == "yes":
                    claim()
            else:
                playsound("joker_laugh.mp3")
                messagebox.showinfo("WINNINGS!!!!", " You WIN the Jackpot of R10 Million, Please refer to Godwin and Thapelo for your Winnings")
                msg = messagebox.askquestion("Claim Prize", "Do you want to claim your prize??")
                if msg == "yes":
                    claim()
        else:
            messagebox.showerror("ERROR", "Please enter the proper numbers")
    except ValueError:
        messagebox.showerror("Something Went Wrong", "Please enter only numbers")
    finally:
        btn["text"] = "ROLL Again"


def claim():
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
    num1['state'] = "normal"
    num1.delete(0, END)
    num1['state'] = "readonly"
    num2['state'] = "normal"
    num2.delete(0, END)
    num2['state'] = "readonly"
    num3['state'] = "normal"
    num3.delete(0, END)
    num3['state'] = "readonly"
    num4['state'] = "normal"
    num4.delete(0, END)
    num4['state'] = "readonly"
    num5['state'] = "normal"
    num5.delete(0, END)
    num5['state'] = "readonly"
    num6['state'] = "normal"
    num6.delete(0, END)
    num6['state'] = "readonly"


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
btn = Button(root, text="ROLL", width=10, bg="green", command=roll, borderwidth=5)
btn.place(x=420, y=300)
clrbtn = Button(root, text="Clear", width=10, bg="green", command=clear, borderwidth=5)
clrbtn.place(x=230, y=550)
extbtn = Button(root, text="Exit", width=10, bg="green", command=exit_btn, borderwidth=5)
extbtn.place(x=600, y=550)


# Run Program
root.mainloop()
