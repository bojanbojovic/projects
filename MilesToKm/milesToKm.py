from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.columnconfigure(index=5, weight=1)
window.rowconfigure(index=3, weight=1)

input = Entry(width=5)
input.grid(column=1, row=0)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="0")
label2.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=3, row=1)

label4 = Label(text="Miles")
label4.grid(column=3, row=0)

def buttonClicked():
    miles = int(input.get())
    km = int(miles * 1.6)
    label2.config(text=f"{km}")

button = Button(text="Calculate", command=buttonClicked)
button.grid(column=1, row=2)



window.mainloop()
