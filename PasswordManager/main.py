from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search():
    toFind = websiteEntry.get()
    found = False
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if toFind in data:
            email = data[toFind]["email"]
            password = data[toFind]["password"]
            messagebox.showinfo(title=toFind, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {toFind} exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e",
               "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
               "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "|"]
    password = []

    for i in range(10):
        password.append(random.choice(letters))
    for i in range(4):
        password.append(random.choice(numbers))
    for i in range(4):
        password.append(random.choice(symbols))
    random.shuffle(password)
    passW = "".join(password)
    passwordEntry.insert(0, passW)
    pyperclip.copy(passW)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def addPassword():

    website = websiteEntry.get()
    email = usernameEntry.get()
    password = passwordEntry.get()
    newData = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        isOk = messagebox.askokcancel(title=website, message="Is it ok to save?")

        if isOk:
            try:
                with open(file="data.json", mode="r") as file:
                    # reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(newData, file, indent=4)
            else:
                # Updating old data
                data.update(newData)
                with open(file="data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
passwordPicture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passwordPicture)
canvas.grid(row=0, column=1)

websiteTitle = Label(text="Website:", width=8)
websiteTitle.grid(row=1, column=0)

websiteEntry = Entry(width=35)
websiteEntry.grid(row=1, column=1, columnspan=2)
websiteEntry.focus()

searchButton = Button(text="Search", command=search, highlightthickness=0, width=13)
searchButton.grid(row=1, column=2)

usernameTitle = Label(text="Email/Username:")
usernameTitle.grid(row=2, column=0)

usernameEntry = Entry(width=35)
usernameEntry.grid(row=2, column=1, columnspan=2)
usernameEntry.insert(0, "bojanbojovic035@gmail.com")

passwordTitle = Label(text="Password:")
passwordTitle.grid(row=3, column=0)

passwordEntry = Entry(width=18)
passwordEntry.grid(row=3, column=1)

genPassword = Button(text="Generate Password", command=generatePassword, highlightthickness=0, width=13)
genPassword.grid(row=3, column=2)

add = Button(text="Add", command=addPassword, highlightthickness=0, width=36)
add.grid(row=4, column=1, columnspan=2)



window.mainloop()
