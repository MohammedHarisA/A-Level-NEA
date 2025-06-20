from tkinter import *
import sqlite3
from tkinter import messagebox
from Classes import MyButtons


# Create window.
window = Tk()
window.title("Log In page.")
icon = PhotoImage(file='OIP.png')
window.iconphoto(True,icon)
window.minsize(1450, 750) # Set parameters for window size.
window.rowconfigure(0,weight = 1)
window.columnconfigure(0, weight= 1)
window.state('zoomed')

my_buttons = MyButtons(window)
# Create Frames and grid.

LogInFrame = Frame(window, background = '#4FA8F0' )
RegisterFrame = Frame(window, background = '#4FA8F0')

for frame in (LogInFrame, RegisterFrame):
    frame.grid(row=0, column = 0, sticky = 'nsew')

# Code that will show the appropriate frame.
def showframe(frame):
    frame.tkraise()

showframe(LogInFrame) # Original frame.

###### Database variabes ######
Email = StringVar()
FullName = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()

# ============ LOGIN DATABASE CONNECTION =========
conn = sqlite3.connect('Client_info.db')
cur = conn.cursor()
print("Database connected successfully.")

cur.execute("""CREATE TABLE IF NOT EXISTS Client_info(Email TEXT PRIMARY KEY,
            FullName TEXT, 
            Password TEXT, 
            ConfirmPassword TEXT)""")

print("Table Created Successfully")



conn.commit()
conn.close()

# =================================================
# Checks if email and passwork are correct.
def login():
    conn = sqlite3.connect("Client_info.db")
    cursor = conn.cursor()

    find_user = 'SELECT * FROM Client_info WHERE Email = ? and Password = ?'
    cursor.execute(find_user, [(email_entry.get().lower()), (password_entry1.get())])

    result = cursor.fetchall()
    
    # If statement to indicate if login has been successful.
    
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
        print(result)

        with open("datafile.txt", "w") as file:
            file.write(f"{email_entry.get().lower()}")
        
        # Call main.py file as subprocess.
        from subprocess import call
        call(["python", "main.py"])
        

    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")


# ***********************************************Log In Page *****************************************************
#Create the individual frames for the login page and place.
Login_frame1 = Listbox(LogInFrame, bg = '#038DFF', width = 115, height = 50, highlightthickness=0, borderwidth=0)
Login_frame2 = Listbox(LogInFrame, bg='#67B6F7', width = 115, height = 50, highlightthickness=0, borderwidth=0)
Login_frame3 = Listbox(LogInFrame, bg='#4FA8F0', width = 100, height = 33, highlightthickness=0, borderwidth=0)
Login_frame4 = Listbox(LogInFrame, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)

Login_frame1.place(x=0,y=0)
Login_frame2.place(x= 676,y= 0)
Login_frame3.place(x=75,y= 106)
Login_frame4.place(x=676,y=106)

image1 = PhotoImage(file='Coverphoto1.png')
Label(Login_frame3, image=image1).place(x= 70, y= 35)

# ====== E-mail Entry box and Label ==========
email_entry = Entry(Login_frame4,fg="Black",font=("Helvetica", 12),highlightthickness=1,textvariable=Email )

email_entry.place(x=134, y=170, width=256, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_entry.insert(0,"e.g. hello123@gmail.com")
email_label = Label(Login_frame4, text='* Email / Username', fg="#89898b", bg='#f8f8f8', font=("Helvetica", 11, 'bold'))
email_label.place(x=130, y=140)

# ==== Password Entry Box and Label ==================
password_entry1 = Entry(Login_frame4, fg="Black",
                        font=("Helvetica", 12),
                        show='*',
                        highlightthickness=1,
                        textvariable=Password)

password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")

password_label = Label(Login_frame4, text='* Password',
                       fg="#89898b", bg='#f8f8f8',
                       font=("Helvetica", 11, 'bold'))

password_label.place(x=130, y=220)

# Function to show and hide obscured entries.
def password_command1():
    if password_entry1.cget('show') == '*':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='*')

ShowPass = Checkbutton(Login_frame4, bg='#f8f8f8',
                       command=password_command1,
                       text='Show password',
                       font = ("Helvetica",10))
ShowPass.place(x=140, y=288)

