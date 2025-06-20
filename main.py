# Main Screen.
from tkinter import *
from tkinter import messagebox
from Classes import *
from Classes import MyButtons  # Used to create buttons.
from Classes import StudyApp  # For the buttons.

# Set window parameters.
window = Tk()
window.title('Main page')
icon = PhotoImage(file='OIP.png')
# window.iconphoto(True,icon)
window.minsize(650, 600)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.attributes('-fullscreen',True) # Makes window full screen.
my_buttons = MyButtons(window)

THEME_COLOUR = "Midnightblue"

# Create Frames and grid.
Main_Frame1 = Frame(window, width=window.winfo_width(), height=window.winfo_height(), bg= THEME_COLOUR)
Main_Frame2 = Frame(window, width=window.winfo_width(), height=window.winfo_height(), bg= THEME_COLOUR)
Main_Frame3 = Frame(window, width=window.winfo_width(), height=window.winfo_height(), bg= THEME_COLOUR)


# Grid Frames.
for frame in (Main_Frame1, Main_Frame2, Main_Frame3):
    frame.grid(row=0, column=0, sticky='nsew')


# Code that will show the appropriate frame.
def showframe(frame):
    frame.tkraise()


showframe(Main_Frame1)  # Original frame.

# =======================================================================================================================
# =======================================================================================================================
# ==================================================[ Home Screen ]======================================================
# =======================================================================================================================

side_menu = Listbox(Main_Frame1, width=20, height=49, relief='groove', bd=5, font=("Helvetica", 15))
side_menu.grid(row=0, column=0, sticky='nsew')
side_menu.grid_propagate(False)

def getuser():
    with open('datafile.txt', 'r') as file:
        E_Mail = file.read().strip()
        print(E_Mail)
        return E_Mail


