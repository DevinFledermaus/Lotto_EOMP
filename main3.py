# Devin Fledermaus Class 1
import tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import requests
from datetime import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Creating the window
root = Tk()
root.geometry("700x800")
root.resizable(False, False)
root.title("Banking Details")
root.config(bg="blue")

now = datetime.now()


class BankDetails:

    def __init__(self, window):
        # Labels
        self.lbl1 = Label(window, text="Banking Details", font=("Arial", 30))
        self.lbl1.place(x=200, y=30)
        self.lbl2 = Label(window, text="Account Holder Name", font=("Arial", 15))
        self.lbl2.place(x=50, y=100)
        self.lbl3 = Label(window, text="Account number", font=("Arial", 15))
        self.lbl3.place(x=50, y=150)
        self.lbl4 = Label(window, text="Bank", font=("Arial", 15))
        self.lbl4.place(x=50, y=200)
        # Entries
        self.ent1 = Entry(root, width=30)
        self.ent1.place(x=300, y=100)
        self.ent2 = Entry(root, width=30)
        self.ent2.place(x=300, y=150)
        self.ent3 = Entry(root, width=20)
        self.ent3.place(x=150, y=500)
        self.ent4 = Entry(root, width=20)
        self.ent4.place(x=150, y=650)
        # OptionMenu
        self.default_txt = "Select Bank"
        self.default_var = tkinter.StringVar(value=self.default_txt)
        self.optmenu = OptionMenu(root, self.default_var, "Absa Bank", "Capitec Bank", "Standard Bank", "First National Bank")
        self.optmenu.place(x=300, y=200)
        # Buttons
        self.btn = Button(root, text="Submit", width=5, bg="green", command=self.check, borderwidth=5)
        self.btn.place(x=300, y=320)
        self.clrbtn = Button(root, text="Clear", width=5, bg="green", command=self.clear, borderwidth=5)
        self.clrbtn.place(x=150, y=320)
        self.extbtn = Button(root, text="Exit", width=5, bg="green", command=self.exit_btn, borderwidth=5)
        self.extbtn.place(x=450, y=320)
        self.conbtn = Button(root, text="Convert", width=16, bg="green", command=self.convert, borderwidth=5)
        self.conbtn.place(x=150, y=570)
        # Retrieving the information from an external JSON file as a source of reference
        self.conversion_rate = {}
        try:
            self.information = requests.get('https://v6.exchangerate-api.com/v6/910ab09f145c5695a5228187/latest/ZAR')
            information_json = self.information.json()

            self.conversion_rate = information_json['conversion_rates']
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "No internet connection. Please try again later.")
        # Listbox
        self.convert_list = Listbox(root, width=15, bg="white")
        for i in self.conversion_rate.keys():
            self.convert_list.insert(END, str(i))
            self.convert_list.place(x=370, y=500)

    # Defining the buttons
    # Defining my conversion button
    def convert(self):
        try:
            information = requests.get('https://v6.exchangerate-api.com/v6/910ab09f145c5695a5228187/latest/ZAR')
            information_json = information.json()

            conversion_rate = information_json['conversion_rates']

            num = float(self.ent3.get())
            ans = num * information_json['conversion_rates'][self.convert_list.get(ACTIVE)]
            self.ent4.delete(0, END)
            self.ent4.insert(0, ans)
        except (ValueError, requests.exceptions.ConnectionError):
            self.ent3.delete(0, END)
            self.ent4.delete(0, END)
            messagebox.showerror("Error", "Please enter digits")

    # Sending my email
    def verify(self):
        file_to_read = "user_details.txt"
        file = open(file_to_read, "r")
        list_file = file.readline()

        email_list = str(list_file)

        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email_list)
        email = emails[-1]

        sender_email_id = 'd.e.fledermaus86@gmail.com'
        receiver_email_id = str(emails[-1])
        password = input("Enter your password: ")
        subject = "Greetings"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "This is my attempt at sending to multiple recipients\n"
        body = body + "Hope this works"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(sender_email_id, password)
        print(receiver_email_id)

        # message to be sent

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, text)

        # terminating the session
        s.quit()

    # Defining the submit button
    def check(self):

        sel = self.ent1.get()
        sel2 = self.ent2.get()

        # text file
        w = open("user_details.txt", "a+")
        w.write("Account Holder Name: " + str(sel) + "," + " " + "Account Number: " + str(sel2) + "," + " " + "Bank: " + self.default_var.get() + " " + "&" + " " + "Winnings Claimed at: " + str(now) + "\n")
        w.close()

        # Account holder error
        if not sel.isalpha():
            messagebox.showerror('Account Holder Name', 'Please make sure account holder name is entered correctly')

        # Account number error
        elif not sel2.isdigit():
            messagebox.showerror('Account Number', 'Please make sure account number is entered correctly')

        # No Bank selected error
        elif self.default_var.get() == "Select Bank":
            messagebox.showerror('Bank', 'Please select a bank')
        else:
            self.verify()

    # Defining my clear button
    def clear(self):
        playsound("clear.mp3")
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.default_var.set(self.default_txt)

    # Defining my exit button with messagebox
    def exit_btn(self):
        playsound("exit.mp3")
        msg = messagebox.askquestion("Termination", "Are you sure you want to close the program?")
        if msg == "yes":
            root.destroy()


obj_BankDetails = BankDetails(root)


# Run Program
root.mainloop()
