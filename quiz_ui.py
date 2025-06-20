from tkinter import *
from tkinter import messagebox
import sqlite3 # To connect database.
import random # Used to randomise questions and quotes.

COLOUR = "#028090"                 #"#E56B6F"#red   #"#2FBF71"green # "#635380"purple     # "#028090"blueish

# Initialize global variables variables ( Can be used effectively anywhere).
selected_subject = None
selected_question_count = None
selected_timer = None
current_question_index = 0
score = 0
time_left = 300  # Default 5 minutes in seconds
questions = []
user_answers = []  # Stores user's answers for feedback
quiz_window = None  # Stores the main quiz window instance.  # None shows that it has no initial value.


def load_questions_from_db(subject, question_count):
    # Retrieve and load questions from the SQLite database based on the selected subject and question count.
    global questions
    try:
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT question, option1, option2, option3, option4, answer
            FROM questions
            WHERE subject = ?
            LIMIT ?
        ''', (subject, question_count))
        questions = cursor.fetchall()
        conn.close()
    except sqlite3.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")
        questions = []
        
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


        
def start_quiz():
    # Start the quiz based on selected options.
    global selected_subject, selected_question_count, selected_timer, time_left
    selected_subject = subject_var.get()
    #Exception handling.
    try:
        selected_question_count = int(question_count_var.get())
        selected_timer = int(timer_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please select valid options for questions and timer.")
        return

    if not selected_subject:
        messagebox.showerror("Selection Error", "Please select a subject.")
        return
    # Converts the minutes to seconds.
    time_left = selected_timer * 60
    load_questions_from_db(selected_subject, selected_question_count)
    # Prevents quiz from running if no question are found for the desired subject / Topic.
    if not questions:
        messagebox.showerror("No Questions", "No questions found for the selected subject.")
        return

    splash_screen.destroy()  # Close splash screen
    main_quiz_screen()  # Open main quiz screen

# ================== Main quiz =============================================================
def main_quiz_screen():
    # Set up the main quiz screen.
    global quiz_window, question_number_label, timer_label, q_label, option_box, selected_answer, submit_button
    quiz_window = Tk()
    quiz_window.attributes('-fullscreen', True)  # Make window fullscreen
    quiz_window.title("Quiz UI")
    quiz_window.config(background=COLOUR)#

    # Grid layout configuration for widgets
    quiz_window.columnconfigure(0, weight=1)
    quiz_window.columnconfigure(1, weight=1)
    quiz_window.columnconfigure(2, weight=1)
    quiz_window.rowconfigure(0, weight=1)
    quiz_window.rowconfigure(1, weight=3)
    quiz_window.rowconfigure(2, weight=3)
    quiz_window.rowconfigure(3, weight=1)

    # Heading Label
    Heading_Label = Label(quiz_window, text="Quiz Time!", font=('helvetica', 28, 'bold'), bg=COLOUR, fg='white')#
    Heading_Label.grid(row=0, column=0, columnspan=2, sticky='W', padx=20, pady=10)

    # Timer and Question Number Labels
    timer_label = Label(quiz_window, text=f"Time Left: {selected_timer}:00", font=('helvetica', 20, 'bold'), bg=COLOUR, fg='white')#
    timer_label.grid(row=0, column=2, sticky='E', padx=20)
    question_number_label = Label(quiz_window, text=f"Question: 1/{selected_question_count}", font=('helvetica', 20, 'bold'), bg=COLOUR, fg='white')#
    question_number_label.grid(row=0, column=1, sticky='E', padx=20)

    # Question Label
    q_label = Label(quiz_window, text="", font=('helvetica', 24, 'bold'), relief=RAISED, bg='white', wraplength=800)
    q_label.grid(row=1, column=0, columnspan=3, sticky='EW', pady=20, padx=20)

    # Option Box to house the four possible answers.
    option_box = Frame(quiz_window, bg="White", relief=SUNKEN, bd=5)#
    option_box.grid(row=2, column=0, columnspan=3, pady=20, padx=40, sticky='EW')

    # Selected Answer Variable
    selected_answer = StringVar(value=None)

    # Submit Button
    submit_button = Button(quiz_window, text="Submit", command=lambda: submit_answer(quiz_window), font=('helvetica', 18), bg='white', fg=COLOUR)#
    submit_button.grid(row=3, column=0, columnspan=3, pady=20)

    # Load First Question and Start Timer
    load_question()
    update_timer(quiz_window, timer_label)

    quiz_window.mainloop()


# Functions for quiz functionality. ==================================================

def load_question():
    # Load the current question and options form the quiz database.
    global current_question_index
    if current_question_index < selected_question_count:
        question_data = questions[current_question_index]
        q_label.config(text=f"Q{current_question_index + 1}: {question_data[0]}")
        question_number_label.config(text=f"Question: {current_question_index + 1}/{selected_question_count}")
        for widget in option_box.winfo_children():
            widget.destroy() # Destroys previous widgets in answer box.
            
            # Create option buttons for answers.
        for option in question_data[1:5]:
            rb = Radiobutton(
                option_box,
                text=option,
                variable=selected_answer,
                value=option,
                font=('helvetica', 18, 'bold'),
                bg=COLOUR,#
                fg='white',
                anchor='w',
                indicatoron=0,
                selectcolor='lightblue',
            )
            rb.pack(fill='x', padx=20, pady=10)
    else:
        end_game() # End game function.


def submit_answer(window):
    # Submit the selected answer and move to the next question.
    global current_question_index, score, user_answers

    selected = selected_answer.get()
   
    user_answers.append(selected if selected  else "No Answer")

    if selected and selected == questions[current_question_index][5]:  # Correct answer
        score += 1
    current_question_index += 1
    load_question()


def store_score(percentage):
    conn = sqlite3.connect("Client_info.db")
    print("Database opened successfully.")

    # Ensure table structure is correct (if deleted manually, this will recreate it)
    DDL = '''CREATE TABLE IF NOT EXISTS Scores( 
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Email TEXT,
              Subject TEXT,
              Score REAL)'''  # Allows multiple scores per email

    conn.execute(DDL)
    print("Table Exists / Created.")

    email = getuser()  
    subject = subject_var.get() 

    # Use parameterized query to prevent SQL injection
    DML = "INSERT INTO Scores (Email, Subject, Score) VALUES (?, ?, ?)"

    try:
        conn.execute(DML, (email, subject, round(percentage, 2)))
        conn.commit()  # Saves the data permanently
        print("Data Added")
    except sqlite3.Error as err:
        print("Oops! An error has occurred:", err)

    conn.close()



def end_game():
    # Displays the final score and ends the game once completed
    global quiz_window, selected_question_count, score

    # Destroy quiz window
    if quiz_window is not None:
        quiz_window.destroy()

    # Calculates percentage
    percentage = (score / selected_question_count) * 100
    store_score(percentage) # Calls function to store the percentage score in database.

    # End Game Screen
    end_screen = Tk()
    end_screen.title("Quiz Results")
    end_screen.geometry("600x500")
    end_screen.config(background=COLOUR)#

    # Final Score Display
    Label(end_screen, text="Quiz Completed!", font=('helvetica', 24, 'bold'), bg=COLOUR, fg='white').pack(pady=20)#
    Label(end_screen, text=f"Your Score: {score}/{selected_question_count}", font=('helvetica', 18), bg=COLOUR, fg='white').pack(pady=10)#
    Label(end_screen, text=f"Percentage: {percentage:.2f}%", font=('helvetica', 18), bg=COLOUR, fg='white').pack(pady=10)#

    # Show Feedback Button
    Button(
        end_screen,
        text="Show Feedback",
        command=lambda: show_feedback(end_screen),
        font=('helvetica', 18, 'bold'),
        bg='white',
        fg=COLOUR #
    ).pack(pady=20)

    # Exit Button
    Button(
        end_screen,
        text="Exit",
        command=lambda: quit(),
        font=('helvetica', 18, 'bold'),
        bg='white',
        fg=COLOUR # 
    ).pack(pady=10)

    end_screen.mainloop()

# ============ Feedback window =========================================================================
def show_feedback(parent_window):
    # Displays detailed feedback for each question.
    parent_window.destroy()  # Close the results screen
    feedback_screen = Tk()
    feedback_screen.title("Quiz Feedback")
    feedback_screen.geometry("800x400")
    feedback_screen.resizable(False,False)
    feedback_screen.config(background=COLOUR)#

    motivational_messages = [
        "Great effort! Keep improving!",
        "You did fantastic! Never stop learning!",
        "Awesome job! You're doing great!",
        "Keep pushing! You’re getting better every day!",
        "Well done! Your hard work is paying off!"
    ]

    # Scrollable Frame for Feedback
    canvas = Canvas(feedback_screen, bg='White')
    scroll_y = Scrollbar(feedback_screen, orient="vertical", command=canvas.yview, width = 25) # Create scrollbar.
    feedback_frame = Frame(canvas, bg=COLOUR)#

# Makes sure the feedback window can display all widgets.
    feedback_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=feedback_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll_y.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scroll_y.pack(side=RIGHT, fill=Y)

    Label(feedback_frame, text="Detailed Feedback", font=('helvetica', 24, 'bold'), bg=COLOUR, fg='white').pack(pady=20)#

    for index, question_data in enumerate(questions):
        question_text, *options, correct_answer = question_data
        selected_answer = user_answers[index]
        feedback = f"""
        Question {index + 1}: {question_text}
        Your Answer: {selected_answer or 'No Answer'}
        Correct Answer: {correct_answer}
        """
        Label(feedback_frame, text=feedback, font=('helvetica', 16), bg=COLOUR, fg='white', wraplength=700, justify='left').pack(pady=10, padx=10)#
# Displays motivational message.
    motivational_message = random.choice(motivational_messages)
    Label(feedback_frame, text=motivational_message, font=('helvetica', 18, 'italic'), bg=COLOUR, fg='white', wraplength=700, justify='center', relief= RIDGE, bd = 5).pack(pady=20, padx= 10)#
    # Exit button.
    Button(feedback_frame, text="Exit", command=lambda: quit(), font=('helvetica', 18), bg='white', fg=COLOUR).pack(pady=10)#

    feedback_screen.mainloop()


def update_timer(window, timer_label):
    # Update the countdown timer.
    global time_left
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"Time Left: {mins:02d}:{secs:02d}")
        time_left -= 1
        window.after(1000, update_timer, window, timer_label)
    else:
        end_game()


# ===================== Splash Screen ========================================


splash_screen = Tk() # First screen that shows up displaying options for quiz.
splash_screen.title("Quiz Setup")
splash_screen.config(background= COLOUR)#
splash_screen.geometry("1020x500")
splash_screen.resizable(False, False) # Make screen non resizable.

center_frame = Frame(splash_screen, bg= COLOUR) #
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

subject_var = StringVar()
Label(center_frame, text="Select Subject:", font=('helvetica', 18, 'bold'), bg= COLOUR, fg='white').pack(pady=10)#
OptionMenu(center_frame, subject_var, "SPAG1", "SPAG2", "MATHS", "Literature").pack(pady=10)

question_count_var = StringVar(value="10")
Label(center_frame, text="Number of Questions:", font=('helvetica', 18, 'bold'), bg= COLOUR, fg='white').pack(pady=10)#
OptionMenu(center_frame, question_count_var, "5", "10", "15", "20").pack(pady=10)

timer_var = StringVar(value="5")
Label(center_frame, text="Select Timer (minutes):", font=('helvetica', 18, 'bold'), bg= COLOUR, fg='white').pack(pady=10)#
OptionMenu(center_frame, timer_var, "5", "10", "20", "25").pack(pady=10)

Button(center_frame, text="Start Quiz", command=start_quiz, font=('helvetica', 18), bg='white', fg= COLOUR).pack(pady=20)#

splash_screen.mainloop()
#========================================================
#========================================================
