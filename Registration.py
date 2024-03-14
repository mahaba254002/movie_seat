import sqlite3

class Registration:
    def __init__(self):
        pass

    def login(self):
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")

        if self.verify_user(email.lower(), password.lower()):
            print("Welcome back!")
            # Add code here to open the main window or perform other actions after successful login
        else:
            print("Invalid email or password.")

    def verify_user(self, email, password):
        conn = sqlite3.connect("registration.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
        row = cursor.fetchone()

        if row is not None:
            saved_password = row[2]
            if password == saved_password:
                return True

        return False

    def open_table(self):
        conn = sqlite3.connect("registration.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        for row in rows:
            name = row[0]
            email = row[1]
            password = row[2]
            print("Name:", name)
            print("Email:", email)
            print("Password:", password)
            print("--------------------------")
        conn.close()

registration = Registration()
registration.login()
registration.open_table()
