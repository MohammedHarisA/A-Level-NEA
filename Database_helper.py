#Load questions into database: 
import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create the table for storing questions
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
''') # not null placeholder.
# ======================================================================
# Insert sample questions into the database
sample_questions = [
    # SPAG1 Questions
    ('SPAG1', 'What is the capital of France?', 'Berlin', 'Rome', 'Madrid', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is 2 + 2?', '3', 'I can’t believe this is the answer', '5', '6', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is the synonym of "happy"?', 'Sad', 'I can’t believe this is the answer', 'Angry', 'Tired', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which word is a noun?', 'Run', 'Quickly', 'I can’t believe this is the answer', 'Silent', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is the antonym of "old"?', 'Big', 'Fast', 'Tall', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is 10 - 5?', 'I can’t believe this is the answer', '3', '4', '6', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which color is a primary color?', 'Green', 'Purple', 'I can’t believe this is the answer', 'Orange', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is the opposite of "up"?', 'Left', 'I can’t believe this is the answer', 'Right', 'Forward', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which word is a verb?', 'Happiness', 'I can’t believe this is the answer', 'Brilliant', 'High', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is the past tense of "run"?', 'I can’t believe this is the answer', 'Running', 'Runs', 'Runned', 'I can’t believe this is the answer'),
    ('SPAG1', 'How many days are in a week?', '6', '8', '10', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which planet is known as the Red Planet?', 'Earth', 'Venus', 'I can’t believe this is the answer', 'Jupiter', 'I can’t believe this is the answer'),
    ('SPAG1', 'What is the largest ocean on Earth?', 'Atlantic', 'Indian', 'Arctic', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which continent is the Sahara Desert in?', 'Asia', 'Australia', 'Europe', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG1', 'Which element has the symbol O?', 'Gold', 'Iron', 'I can’t believe this is the answer', 'Osmium', 'I can’t believe this is the answer'),

    # SPAG2 Questions
    ('SPAG2', 'Who wrote "Hamlet"?', 'Dickens', 'Hemingway', 'Orwell', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'Which language is primarily spoken in Brazil?', 'Spanish', 'French', 'English', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is the plural of "child"?', 'Childs', 'Child', 'Childes', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'Identify the verb: "She sings beautifully."', 'She', 'I can’t believe this is the answer', 'Beautifully', 'None', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is the comparative form of "good"?', 'Best', 'Gooder', 'Worse', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is 3 x 3?', '6', '9', 'I can’t believe this is the answer', '15', 'I can’t believe this is the answer'),
    ('SPAG2', 'Who painted the Mona Lisa?', 'Van Gogh', 'Picasso', 'I can’t believe this is the answer', 'Monet', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is H2O?', 'Helium', 'I can’t believe this is the answer', 'Hydrogen', 'Oxygen', 'I can’t believe this is the answer'),
    ('SPAG2', 'Who is the founder of Microsoft?', 'Steve Jobs', 'Bill Clinton', 'I can’t believe this is the answer', 'Mark Zuckerberg', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is the capital of Japan?', 'Seoul', 'Beijing', 'Bangkok', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'Which planet is closest to the sun?', 'Earth', 'Venus', 'Mars', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('SPAG2', 'Who wrote "Romeo and Juliet"?', 'Hemingway', 'Dickens', 'I can’t believe this is the answer', 'Tolstoy', 'I can’t believe this is the answer'),
    ('SPAG2', 'How many continents are there?', '5', '6', 'I can’t believe this is the answer', '8', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is the speed of light?', '100,000 km/s', 'I can’t believe this is the answer', '300,000 km/s', '500,000 km/s', 'I can’t believe this is the answer'),
    ('SPAG2', 'What is the chemical symbol for gold?', 'Ag', 'Au', 'Pb', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),

    # MATHS Questions
    ('MATHS', 'What is 2 + 3?', '4', 'I can’t believe this is the answer', '6', '7', 'I can’t believe this is the answer'),
    ('MATHS', 'What is the square root of 64?', '6', '7', 'I can’t believe this is the answer', '9', 'I can’t believe this is the answer'),
    ('MATHS', 'What is 10 / 2?', '4', 'I can’t believe this is the answer', '10', '20', 'I can’t believe this is the answer'),
    ('MATHS', 'What is 3 x 3?', '6', 'I can’t believe this is the answer', '12', '15', 'I can’t believe this is the answer'),
    ('MATHS', 'Solve for x: 2x + 3 = 7.', '1', 'I can’t believe this is the answer', '3', '4', 'I can’t believe this is the answer'),
    ('MATHS', 'What is 9 + 10?', '15', '18', '20', 'I can’t believe this is the answer', 'I can’t believe this is the answer'),
    ('MATHS', 'What is 5 x 6?', '25', 'I can’t believe this is the answer', '35', '40', 'I can’t believe this is the answer'),
    ('MATHS', 'What is 12 / 4?', '2', 'I can’t believe this is the answer', '4', '5', 'I can’t believe this is the answer'),
    ('MATHS', 'What is the value of Pi?', '3.0', '3.1', 'I can’t believe this is the answer', '3.5', 'I can’t believe this is the answer'),
    ('MATHS', 'What is the derivative of x^2?', 'x', 'I can’t believe this is the answer', '2x^2', '2x', 'I can’t believe this is the answer'),
    ('MATHS', 'What is the derivative of x^2?', 'x', 'I can’t believe this is the answer', '2x^2', '2x', 'I can’t believe this is the answer')]
# ======================================================================




DML = '''INSERT INTO questions Values '''
