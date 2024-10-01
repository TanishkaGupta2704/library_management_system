from tkinter import *
from PIL import ImageTk, Image

class Libsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN PAGE")
        self.root.geometry("1550x800+0+0")

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
                l3 = Label(root, text="form submitted !!", background="#FFFDD0")
                l3.grid(row=17, column=11)

            root.configure(background="#FFFDD0")

            l0 = Label(root, text="NIT\nKURUKSHETRA", font=("comic sans ms", 18, "bold"), background="#FFFDD0")
            l0.grid(row=0, column=4)

            I = Image.open(r"C:\Users\asus\OneDrive\Pictures\Library.jpg")
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

            my_button = Button(root, text="submit", padx=20, pady=5, command=Myclick, fg="white", background="black")
            my_button.grid(row=8, column=14)

            root.mainloop()

        # title
        lbl_title = Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=("times new roman", 18, "bold"), bg="#23C471")
        lbl_title.place(x=0, y=120, width=1550, height=50)

        logout_button = Button(root, text="LOGOUT", command=logout, bg="white", fg="black",
                               font=("times new roman", 10, "bold"))
        logout_button.place(x=1350, y=130, height=30, width=100)

        # status bar
        my_button = Button(root, text="MY ACCOUNT", fg="white", background="#382b58",
                           font=("comic sans ms", 15, "bold"), relief="raised")
        my_button.place(x=0, y=170, width=258.33, height=50)

        # Dropdown menu for My Account
        options = ["Student Info", "Library Corner"]
        selected_option = StringVar(root)
        selected_option.set(options[0])  # default value

        dropdown_menu = OptionMenu(root, selected_option, *options)
        dropdown_menu.config(fg="white", bg="#382b58", font=("comic sans ms", 15, "bold"))
        dropdown_menu.place(x=0, y=220, width=258.33, height=50)

        my_button1 = Button(root, text="MY LIBRARY", fg="white", background="#382b58",
                            font=("comic sans ms", 15, "bold"), relief="raised")
        my_button1.place(x=258.33, y=170, width=258.33, height=50)

        my_button2 = Button(root, text="AUDIOBOOKS", fg="white", background="#382b58",
                            font=("comic sans ms", 15, "bold"), relief="raised")
        my_button2.place(x=516.66, y=170, width=258.33, height=50)
        my_button3 = Button(root, text="NOTIFICATIONS", fg="white", background="#382b58",
                            font=("comic sans ms", 15, "bold"), relief="raised")
        my_button3.place(x=774.99, y=170, width=258.33, height=50)

        my_button4 = Button(root, text="ABOUT US", fg="white", background="#382b58",
                            font=("comic sans ms", 15, "bold"), relief="raised")
        my_button4.place(x=1033.32, y=170, width=258.33, height=50)

        e1 = Entry(root, fg="grey", bg="#F0EBE3", font=("comic sans ms", 15, "bold"), relief="raised")
        e1.place(x=1291.65, y=170, height=50)
        e1.insert(0, "Search book by name/author:")

        # side frame
        side_frame = Frame(root, bd=4, relief="raised", bg="#382b58")
        side_frame.place(x=0, y=220, height=580, width=258.33)
        my_button5 = Button(side_frame, text="SWITCH ACCOUNT", fg="white", bg="#382b58",
                            font=("comic sans ms", 15, "bold"),
                            relief="raised")
        my_button5.place(x=0, y=510, height=50, width=258.33)

        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Libsystem(root)
    root.mainloop()

