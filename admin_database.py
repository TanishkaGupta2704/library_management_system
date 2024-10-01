import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('admin_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE admins1
                 (
                  name TEXT ,
                  adminID INTEGER)''')
    conn.commit()
    conn.close()

#function to clear data from database
def clear():
    conn=sqlite3.connect("admin_database.db")
    c=conn.cursor()
    c.execute("DELETE FROM admins1")
    conn.commit()
    conn.close()

# Function to add a new book record to the database
def add_admin(name,adminID):
    conn = sqlite3.connect("admin_database.db")
    c = conn.cursor()
    c.execute('''INSERT INTO admins1 (name, adminID)
                 VALUES (?, ?)''', (name, adminID))
    conn.commit()
    conn.close()

# Function to retrieve all book records from the database
def get_all_admins():
    conn = sqlite3.connect('admin_database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM admins1')
    admins1 = c.fetchall()
    conn.close()
    return admins1

# Example usage of the functions
if __name__=="__main__":
    # create_table()

    # Add a admin record
    # add_admin('Aryan Kumar',256)
    

    # Retrieve all admin records

    admins1 = get_all_admins()
    for admin in admins1:
        print(admin)


