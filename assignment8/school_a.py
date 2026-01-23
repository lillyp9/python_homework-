import sqlite3
import os

print("school_a.py is running")
print("Current working directory:", os.getcwd())

with sqlite3.connect("db/school.db") as conn:
    print("Database created and connected successfully.")

print("Done")

#create table students , courese , and enrollments
with sqlite3.connect("db/school.db") as conn:
    cursor = conn.cursor()
    
    # Create students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)
    
    # Create courses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    """)
    
    # Create enrollments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        enrollment_date TEXT,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    print("Tables created successfully.")