from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk


# ================================== Class for Creating buttons for the GUI.=================================================

from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

class MyButtons:
    def __init__(self, master):
        self.master = master

    def create_button(self, frame=None, text='', command=None, row=0, column=0, bg='SystemButtonFace'):
        if frame is None:
            frame = self.master
        button = Button(
            frame,
            text=text,
            command=command,
            font=("Helvetica", 20, "bold"),
            relief='ridge',
            bd=0,
            pady=5,
            padx=12,
            cursor='hand2',
            bg=bg
        )
        button.grid(row=row, column=column, padx=5, pady=5)
        return button

    def create_red_button(self, frame=None, text='', command=None, row=0, column=0):
        return self.create_button(frame, text, command, row, column, bg='red')

    def create_green_button(self, frame=None, text='', command=None, row=0, column=0):
        return self.create_button(frame, text, command, row, column, bg='green')

    def create_blue_button(self, frame=None, text='', command=None, row=0, column=0):
        return self.create_button(frame, text, command, row, column, bg='blue')

    def create_yellow_button(self, frame=None, text='', command=None, row=0, column=0):
        return self.create_button(frame, text, command, row, column, bg='yellow')

    def create_white_button(self, frame=None, text='', command=None, row=0, column=0):
        return self.create_button(frame, text, command, row, column, bg='white')

    def create_frame(self, row, column, rowspan=1, columnspan=1):
        frame = ttk.Frame(self.master, borderwidth=2, relief='groove', padding=10)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=10, pady=10, sticky='nsew')
        return frame

