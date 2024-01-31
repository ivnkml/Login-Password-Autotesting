import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, master):
        self.master = master
        master.title("Login and password form")

        self.label_username = tk.Label(master, text="Login:")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_login = tk.Button(master, text="Enter", command=self.check_credentials)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Adding an attribute to store the result of credential verification
        self.login_result = False

    def check_credentials(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "password":
            self.login_result = True
            messagebox.showinfo("Success", "Login completed succesfully!")
        else:
            self.login_result = False
            messagebox.showerror("Error", "Wrong login or password!")

# Add a function that returns the result of credential verification
def login(username, password):

    return username == "admin" and password == "password"

# Adding a function for testing with a fixed session
def login_with_session(username, password, session):
  
    return login(username, password) and session == "fixed_session"

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
