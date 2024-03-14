        email = input("Please enter your email: ")
        password = input("Please enter your password: ")

        if self.verify_user(email, password):
            print("Other stuff")

        else:
            print("Invalid email or password.")