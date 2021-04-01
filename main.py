# Command-line address-book program
import sqlite3

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


def access_contacts(db):
    """Function to access the specific contacts saved in the class Person."""
    
    YES = {'yes', 'y', 'ye'}

    contact_id = input('Which contact do you want to access? ')
    
    try:
        contact_id = int(contact_id)

    except er as Exception:
        print(er)

    db[contact_id].info()
        
    user_input_choice = input('Do you want to access any other contact? y/N ').lower()

    if user_input_choice in YES:
        access_contacts(db)
        return

    userExit(db)
    return


def edit_contact(db):
    """Function to edit the contacts saved in the class Person"""
    
    YES = {'yes', 'y', 'ye'}

    contact_id = input('Which contact do you want to edit? ')
    
    try:
        contact_id = int(contact_id)

    except er as Exception:
        print(er)

    change = input("What do you want to edit in contact {}? ".format(contact_id)).lower()
    if change == 'email' or d == 'email address':
        new_email = input("Digit the new email address: ")
        db[contact_id].new_email(new_email)
        
    elif change == 'phone' or d == 'phone number':
        new_phone = input("Digit the new phone number: ")
        db[contact_id].newphone(new_phone)

    else:
        print('Invalid value, try again!')
        edit_contact()
        return
    

    user_input_choice = input('Do you want to edit another contact? y/N ').lower()

    if user_input_choice in YES:
        edit_contact()
        return
    
    userExit(db)
    return


def add_contact(db):
    """Function to add contacts to the class Person"""
    contacts = input("Enter the number of contacts that you want to add: ")
    try:
        contacts = int(contacts)

    except e as Exception:
        print e
        return
        
    for i in range(0, contacts):
        name = input("Enter the name of the contact {}: ".format(len(db) + 1))
        email = input("Enter the email address of the contact {}: ".format(len(db) + 1))
        phone = input("Enter the phone number of the contact {}: ".format(len(db) + 1))
        db[len(db) + 1] = Person(name, email, person)
        
    userExit(db)
    return


def userExit(db):
    """Function to ask if the user want to do anything else with the program"""
    YES = {'yes', 'y', 'ye'}
    choice = input('Do you want to do anything else? y/N ').lower()

    if choice in yes:
        userChoice(db)
    
    return

def userChoice(db):
    """Function to ask the user what they want to do."""
    
    userChoice = input('What do you want to do? (add, access, edit or EXIT) ').lower()

    if userChoice == 'add':
        add_contact(db)
    elif userChoice == 'access':
        get_access(db)
    elif choice == 'edit':
        edit_contact(db)
    else:
        return

class Database:
    def __init__(self):
        """Start sqlite database in memory"""
        self.memoryDatabase = sqlite3.connect(:memory:)
        self.db = self.memoryDatabase.cursor()


    def save(self):
        """Function to save the data in an sqlite database."""
        YES = ['yes', 'ye', 'y']

        saveDb = input("Do you want to save the contacts? y/N ").lower()
        
        if saveDb in YES:
            con = sqlite3.connect('contacts.db')
            contacts = self.db.execute("SELECT ALL FROM contacts")
            self.db = con.cursor()
            self.db.executemany("INSERT INTO contacts VALUES (?, ?, ?, ?)", contacts)
            con.commit()
            con.close()

        return

    def load():
        """Function to load the previous archived data."""
        con = sqlite3.connect('contacts.db')
        self.db = con.cursor()

    def accessContacts():
        """Function to access a list of all contacts."""

        contacts = self.db.execute("SELECT ALL FROM contacts")

        for i in range(contacts):
            print('Contact {}: '.format(i+1), contact[i].get_name())

        userExit(self)


    def get_access():
        """Function to get the option of the user in which type of access they want."""
    d = input("Do you want to access all contacts or specific contacts? "
              "(a for all, s for specific) ")
    if d == 'a' or d == 'all' or d == 'All':
        access_all_contacts()
    else:
        access_contacts()

def ask_to_save ():
    yes = {'yes', 'y', 'Yes', 'ye', 'Ye'}
    no = {'No', 'no', 'N', 'n', ''}
    choice = input('Do you want to save the values? Y/N ')
    if choice in yes:
        save_archive()
    elif choice in no:
        print ('Choosing that, nothing will be saved!')
        choice_two = input("Are you sure that you don't want to save anything? Y/N ")
        if choice_two in yes:
            print ('Ok! Nothing will be saved')
        elif choice_two in no:
            ask_to_save()
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")
            print()
            ask_to_save()

def ask_to_load ():
    yes = {'yes', 'y', 'Yes', 'ye', 'Ye'}
    no = {'No', 'no', 'N', 'n', ''}
    choice_one = input('Do you want to load any previous version? Y/N ')
    if choice_one in yes:
        load_archive()
    elif choice_one in no:
        print ('Nothing will be loaded')
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        print()
        ask_to_load()

if __name__ = "__main__":
    person = {}
    save = {}
    ask_to_load()
    userChoice(db)
    ask_to_save()
