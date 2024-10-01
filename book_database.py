import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  pdf_path TEXT NOT NULL,
                  image_path TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#function to clear data from database
def clear():
    conn=sqlite3.connect("library.db")
    c=conn.cursor()
    c.execute("DELETE FROM books")
    conn.commit()
    conn.close()

# Function to add a new book record to the database
def add_book(name, pdf_path, image_path):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''INSERT INTO books (name, pdf_path, image_path)
                 VALUES (?, ?, ?)''', (name, pdf_path, image_path))
    conn.commit()
    conn.close()

# Function to retrieve all book records from the database
def get_all_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    return books

# Example usage of the functions
def main():
    # create_table()

    # Add a book record
    add_book('GENESIS', r"C:\Users\asus\Downloads\Genesis.pdf",r"C:\Users\asus\OneDrive\Pictures\genesis.jpg" )
    add_book('KNOWLEDGE REVEALED', r"C:\Users\asus\Downloads\Knowledge-Revealed.pdf",r"C:\Users\asus\OneDrive\Pictures\knowledge revealed.jpg" )
    add_book('MADE A KILLING',r"C:\Users\asus\Downloads\Made-A-Killing.pdf" , r"C:\Users\asus\OneDrive\Pictures\made a killing.jpg")
    add_book('28 DAYS', r"C:\Users\asus\Downloads\28-Days.pdf", r"C:\Users\asus\OneDrive\Pictures\28 days.jpg")
    add_book('FORBIDDEN ROACK AND ROLL', r"C:\Users\asus\Downloads\Forbidden-Rock-and-Roll.pdf", r"C:\Users\asus\OneDrive\Pictures\forbidden rock nd roll.jpg")
    add_book('DEMON GIRL',r"C:\Users\asus\Downloads\The-Demon-Girl.pdf" , r"C:\Users\asus\OneDrive\Pictures\demon girl.jpg")
    # add_book('TIME MACHINE', r"C:\Users\asus\Downloads\The-Time-Machine.pdf", r"C:\Users\asus\OneDrive\Pictures\time machine.jpg")
    # add_book('ALLADIN AND MAGIC LAMP', r"C:\Users\asus\Downloads\Aladdin-and-the-Magic-Lamp.pdf", r"C:\Users\asus\OneDrive\Pictures\alladin.jpg")
    

    # Retrieve all book records

    books = get_all_books()
    for book in books:
        print(book)


if __name__ == "__main__":
    main()