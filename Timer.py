from tkinter import *

root = Tk()
root.title("Timer")
root.geometry("400x400")


def thing():
    my_label.config(text="hello")


login_btn = PhotoImage(file="calendar_ico.png")

my_label = Button(root, image=login_btn, command=thing, borderwidth=0)
my_label.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

mainloop()

import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox

root = tk.Tk()
time_now = datetime.now()
calendar = DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2)
calendar.pack()

def date_check():
    calendar_date = datetime.strptime(calendar.get(),"%m/%d/%y")
    if calendar_date > time_now:
        messagebox.showerror("Error", "Selected date must not exceed current date")
        calendar.set_date(time_now)
    root.after(100,date_check)

root.after(100,date_check)

root.mainloop()





# def clock():
#     hour = time.strftime("%H")
#     minute = time.strftime("%M")
#     second = time.strftime("%S")
#     day = time.strftime("%A")
#     am_pm = time.strftime("%p")
#
#     time_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm + " " + day)
#     time_label.after(1000, clock)
#
#
# time_label = Label(root, text="", font=("Helvetica", 12), fg="red", bg="black")
# time_label.pack()
#
# clock()
#
# root.mainloop()
