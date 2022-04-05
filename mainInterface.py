from tkinter import *
from tkinter import messagebox


class Account:
    def __init__(self):
        ##Create Window
        self.windows = Tk()
        self.windows.title("Account Information")
        self.windows.geometry("300x150")
        ##Create Frames
        self.username_frame = Frame(self.windows)
        self.password_frame = Frame(self.windows)
        self.submit_frame = Frame(self.windows)
        self.result_frame = Frame(self.windows)
        ##Creating Components
        self.username_label = Label(self.username_frame, text="Username: ")
        self.username_entry = Entry(self.username_frame, bg="snow2")
        self.password_label = Label(self.password_frame, text="Password: ")
        self.password_entry = Entry(self.password_frame, bg="snow2")
        self.submit_button = Button(self.submit_frame, text= "Submit", padx=10, command= self.displayText)
        self.result = StringVar()
        self.result.set("")
        self.result_label = Label(self.result_frame, textvariable=self.result, fg="black")
        ##Creating pack() Components
        self.username_label.pack(side="left")
        self.username_entry.pack(padx= 5, pady=5)
        self.password_label.pack(side="left")
        self.password_entry.pack(padx=5, pady=5)
        self.submit_button.pack(padx=10)
        self.result_label.pack()

        ##Creating pack() Frames
        self.username_frame.pack()
        self.password_frame.pack()
        self.submit_frame.pack()
        self.result_frame.pack()

        mainloop()

    def displayText(self):
        try:
            username = str(self.username_entry.get())
            password = str(self.password_entry.get())
            if username.isnumeric() or password.isnumeric():
                messagebox.showerror("ERROR", "CANNOT BE JUST NUMBER!")
            else:
                self.result.set(f'Username is {username} \n Password is {password}')
        except:
            messagebox.showerror('ERROR', "BAD INPUT!")

accountInfo = Account()