Info_Label = Label(Login_frame4, bg = '#f8f8f8',
                   text = "To EXIT click Escape (ESC) on your keyboard.",
                   fg = "Red",
                   width = 55,
                   height=5,
                   font = ("Helvetica",10,"bold"),
                   relief= GROOVE,
                   bd = 3)
Info_Label.place(x= 80,y= 410 )
Info_Label.config(highlightbackground="black", highlightcolor="black")

window.bind("<Escape>", lambda event: window.quit()) # Press ESC key to kill program.

# ========= Buttons ===============
Sign_up_button = Button(LogInFrame, text='Sign up',
                        font=("Helvetica", 12),
                        bg='#f8f8f8',
                        fg="#89898b",
                        command=lambda: showframe(RegisterFrame),
                        borderwidth=0,
                        activebackground='#1b87d2',
                        cursor='hand2')
Sign_up_button.place(x=1100, y=175)

# ===== Welcome Label ==============
welcome_label = Label(Login_frame4, text="SAT'S GAME QUIZ.", font=('Times', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ======= Top Login Button =========
login_button = Button(LogInFrame, text='Login',
                      font=("Helvetica", 12),
                      bg='#f8f8f8',
                      fg="#89898b",
                      borderwidth=0,
                      activebackground='#1b87d2',
                      cursor='hand2')
login_button.place(x=845, y=175)

Indicator1 = Canvas(LogInFrame,
                    width=60,
                    height=5,
                    bg='#1b87d2')
Indicator1.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = Button(Login_frame4, fg='#f8f8f8',
                   text='Login',
                   bg='#1b87d2',
                   font=("Helvetica", 15),
                   cursor='hand2',
                   activebackground='#1b87d2',
                   relief = RIDGE,
                   bd = 5,
                   command=lambda: login())
loginBtn1.place(x=133, y=340, width=256, height=50)

# ===================================================================================================================
# ===================================================================================================================
# === FORGOT PASSWORD  PAGE =========================================================================================
# ===================================================================================================================
# ===================================================================================================================


def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # Variables
    email = StringVar()
    password = StringVar()
    confirmPassword = StringVar()

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("Helvetica", 12), highlightthickness=2,
                         textvariable=email)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='* Email account', fg="#89898b", bg='#f8f8f8',
                         font=("Helvetica", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ====  New Password ==================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("Helvetica", 12), show='*', highlightthickness=2,
                               textvariable=password)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='* New Password', fg="#89898b", bg='#f8f8f8', font=("Helvetica", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("Helvetica", 12), show='*', highlightthickness=2
                                   , textvariable=confirmPassword)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='* Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("Helvetica", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("Helvetica", 14),
                         cursor='hand2', activebackground='#1b87d2', command=lambda: change_password())
    update_pass.place(x=40, y=240, width=256, height=50)

 # ========= DATABASE CONNECTION FOR FORGOT PASSWORD=====================
    def change_password():
        change_pass_permission = True # Boolean statement to ensure security of system.
        if new_password_entry.get() == '' or confirm_password_entry.get() == '':
            messagebox.showerror('Error!', "Entry boxes are Empty.")
            change_pass_permission = False # Not allowed entry.
    
        if change_pass_permission == True:
            if new_password_entry.get() == confirm_password_entry.get():
                db = sqlite3.connect("Client_info.db")
                print("Database connected successfully.")
                cur = db.cursor()

                insert = '''update Client_info set Password=?, ConfirmPassword=? where Email=? '''
                cur.execute(insert, [new_password_entry.get(), confirm_password_entry.get(), email_entry2.get().lower(), ])
                db.commit()
                db.close()
                messagebox.showinfo('Congrats', 'Password changed successfully')

            else:
                messagebox.showerror('Error!', "Passwords didn't match")