def getusersname():
    data = getuser()  # Ensure this function returns a valid email
    if not data:
        messagebox.showerror("Input Error", "Email not found.")
        return None

    try:
        conn = sqlite3.connect('Client_info.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT FullName
            FROM Client_info
            WHERE Email = ?
        ''', (data,))

        user_name = cursor.fetchall()
        conn.close()

        if user_name:
            return user_name[0][0]  # Return the FullName (first element of the first tuple)
        else:
            return None  # No result found for the email

    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")
        return None


Name = getusersname()

Toplabel = Label(Main_Frame1, width=86, height=3, text=(f'Welcome {Name} '), relief='groove', bd=5,
                 font=("Helvetica", 18, 'bold'))
Toplabel.grid(row=0, column=1, sticky='ne')

# Create buttons for side menu.

Home_Button = my_buttons.create_white_button(frame=side_menu, text="   Home   ", command=lambda: showframe(Main_Frame1),
                                             row=0, column=0)
Home_Button.configure(relief='ridge', bd=2, pady=5, padx=22)

Scores_Button = my_buttons.create_white_button(frame=side_menu, text="    Scores   ",
                                               command=lambda: showframe(Main_Frame2), row=1, column=0)
Scores_Button.configure(relief='ridge', bd=2, pady=5, padx=12)

Instrctions_Button = my_buttons.create_white_button(frame=side_menu, text="Instructions",
                                                     command=lambda: showframe(Main_Frame3), row=2, column=0)
Instrctions_Button.configure(relief='ridge', bd=2, pady=5, padx=10)

Exit_Button = my_buttons.create_white_button(frame=side_menu, text="       Exit       ",
                                                    command= lambda: window.quit() , row=3, column=0)
Exit_Button.configure(relief='ridge', bd=2, pady=5, padx=6)
Indicator1 = Canvas(side_menu, width=80, height=5, bg='#1b87d2')  # Indicates which screen the user is on.
Indicator1.place(x=67, y=47)

Box1 = Listbox(Main_Frame1, width=100, height=5, relief='groove', bd=5, bg='Blue')
Box1.place(x=465, y=150)

# Instance creation from StudyApp in Classes.py to use in buttons below.
app = StudyApp()


# function for Quiz_Button
def Quiz_ui():  # Call quiz_ui.py file as subprocess.
    from subprocess import call
    call(["python", "quiz_ui.py"])


# Place buttons in Box 1.

SPAG1_button = my_buttons.create_white_button(frame=Box1, text="SPAG 1", command=lambda: app.Spag_1(), row=0, column=0)

SPAG2_button = my_buttons.create_white_button(frame=Box1, text="SPAG 2", command=lambda: app.Spag_2(), row=0, column=1)

Literature_button = my_buttons.create_white_button(frame=Box1, text="Literature", command=lambda: app.Literature(),
                                                   row=0, column=2)

Maths_Button = my_buttons.create_white_button(frame=Box1, text="Maths", command=lambda: app.Maths(), row=0, column=3)

Quiz_Button = my_buttons.create_white_button(frame=Box1, text="Quiz", command=lambda: Quiz_ui(), row=0, column=4)

Add_Button = my_buttons.create_white_button(frame=Box1, text="Add More", command=lambda: app.Add_More(), row=0,
                                            column=5)

# =======================================================================================================================
# =======================================================================================================================
# ==================================================[ Scores Screen ]====================================================
# =======================================================================================================================

side_menu = Listbox(Main_Frame2, width=20, height=49, relief='groove', bd=5, font=("Helvetica", 15))
side_menu.grid(row=0, column=0, sticky='nsew')
side_menu.grid_propagate(False)

# Create buttons for side menu.

Home_Button = my_buttons.create_white_button(frame=side_menu, text="   Home   ", command=lambda: showframe(Main_Frame1), row=0, column=0)
Home_Button.configure(relief='ridge', bd=2, pady=5, padx=22)

Scores_Button = my_buttons.create_white_button(frame=side_menu, text="    Scores   ", command=lambda: showframe(Main_Frame2), row=1, column=0)
Scores_Button.configure(relief='ridge', bd=2, pady=5, padx=12)

Instrctions_Button = my_buttons.create_white_button(frame=side_menu, text="Instructions",
                                                     command=lambda: showframe(Main_Frame3), row=2, column=0)
Instrctions_Button.configure(relief='ridge', bd=2, pady=5, padx=10)

Exit_Button = my_buttons.create_white_button(frame=side_menu, text="       Exit       ",
                                                    command= lambda: window.quit() , row=3, column=0)
Exit_Button.configure(relief='ridge', bd=2, pady=5, padx=6)

Toplabel = Label(Main_Frame2, width=86, height=3, text=('-- SCORES --'), relief='groove', bd=5, font=("Helvetica", 18, 'bold'))
Toplabel.grid(row=0, column=1, columnspan=2, sticky='ne')

Indicator1 = Canvas(side_menu, width=90, height=5, bg='#1b87d2')  # Indicates which screen the user is on.
Indicator1.place(x=65, y=120)

Email = getuser()

# =======================================================================================================================
# ==========================================[ Scores Table Section in Main_Frame2 ]====================================
# =======================================================================================================================

def display_scores():
    print("display_scores() called")  # Debug print in console
    selected_subject = subject_var.get()
    text_widget.delete("1.0", END)  # Clear previous results

    try:
        conn = sqlite3.connect("Client_info.db")  # Connect to database.
        cursor = conn.cursor()

        # Query to get scores for the selected subject.
        cursor.execute("SELECT ID, Email, Score FROM Scores WHERE Email = ? AND Subject = ?", (Email, selected_subject,))
        rows = cursor.fetchall()
        print(f"Fetched {len(rows)} rows for subject: {selected_subject}")  # Debug print

        if not rows:
            text_widget.insert(END, f"No scores found for {selected_subject}.\n")
        else:
            text_widget.insert(END, f"Scores for {selected_subject}:\n\n")
            for row in rows:
                text_widget.insert(END, f"ID: {row[0]}, Email: {row[1]}, Score: {row[2]}%\n")

    except sqlite3.Error as err:
        text_widget.insert(END, f"Oops! An error has occurred: {err}\n")
        print("SQLite error:", err)
    finally:
        if conn:
            conn.close()

# Create the subject selection dropdown.
subject_var = StringVar(Main_Frame2)
subject_var.set("MATHS")  # Default selection

Subject_Label = Label(Main_Frame2, text="Select subject:", font=("Helvetica", 15, "bold"), relief = RAISED, bd = 3)
Subject_Label.place(x=550, y=200)

Subject_options = ["MATHS", "Literature", "SPAG1", "SPAG2"]
Subject_Menu = OptionMenu(Main_Frame2, subject_var, *Subject_options)
Subject_Menu.place(x=715, y=200)  
# Button to fetch scores.
Load_button = Button(Main_Frame2, text="Load Scores", font=("Helvetica", 15), cursor='hand2', command=display_scores)
Load_button.place(x=550, y=240)

# Text widget to display scores.
text_widget = Text(Main_Frame2, height=15, width=50, wrap=WORD, font=("Helvetica", 15))
text_widget.place(x=550, y=300)

display_scores()



# =======================================================================================================================
# =======================================================================================================================
# ==================================================[ Instructions Screen ]==============================================
# =======================================================================================================================


side_menu = Listbox(Main_Frame3, width=20, height=49, relief='groove', bd=5, font=("Helvetica", 15))
side_menu.grid(row=0, column=0, sticky='nsew')
side_menu.grid_propagate(False)

# Create buttons for side menu.

Home_Button = my_buttons.create_white_button(frame=side_menu, text="   Home   ", command=lambda: showframe(Main_Frame1),
                                             row=0, column=0)
Home_Button.configure(relief='ridge', bd=2, pady=5, padx=22)

Scores_Button = my_buttons.create_white_button(frame=side_menu, text="    Scores   ",
                                               command=lambda: showframe(Main_Frame2), row=1, column=0)
Scores_Button.configure(relief='ridge', bd=2, pady=5, padx=12)

Instrctions_Button = my_buttons.create_white_button(frame=side_menu, text="Instructions",
                                                     command=lambda: showframe(Main_Frame3), row=2, column=0)
Instrctions_Button.configure(relief='ridge', bd=2, pady=5, padx=10)

Exit_Button = my_buttons.create_white_button(frame=side_menu, text="       Exit       ",
                                                    command= lambda: window.quit() , row=3, column=0)
Exit_Button.configure(relief='ridge', bd=2, pady=5, padx=6)



Toplabel = Label(Main_Frame3, width=86, height=3, text=(" -- INSTRUCTIONS -- "), relief='groove', bd=5,
                 font=("Helvetica", 18, 'bold'))
Toplabel.grid(row=0, column=1, sticky='ne')

Indicator1 = Canvas(side_menu, width=95, height=5, bg='#1b87d2')  # Indicates which screen the user is on.
Indicator1.place(x=60, y=197)

Label(Main_Frame3,
      text="TO ACCESS ANY OF THE REVISION CONTENT AND MATERIALS,\n PLEASE CLICK ANY OF THE FOLLOWING OPTIONS IN THE HOME SCREEN: 'SPAG 1', 'SPAG 2', 'MATHS', 'LITERATURE'",
      font=("Helvetica", 15, "bold")).place(x=250, y=150)

tutorial_image = PhotoImage(file='tutorial.png')
Label(Main_Frame3, image=tutorial_image).place(x=495, y=215)

Label(Main_Frame3,
      text="TO ACCESS QUIZ, PRESS QUIZ BUTTON AND SELECT SUBJECT, NUMBER OR QUESTIONS AND TIMER TO BEGIN.\n HAVE FUN ;)",
      font=("Helvetica", 15, "bold")).place(x=250, y=350)

window.mainloop()
