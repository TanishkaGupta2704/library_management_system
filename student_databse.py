import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE students2(
           name text,
           roll int,
           books text,
           year int,
           idate text,
           fine int
           
           )""")
    conn.commit()
    conn.close()

#function to clear data from database
def clear():
    conn=sqlite3.connect("student_database.db")
    c=conn.cursor()
    c.execute("DELETE FROM students2")
    conn.commit()
    conn.close()

# Function to add a new book record to the database
def add_student(name, roll,books,year,idate,Fine):
    conn = sqlite3.connect("student_database.db")
    c = conn.cursor()
    c.execute('''INSERT INTO students2 (name, roll,books, year,idate,Fine)
                 VALUES (?, ?, ?, ?, ?,?)''', (name, roll,books, year,idate,Fine))
    conn.commit()
    conn.close()

# Function to retrieve all book records from the database
def get_all_students():
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students2')
    students = c.fetchall()
    conn.close()
    return students

# Example usage of the functions
def main():
    # create_table()

    # Add a book record
    add_student('Siddhartha Chaturvedi',123102141,"let us c","1st year","20/04/2024",6 )
    add_student('Tanishka Gupta',123102175,"higher mathematics","2nd year","10-04-2024",0 )
    # add_student('Ashita Pahwa',123102181,"05-04-2024","20-04-2024",1 )
    # add_student('Ananya Pandey',123102145,"01-04-2024","20-04-2024",6 )
    add_student('Roshan Pratap',123102148,"BS. Grewal","2nd year","22-04-2024",0 )
    

    

    # Retrieve all book records

    students1 = get_all_students()
    
    print(students1)


if __name__ == "__main__":
    main()