class StudyApp:
    def __init__(self):
        self.master = Tk()  # Main application window
        self.master.title("Study App")
        self.master.geometry("800x600")
        self.master.configure(background='lightblue')
        self.master.iconify() # Hides the window.

    def create_window(self, title, items):
        win = Toplevel(self.master)
        win.title(title)
        win.geometry("1125x650")
        win.configure(background='lightblue')
        win.resizable(0, 0)

        Label(win, text=f"      {title}", font=("Helvetica", 20, "bold", "underline")).grid(row=0, column=0, pady=10)

        topics_frame = LabelFrame(win, text="Select which topic you would like to study.",
                                   font=("Helvetica", 12, 'bold', 'underline'), padx=10, pady=10)
        topics_frame.grid(column=0, row=1, pady=20, padx=20, sticky='nsew')

        listbox_frame = Frame(topics_frame)
        listbox_frame.grid(row=0, column=0, sticky='nsew')

        listbox = Listbox(listbox_frame, font=("Helvetica", 12), width=105, height=15, cursor='hand2',
                          highlightbackground='lightblue', highlightthickness=5)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        for topic in items:
            listbox.insert(END, topic)
            listbox.insert(END, "")  # Empty line for spacing

        scrollbar = Scrollbar(listbox_frame, orient=VERTICAL, command=listbox.yview, width=20, cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.config(yscrollcommand=scrollbar.set)

        topics_frame.grid_rowconfigure(0, weight=1)
        topics_frame.grid_columnconfigure(0, weight=1)

        result_label = Label(win, text="", font=("Helvetica", 15, "bold"), bg='lightblue')
        result_label.grid(column=0, row=4, pady=10)

        submit_button = Button(win, text="Submit", font=("Helvetica", 15, "bold"), command=lambda: self.submit(listbox, result_label, win))
        submit_button.grid(column=0, row=2, pady=20)

        exit_button = Button(win, text="Return.", font=("Helvetica", 15, "bold"), command=win.destroy)
        exit_button.grid(column=0, row=3, pady=20)

    def submit(self, listbox, result_label, win):
        selected_index = listbox.curselection()
        if selected_index:
            selected_topic = listbox.get(selected_index[0])
            result_label.config(text=f"Selected Topic: {selected_topic}")
            win.destroy()
            self.stop_level()
        else:
            result_label.config(text="No topic selected.")

    def stop_level(self):
        flashcard_window = Toplevel(self.master)
        flashcard_app = Flashcards(flashcard_window)  

    def Spag_1(self):
        SP1_LB_ITEMS = [
            "Sentence Structure",
            "Nouns, pronouns and adjectives (Types and usage).",
            "Verbs (Tenses e.g. Past, Present and Future).",
            "Adverbs (How, when, where and why actions happen).",
            "Prepositions and Conjunctions (Linking words and phrases).",
            "Articles and Determiners (The use of 'a', 'an', 'the', and other determiners).",
            "Punctuation (e.g. '!','.',',',';',etc...).",
            "Clauses and Phrases (Main and subordinate clauses, noun phrases, and verb phrases)."
        ]
        self.create_window("SPAG 1", SP1_LB_ITEMS)

    def Spag_2(self):
        SP2_LB_ITEMS = [
            "Prefixes and Suffixes",
            "Synonyms and Antonyms",
            "Homophones and Homographs",
            "Word Classes (Nouns, Verbs, Adjectives, etc.)",
            "Conjunctions (Coordinating and Subordinating)",
            "Passive and Active Voice",
            "Direct and Indirect Speech",
            "Modal Verbs and Adverbs of Possibility"
        ]
        self.create_window("SPAG 2", SP2_LB_ITEMS)

    def Literature(self):
        Lit_LB_ITEMS = [
            "Classic Children's Literature",
            "Modern Children's Literature",
            "Poetry",
            "Folktales and Fables",
            "Myths and Legends",
            "Comprehension Skills",
            "Character Analysis",
            "Themes and Motifs"
        ]
        self.create_window("LITERATURE", Lit_LB_ITEMS)

    def Maths(self):
        Maths_LB_ITEMS = [
            "Number and Place Value",
            "Addition and Subtraction",
            "Multiplication and Division",
            "Fractions, Decimals, and Percentages",
            "Ratio and Proportion",
            "Algebra",
            "Measurement",
            "Geometry - Properties of Shapes",
            "Geometry - Position and Direction",
            "Statistics"
        ]
        self.create_window("MATHS", Maths_LB_ITEMS)

    def Add_More(self):
        def submit():
            check_counter = 0
            warn = ""
            if subject_var.get() == "":
                warn = "Please select a subject."
            else:
                check_counter += 1

            if question_text.get() == "":
                warn = "Complete all entries."
            else:
                check_counter += 1

            if answer_1.get() == "":
                warn = "Complete all entries."
            else:
                check_counter += 1

            if answer_2.get() == "":
                warn = "Complete all entries."
            else:
                check_counter += 1

            if answer_3.get() == "":
                warn = "Complete all entries."
            else:
                check_counter += 1

            if answer_4.get() == "":
                warn = "Complete all entries."
            else:
                check_counter += 1

            if Correct_answer.get() == "":
                warn = "Complete all entries."
            elif Correct_answer.get() not in [answer_1.get(), answer_2.get(), answer_3.get(), answer_4.get()]:
                warn = "The correct answer is not among the provided options."
            else:
                check_counter += 1

            if check_counter == 7:
                try:
                    add_question()  # Runs add question function.
                except Exception as exp:
                    messagebox.showerror('', exp)
            else:
                messagebox.showerror('Oops!', warn + " CLICK ON BUTTON AGAIN.")
                win.destroy()

        def add_question():
            conn = sqlite3.connect('quiz.db')
            cursor = conn.cursor()
            print("Database connected.")

            try:
                with open('question_id.txt', 'r') as file:
                    content = file.read().strip()
                    print(content)
                    ID_NUM = int(content)
            except FileNotFoundError:
                print("File was not found.\nPlease try again.")
            except ValueError:
                print("The file content is not a valid number.")

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                subject TEXT NOT NULL,
                question TEXT NOT NULL,
                option1 TEXT NOT NULL,
                option2 TEXT NOT NULL,
                option3 TEXT NOT NULL,
                option4 TEXT NOT NULL,
                answer TEXT NOT NULL
            )
            ''')
            NEW_ID = (1 + (ID_NUM))
            input1 = selected_subject = subject_var.get()
            input2 = question_text.get()
            input3 = answer_1.get()
            input4 = answer_2.get()
            input5 = answer_3.get()
            input6 = answer_4.get()
            input7 = Correct_answer.get()
            data = (NEW_ID, input1, input2, input3, input4, input5, input6, input7)

            DML = ''' INSERT INTO questions VALUES '''
            DML += str(data)
            print(DML)

            try:
                conn.execute(DML)
                conn.commit()
                print("Data added successfully.")
                messagebox.showinfo(title="SUCCESS!", message="The question has been added successfully!")

                with open('question_id.txt', 'w') as file:
                    file.write(str(NEW_ID))
                win.destroy()

            except sqlite3.Error as err:
                print("Oh No! An error has occurred", err)
                win.destroy()

            conn.close()

        win = Toplevel(self.master)
        win.title('Add More')
        win.geometry("1125x650")
        win.configure(background="Midnightblue")
        win.attributes('-fullscreen', True) # Makes window full screen.

        Label(win, text="      Add More", font=("Helvetica", 20, "bold", "underline")).grid()

        Button(win, text="EXIT.", command=lambda: win.destroy(), font=('helvetica', 18, 'bold'), relief=RAISED, bd=5,
               bg='white', fg="Midnightblue", cursor='hand2').grid(pady=20)

        center_frame = Frame(win, bg="Midnightblue", relief=RIDGE, bd=10)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        subject_var = StringVar()
        Label(center_frame, text="Select Subject:", font=('helvetica', 15, 'bold'), bg="Midnightblue", fg='white').pack(pady=10)
        OptionMenu(center_frame, subject_var, "SPAG1", "SPAG2", "MATHS", "LITERATURE").pack(pady=10)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter question.", relief=RIDGE, bd=5).pack(pady=10)
        question_text = Entry(center_frame, fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        question_text.pack(pady=10, padx=20)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter possible answer.", relief=RIDGE, bd=5).pack(pady=10)
        answer_1 = Entry(center_frame, fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        answer_1.pack(pady=10)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter possible answer.", relief=RIDGE, bd=5).pack(pady=10)
        answer_2 = Entry(center_frame, fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        answer_2.pack(pady=10)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter possible answer.", relief=RIDGE, bd=5).pack(pady=10)
        answer_3 = Entry(center_frame, fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        answer_3.pack(pady=10)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter possible answer.", relief=RIDGE, bd=5).pack(pady=10)
        answer_4 = Entry(center_frame, fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        answer_4.pack(pady=10)

        Label(center_frame, font=('helvetica', 12, 'bold'), text="Enter Correct answer.", relief=RIDGE, bd=5).pack(pady=10)
        Correct_answer = Entry(center_frame , fg="Black", font=("Helvetica", 12), highlightthickness=1, width=45)
        Correct_answer.pack(pady=10)

        Button(center_frame, text="Add question.", command=submit, font=('helvetica', 18, 'bold'), bg='white',
               relief=RAISED, bd=2, fg="Midnightblue", cursor='hand2').pack(pady=20)


# ==================== Class for Flashcards =========================================


class Flashcards:
    def __init__(self, window):
        self.window = window
        self.window.title("SATs Flashcard Quiz")
        self.window.configure(background="Midnightblue")
        self.window.attributes("-fullscreen", True)  # Full-screen mode

        # Load flashcards from file
        self.flashcards = self.load_flashcards("flashcards.txt")
        self.current_card = 0
        self.showing_answer = False  # Track whether the answer is being shown

        # Create GUI elements
        self.label = Label(window, text="", font=("Arial", 36), wraplength=1000)
        self.label.grid(row=0, column=0, columnspan=4, pady=50, sticky="nsew")

        # Buttons on the left side
        self.prev_button = Button(window, text="Previous", font=("Arial", 24), command=self.show_previous_card)
        self.prev_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.show_answer_button = Button(window, text="Show Answer", font=("Arial", 24), command=self.toggle_answer)
        self.show_answer_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Buttons on the right side
        self.next_button = Button(window, text="Next", font=("Arial", 24), command=self.show_next_card)
        self.next_button.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        self.exit_button = Button(window, text="Exit", font=("Arial", 24), command=window.destroy)
        self.exit_button.grid(row=1, column=3, padx=20, pady=20, sticky="nsew")

        # Configure grid weights for resizing
        window.grid_rowconfigure(0, weight=1)
        window.grid_rowconfigure(1, weight=0)  # Buttons row doesn't expand
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)
        window.grid_columnconfigure(3, weight=1)

        # Display the first card
        self.update_card()

    def load_flashcards(self, filename):
        try:
            with open(filename, 'r') as file:
                flashcards = file.readlines()
            return [card.strip().split("|") for card in flashcards]  # Split into [question, answer]
        except FileNotFoundError:
            messagebox.showerror("Error", "Flashcards file not found!")
            return []

    def update_card(self):
        question, answer = self.flashcards[self.current_card]
        if self.showing_answer:
            self.label.config(text=f"Answer: {answer}")
            self.show_answer_button.config(text="Show Question")
        else:
            self.label.config(text=f"Question: {question}")
            self.show_answer_button.config(text="Show Answer")
        self.update_buttons()

    def toggle_answer(self):  # Used to show and hide answers.
        self.showing_answer = not self.showing_answer
        self.update_card()

    def show_previous_card(self):
        if self.current_card > 0:
            self.current_card -= 1
            self.showing_answer = False
            self.update_card()

    def show_next_card(self):
        if self.current_card < len(self.flashcards) - 1:
            self.current_card += 1
            self.showing_answer = False
            self.update_card()

    def update_buttons(self):
        self.prev_button.config(state=NORMAL if self.current_card > 0 else DISABLED)
        self.next_button.config(state=NORMAL if self.current_card < len(self.flashcards) - 1 else DISABLED)




