forgotPassword = Button(Login_frame4, text='Forgot password', font=("Helvetica", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=290, y=290)




# =====================================================================================================================
# =====================================================================================================================
# ==================== USER REGISTRATION PAGE =========================================================================
# =====================================================================================================================
# =====================================================================================================================

Reg_frame1 = Listbox(RegisterFrame, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
Reg_frame2 = Listbox(RegisterFrame, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
Reg_frame3 = Listbox(RegisterFrame, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
Reg_frame4 = Listbox(RegisterFrame, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)

Reg_frame1.place(x=0, y=0)
Reg_frame2.place(x=676, y=0)
Reg_frame3.place(x=75, y=106)
Reg_frame4.place(x=676, y=106)

icon1 = PhotoImage(file='icon1.png')
Label(Reg_frame4, image=icon1).place(x= 20, y= 115)

# ==== Full Name =======
name_entry = Entry(Reg_frame4, fg="#a7a7a7", font=("Helvetica", 12), highlightthickness=1,
                   textvariable=FullName)
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label = Label(Reg_frame4, text='*Full Name', fg="#89898b", bg='#f8f8f8', font=("Helvetica", 11, 'bold'))
name_label.place(x=280, y=120)

# ======= Email ===========
email_entry = Entry(Reg_frame4, fg="#a7a7a7", font=("Helvetica", 12), highlightthickness=1,
                    textvariable=Email)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(Reg_frame4, text='*Email', fg="#89898b", bg='#f8f8f8', font=("Helvetica", 11, 'bold'))
email_label.place(x=280, y=190)

# ====== Password =========
password_entry = Entry(Reg_frame4, fg="#a7a7a7", font=("Helvetica", 12), show='*', highlightthickness=1,
                       textvariable=Password)
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(Reg_frame4, text='* Password', fg="#89898b", bg='#f8f8f8',
                       font=("Helvetica", 11, 'bold'))
password_label.place(x=280, y=265)


def password_command2():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        confirmPassword_entry.config(show='')
    else:
        password_entry.config(show='*')
        confirmPassword_entry.config(show='*')


checkButton = Checkbutton(Reg_frame4, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)


# ====== Confirm Password =============
confirmPassword_entry = Entry(Reg_frame4, fg="#a7a7a7", font=("Helvetica", 12),show='*', highlightthickness=1,
                              textvariable=ConfirmPassword)
confirmPassword_entry.place(x=284, y=385, width=286, height=34)
confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
confirmPassword_label = Label(Reg_frame4, text='* Confirm Password', fg="#89898b", bg='#f8f8f8',
                              font=("Helvetica", 11, 'bold'))
confirmPassword_label.place(x=280, y=355)



# ========= Buttons ====================
SignUp_button = Button(RegisterFrame, text='Sign up', font=("Helvetica", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: showframe(LogInFrame), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175) # for top button.

Indicator2 = Canvas(RegisterFrame, width=60, height=5, bg='#1b87d2')
Indicator2.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(Reg_frame4, text="SAT'S GAME QUIZ.", font=('Times', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ========= Login Button =========
login_button = Button(RegisterFrame, text='Login', font=("Helvetica", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: showframe(LogInFrame), cursor='hand2')
login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
signUp2 = Button(Reg_frame4, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("Helvetica", 15),
                 cursor='hand2', activebackground='#1b87d2', command=lambda: submit())
signUp2.place(x=285, y=445, width=286, height=50)

# =====================================================================================================================
# =====================================================================================================================
# ==================== DATABASE CONNECTION ============================================================================
# =====================================================================================================================
# =====================================================================================================================

connection = sqlite3.connect('Client_info.db')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Client_info(Email TEXT PRIMARY KEY, FullName TEXT, Password TEXT, "
            "ConfirmPassword TEXT)")
try:
    connection.commit()
    connection.close()
except sqlite3.Error as err:
    print("An error has occurred", err)


# Catches each of the empty fields and gives out an appropriate message.
def submit():
    check_counter = 0
    warn = ""
    if name_entry.get() == "":
        warn = "Full Name can't be empty"
    else:
        check_counter += 1

    if email_entry.get() == "":

        warn = "Email Field can't be empty"
    else:
        check_counter += 1

    if password_entry.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if confirmPassword_entry.get() == "":
        warn = "Sorry, can't sign up make sure all fields are complete"
    else:
        check_counter += 1

    if password_entry.get() != confirmPassword_entry.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 5:
        try:
            connection = sqlite3.connect("Client_info.db")
            cur = connection.cursor()
            cur.execute("INSERT INTO Client_info values(?,?,?,?)",
                        (Email.get().lower(), FullName.get(), Password.get(), ConfirmPassword.get()))

            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "New account created successfully")

        except Exception as exp:
            messagebox.showerror('', exp)
    else:
        messagebox.showerror('Error', warn)





window.mainloop()
