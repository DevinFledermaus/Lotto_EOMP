# All the imports
from tkinter import *
from tkinter import messagebox
import requests

# Let's start with the design of the GUI
root = Tk()
root.title("Currency Converter")
root.geometry("700x500")
root.resizable(False, False)
root.config(bg="black")

value = IntVar()

# Retrieving the information from an external JSON file as a source of reference
conversion_rate = {}
try:
    information = requests.get('https://v6.exchangerate-api.com/v6/910ab09f145c5695a5228187/latest/USD')
    information_json = information.json()

    conversion_rate = information_json['conversion_rates']
except requests.exceptions.ConnectionError:
    messagebox.showerror("Error", "No internet connection. Please try again later.")


# Defining my Functions
# Defining my conversion button
def convert():
    try:
        information = requests.get('https://v6.exchangerate-api.com/v6/910ab09f145c5695a5228187/latest/USD')
        information_json = information.json()

        conversion_rate = information_json['conversion_rates']

        num = float(ent.get())
        print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
        ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
        lbl3['text'] = ans
    except (ValueError, requests.exceptions.ConnectionError):
        ent.delete(0, END)
        messagebox.showerror("Error", "Please enter digits")


# Defining my Clear Button
def clear():
    ent.delete(0, END)


# Defining my Exit Button
def btn_ext():
    msg = messagebox.askquestion("Terminating Program", "Are you sure you want to close the currency convertor app?")
    if msg == "yes":
        root.destroy()


# Labels
lbl1 = Label(root, text="Value (US):", font=("Arial", 20), bg="black", fg="gray")
lbl1.place(x=50, y=30)
lbl2 = Label(root, text="To:", font=("Arial", 20), bg="black", fg="gray")
lbl2.place(x=200, y=200)
lbl3 = Label(root, text="Converted to: ", font=("Arial", 20), bg="black", fg="gray")
lbl3.place(x=450, y=200)

# Entry
ent = Entry(root, textvariable=value, width=40, bg="yellow")
ent.place(x=200, y=40)

# Buttons
con_btn = Button(root, command=convert, text="Convert", font=("Arial", 15), width=5, bg="yellow", fg="black", borderwidth=5)
con_btn.place(x=300, y=350)
clrbtn = Button(root, command=clear, text="Clear", font=("Arial", 15), width=5, bg="yellow", fg="black", borderwidth=5)
clrbtn.place(x=100, y=350)
extbtn = Button(root, command=btn_ext, text="Exit", font=("Arial", 15), width=5, bg="yellow", fg="black", borderwidth=5)
extbtn.place(x=500, y=350)


# Listbox
convert_list = Listbox(root, width=10, bg="yellow")
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.place(x=300, y=100)

# Run Program
root.mainloop()
