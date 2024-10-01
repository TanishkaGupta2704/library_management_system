from tkinter import *
from PIL import ImageTk, Image
from students_admin_treeview import Stu_corner
from tkinter import Toplevel
from about_us import About_us
import webbrowser
from functools import partial
from catalog import Catalog
from admin_profile import Profile_sub
from settings import Setting
from threading import Thread

class Libsystem1:
    
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN PAGE")
        self.root.geometry("1550x800+0+0")
# logo
        I1 = Image.open(r"C:\Users\asus\OneDrive\Pictures\nitlogo.jpg")
        new_img1 = I1.resize((150, 120))
        my_img1 = ImageTk.PhotoImage(new_img1)
        l2 = Label(root, image=my_img1)
        l2.place(x=0, y=0)
# side image
        I = Image.open(r"C:\Users\asus\OneDrive\Pictures\nitkkr1.jpg")
        new_img = I.resize((1400, 120))
        my_img = ImageTk.PhotoImage(new_img)
        l1 = Label(root, image=my_img)
        l1.place(x=150, y=0)
           

        def open_webpage(event):
            webbrowser.open("https://example.com")

        def stu_details():
            self.new_window=Toplevel(self.root)
            self.app=Stu_corner(self.new_window)

        def about():
            self.new_window=Toplevel(self.root)
            self.app=About_us(self.new_window)

        def catalog():
            self.new_window=Toplevel(self.root)
            self.app=Catalog(self.new_window)

        def profile():
            self.new_window=Toplevel(self.root)
            self.app=Profile_sub(self.new_window)

        def settings_call():
            self.new_window=Toplevel(self.root)
            self.app=Setting(self.new_window)


        def logout():
            # Close the current window
            root.destroy()
            # Open the login page window or frame
            open_login_page()

        def open_login_page():
            root = Tk()
            root.title("login form")
            root.geometry("1550x800+0+0")
            root.iconbitmap(r"C:\Users\User\Desktop\lib_icon.png")

            def Myclick():
                l3 = Label(root, text="form sumbitted !!", background="#FFFDD0")
                l3.grid(row=17, column=11)

            root.configure(background="#FFFDD0")

            l0 = Label(root, text="NIT\nKURUKSHETRA", font=("comic sans ms", 18, "bold"), background="#FFFDD0")
            l0.grid(row=0, column=4)

            I = Image.open(r"C:\Users\User\Desktop\lib_icon.png")
            new_img = I.resize((600, 400))
            my_img = ImageTk.PhotoImage(new_img)
            l1 = Label(root, image=my_img)
            l1.grid(row=0, column=13, columnspan=3)

            dummy_label_2 = Label(root, background="#FFFDD0")
            dummy_label_2.grid(row=1, column=0, padx=10, pady=10)

            dummy_enter = Label(root, background="#FFFDD0")
            dummy_enter.grid(row=3, column=2, padx=10, pady=10)

            dummy_entry1 = Label(root, background="#FFFDD0")
            dummy_entry1.grid(row=5, column=5, padx=10, pady=10)

            dummy_entry1 = Label(root, background="#FFFDD0")
            dummy_entry1.grid(row=7, column=7, padx=10, pady=10)

            my_label = Label(root, text="Enter details to login:  ", background="#FFFDD0",
                             font=('Helvetica', 18, 'bold'))
            my_label.grid(row=2, column=13)

            button_quit = Button(root, text="EXIT", command=root.quit, width=10)
            button_quit.grid(row=2, column=16)

            my_label2 = Label(root, text="ROLL NO:  ", background="#FFFDD0")
            my_label2.grid(row=4, column=14)

            e = Entry(root, width=30, borderwidth=3, relief="raised")
            e.grid(row=4, column=15)

            my_label3 = Label(root, text="PASSWORD:  ", background="#FFFDD0")
            my_label3.grid(row=6, column=14)

            e = Entry(root, width=30, borderwidth=3, relief="raised")
            e.grid(row=6, column=15)

            # dummy_entry2 = Label(root,background="#FFFDD0")
            # dummy_entry2.grid(row=13, column=10, padx=10, pady=10)

            my_button = Button(root, text="sumbit", padx=20, pady=5, command=Myclick, fg="white", background="black")
            my_button.grid(row=8,column=14)

            root.mainloop()

