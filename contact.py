class Person:
    """A class to archive information about the people, such as name, email address and phone number."""

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email.lower()
        self.phone = phone
        print()
        print(f"Added person {self.name} to the list")
        print()

    def new_email(self, new_email):
        """Change the email address."""
        new_email = new_email.lower()
        While(new_email == self.email):
            print('The new email is the same as the old one!')
            new_email = input("Digit a new email address: ").lower()

        self.email = new_email
        print('The new email is:', new_email)

    def new_phone(self, new_phone):
        """Change the phone number"""
        While(new_phone == self.phone):
            print('The new phone number is the same as the old one!')
            new_phone = input('Digit a new phone number: ')
        
        self.phone = new_phone
        print('The new phone number is:', new_phone)

    def info(self):
        """Return the information about the contact"""
        print()
        print('Name:', self.name)
        print('Email address:', self.email)
        print('Phone number:', self.phone)
        print()

    def get_name(self):
        """Return the name of the contact."""
        return self.name
