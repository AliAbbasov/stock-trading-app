import os
import re
from datetime import datetime
from tkinter.ttk import Combobox
from tkcalendar import *
from Buy import *


def raise_frame(frame):
    frame.tkraise()


def password_not_recognised():
    messagebox.askretrycancel(title="Error", message='Wrong password!')


def user_not_found():
    messagebox.askretrycancel(title="Error", message='User name is not found!')


def open_MainFrame():
    screen.destroy()
    exec(open('Main.py').read())


def register_user():
    username_info = username.get()
    password_info = password.get()
    full_name_info = full_name.get()
    date_of_birth_info = date_of_birth.get()
    country_info = country.get()

    if len(username_info) == 0 or len(password_info) == 0 or len(full_name_info) == 0 or len(country_info) == 0:
        messagebox.showerror("Error", "Please fill out the fields.")
    else:
        list_of_files = os.listdir("Users\\")
        for i in list_of_files:
            if username_info == i:
                messagebox.showerror("Error", "Username already exists")
            else:
                if len(password_info) < 8:
                    messagebox.showerror("Error", "Your input too short.Please enter more than 8 symbols.")
                else:
                    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                    if (regex.search(password_info) == None):
                        file = open("Users\\" + username_info, "w")
                        file.write(username_info + "\n")
                        file.write(password_info + "\n")
                        file.write("Full name: " + full_name_info + "\n")
                        file.write("Date of birth: " + date_of_birth_info + "\n")
                        file.write("Country: " + country_info + "\n")
                        file.close()
                        username_entry.delete(0, END)
                        password_entry.delete(0, END)
                        fullname_entry.delete(0, END)
                        Label(register_frame, text="Registration Success", fg="green", font=("calibri", 11)).pack()
                    else:
                        messagebox.showerror("Error", "Passwords is not accepted.")


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir("Users\\")

    if username1 in list_of_files:
        file1 = open("Users\\" + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            open_MainFrame()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    global register_frame

    register_frame = Frame(screen)
    register_frame.place(x=0, y=0, width=700, height=500)

    global username
    global full_name
    global password
    global date_of_birth
    global country
    global username_entry
    global password_entry
    global fullname_entry

    username = StringVar()
    password = StringVar()
    full_name = StringVar()
    date_of_birth = StringVar()
    country = StringVar()

    Label(register_frame, text="Please enter your information", bg="yellow", width="300", font=("Calibri", 13)).pack()
    Label(register_frame, text="").pack()

    Label(register_frame, text="Username:").pack()
    username_entry = ttk.Entry(register_frame, textvariable=username)
    username_entry.pack()

    Label(register_frame, text="Full Name(As it Appears in Your ID):").pack()
    fullname_entry = ttk.Entry(register_frame, textvariable=full_name)
    fullname_entry.pack()

    Label(register_frame, text="Password:").pack()
    password_entry = ttk.Entry(register_frame, show="*", textvariable=password)
    password_entry.pack()

    Label(register_frame, text="Date of birth:").pack()

    time_now = datetime.now()
    calendar = DateEntry(register_frame, width=12, foreground='white', borderwidth=2, textvariable=date_of_birth)
    calendar.pack()

    def date_check():
        calendar_date = datetime.strptime(calendar.get(), "%m/%d/%y")
        if calendar_date > time_now:
            messagebox.showerror("Error", "Selected date must not exceed current date")
            calendar.set_date(time_now)
        register_frame.after(100, date_check)

    register_frame.after(100, date_check)

    Label(register_frame, text="Country:").pack()
    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
                 "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "	Bahamas", "	Bahrain",
                 "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "	Benin", "Bhutan", "Bolivia",
                 "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
                 "Burundi", "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
                 "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
                 "Costa Rica", "Croatia", "Cuba", "Cyprus", "Denmark",
                 "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
                 "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France",
                 "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
                 "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary",
                 "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                 "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait",
                 "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
                 "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
                 "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
                 "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
                 "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
                 "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
                 "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea",
                 "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
                 "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Samoa", "San Marino", "Saudi Arabia",
                 "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                 "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
                 "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan",
                 "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
                 "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
                 "United Arab Emirates", "United Kingdom", "USA", "Uruguay", "Uzbekistan",
                 "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    Combobox(register_frame, value=countries, width=25, height=10, textvariable=country).pack()

    Label(register_frame, text="").pack()
    ttk.Button(register_frame, text="Register", width=10, command=register_user).pack()
    ttk.Button(register_frame, text='Home', width=10, command=register_frame.destroy).pack()


def login():
    login_frame = Frame(screen)
    login_frame.place(x=0, y=0, width=700, height=500)

    Label(login_frame, text="Please enter your credentials", bg="yellow", width="300", font=("Calibri", 13)).pack()
    Label(login_frame, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(login_frame, text="Username: ").pack()
    username_entry1 = ttk.Entry(login_frame, textvariable=username_verify)
    username_entry1.pack()
    Label(login_frame, text="").pack()
    Label(login_frame, text="Password: ").pack()
    password_entry1 = ttk.Entry(login_frame, show="*", textvariable=password_verify)
    password_entry1.pack()
    Label(login_frame, text="").pack()
    ttk.Button(login_frame, text="Login", width=10, command=login_verify).pack()
    ttk.Button(login_frame, text='Home', width=10, command=lambda: login_frame.destroy()).pack()


def main_screen():
    global screen
    screen = Tk()

    bgimage = PhotoImage(file=r"Pictures\Mega_Trade_Pic.png")
    Label(screen, image=bgimage).place(relwidth=1, relheight=1)

    screen.iconbitmap(r'Pictures\mega_trade.ico')
    screen.geometry("700x500")
    screen.title("Mega Trade App")
    Label(text="Welcome to Mega Trade", bg="yellow", width="300", font=("Calibri", 13)).pack()
    ttk.Button(text="Login", command=login).place(relx=0.45, rely=0.2)
    ttk.Button(text="Register", command=register).place(relx=0.45, rely=0.28)
    screen.mainloop()


main_screen()