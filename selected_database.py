from tkinter import *
import sqlite3

def create_table():
    conn = sqlite3.connect("selected_database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE sel_students4 (
              name TEXT,
              rollno INTEGER,
              year text,
              Issue_book TEXT,
              Issue_date TEXT,
              Fine INTEGER)''')
    conn.commit()
    conn.close()

def clear():
    conn = sqlite3.connect("selected_database.db")
    c = conn.cursor()
    c.execute('''DELETE FROM sel_students4''')
    conn.commit()
    conn.close()

def add_student(name, rollno, year,Issue_date, Issue_book, Fine):
    conn = sqlite3.connect("selected_database.db")
    c = conn.cursor()
    c.execute('''INSERT INTO sel_students4 (name, rollno,year, Issue_book, Issue_date, Fine)
                 VALUES (?, ?, ?, ?, ?,?)''', (name, rollno,year, Issue_book, Issue_date, Fine))
    conn.commit()
    conn.close()

def get_selected_student():
    conn = sqlite3.connect("selected_database.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM sel_students4''')
    sel_students4 = c.fetchall()
    conn.commit()
    conn.close()
    return sel_students4

if __name__ == "__main__":
    clear()
    # create_table()

    add_student('Siddhartha Chaturvedi', 123102141,"1st year", "let us c","01-04-2024", 6)
    


    sel_students4 = get_selected_student()
    # for sel_student in sel_students3:
    #     print(sel_student
    print(sel_students4)