# title
        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("comic sans ms",18,"bold"),bg="#77B0AA")
        lbl_title.place(x=0,y=120,width=1550,height=50)

        logout_button=Button(root, text="LOGOUT", command=logout,bg="white",fg="black",font=("times new roman",10,"bold"))
        logout_button.place(x=1350,y=130,height=30,width=100)

        # status bar
        my_button = Button(root, text="STUDENT'S CORNER", fg="white", background="#382b58",font=("comic sans ms",15,"bold"),relief="raised",command=stu_details)
        my_button.place(x=0,y=170,width=310,height=50)


        my_button2 = Button(root, text="ABOUT US", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),command=about,
                           relief="raised")
        my_button2.place(x=310, y=170, width=310, height=50)
        my_button3 = Button(root, text="MANAGE CATALOG", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                           relief="raised",command=catalog)
        my_button3.place(x=620, y=170, width=310, height=50)

        my_button4 = Button(root, text="PROFILE", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                            relief="raised",command=profile)
        my_button4.place(x=930, y=170, width=310, height=50)
        my_button3 = Button(root, text="SETTINGS", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                            relief="raised",command=settings_call)
        my_button3.place(x=1240, y=170, width=310, height=50)
        # side frame
        side_frame=Frame(root,bd=4,relief="raised",bg="#382b58")
        side_frame.place(x=0,y=220,height=580,width=258.33)

        

        global our_quotes,count1,text_id
        count1=-1
        our_quotes=["The more that you\nread, the more things\nyou will know.The\nmore that you learn,\nthe more places\nyou'll go. -\nDr. Seuss","Education is the most \npowerful weapon which\nyou can use to change\nthe world.\n- Nelson Mandela"]
        #create a canvas//>>
        my_canvas1=Canvas(root,width=258.33,height=580,background="#382b58",)
        my_canvas1.place(x=0,y=220)
 
        text_id=my_canvas1.create_text(20, 50, text=our_quotes[0], anchor='nw', font=("Pristina",22, "bold"),fill="white")
 
        def next1():
            global count1, text_id
            # Increment count
            count1 = (count1 + 1) % len(our_quotes)
            # Update the text of the existing text item
            my_canvas1.itemconfig(text_id, text=our_quotes[count1])
            # Schedule the next update
            root.after(3000, next1)
 
        next1()

        b2=Button(my_canvas1,text="SWITCH ACCOUNT",background="#382b58",fg="white",font=("comic sans ms", 15, "bold"),relief="raised",bd=2,command=logout)
        b2.place(x=2,y=433,width=258.33,height=50)

 
 
        
        my_frame=LabelFrame(root,bd=2,relief=RIDGE,text="POPULAR BOOKS",font=("comic sans ms", 19, "bold"))
        my_frame.place(x=280,y=250,width=1220,height=600)

        footer_label=Label(root,text="Copyright © 2024 National Institute of Technology Kurukshetra. All Rights Reserved.\n CONTACT US:110-2304-306",bd=4,relief="raised",bg="#77B0AA",font=("comic sans ms", 15, "bold"))
        footer_label.place(x=0,y=700,height=100,width=1528)

        # main_frame = Frame(root, relief="raised")
        # main_frame.place(x=300, y=275, height=590, width=1250)       


        def open_book(event,link):
            webbrowser.open(link)
 
        # Load a book icon image//BOOK1 
        book_image1 = Image.open(r"C:\Users\asus\OneDrive\Pictures\genesis.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image1 = book_image1.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image1 = ImageTk.PhotoImage(book_image1)
 
        # Create a label with the book icon image
        book_label1 = Label(my_frame, image=book_image1,padx=20)
        book_label1.image=book_image1
        book_label1.place(x=100,y=100)
 
        # Bind the click event to the book label
        book_label1.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396742/read"))
 
        # Load a book icon image//BOOK2
        book_image2 = Image.open(r"C:\Users\asus\OneDrive\Pictures\knowledge revealed.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image2 = book_image2.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image2 = ImageTk.PhotoImage(book_image2)
 
        # Create a label with the book icon image
        book_label2 = Label(my_frame, image=book_image2,padx=20)
        book_label2.image=book_image2
        book_label2.place(x=400,y=100)
 
        # Bind the click event to the book label
        book_label2.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396744/read"))
 
        # Load a book icon image//BOOK3
        book_image3 = Image.open(r"C:\Users\asus\OneDrive\Pictures\time machine.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image3 = book_image3.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image3 = ImageTk.PhotoImage(book_image3)
 
        # Create a label with the book icon image
        book_label3 = Label(my_frame, image=book_image3,padx=20)
        book_label3.image=book_image3
        book_label3.place(x=700,y=100)
 
        # Bind the click event to the book label
        book_label3.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/127836/read"))
 
        # Load a book icon image//BOOK4
        book_image4 = Image.open(r"C:\Users\asus\OneDrive\Pictures\made a killing.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image4 = book_image4.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image4 = ImageTk.PhotoImage(book_image4)
 
        # Create a label with the book icon image
        book_label4 = Label(my_frame, image=book_image4)
        book_label4.image=book_image4
        book_label4.place(x=1000,y=100)
 
        # Bind the click event to the book label
        book_label4.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396746/read"))
 

        self.root.mainloop()

if __name__=="__main__":
    root=Tk()
    obj = Libsystem1(root)
    root.mainloop()

