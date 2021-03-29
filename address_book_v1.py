# Command-line address-book program
import pickle
import sys


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


def access_contacts():
    """Function to access the specific contacts saved in the class Person."""
    
    YES = {'yes', 'y', 'ye'}

    inicial_access = input('Which contact do you want to access? ')
    person[int(inicial_access)].info()
        
    user_input_choice = input('Do you want to access any other contact? y/N ').lower()

    if user_input_choice in YES:
        access_contacts()
        return

    dyw()
    return


def edit_contact():
    """Function to edit the contacts saved in the class Person"""
    
    YES = {'yes', 'y', 'ye'}

    contact = input('Which contact do you want to edit? ')
    change = input("What do you want to edit in contact {}? ".format(contact)).lower()
    if change == 'email' or d == 'email address':
        new_email = input("Digit the new email address: ")
        person[int(contact)].new_email(new_email)
    elif change == 'phone' or d == 'phone number':
        new_phone = input("Digit the new phone number: ")
        person[int(contact)].newphone(new_phone)
    else:
        print('Invalid value, try again!')
        edit_contact()
        return
    

    user_input_choice = input('Do you want to edit another contact? y/N ').lower()

    if user_input_choice in YES:
        edit_contact()
        return
    
    dyw()
    return


def add_contact():
    """Function to add contacts to the class Person"""
    global person
    global save
    contacts = input("Enter the number of contacts that you want to add: ")
    try:
        contacts = int(contacts)

    except e as Exception:
        print e
        return
        
    for contact in range(0, contacts):
        name = input("Enter the name of the contact {}: ".format(len(person) + 1))
        email = input("Enter the email address of the contact {}: ".format(len(person) + 1))
        phone = input("Enter the phone number of the contact {}: ".format(len(person) + 1))
        person[len(person) + 1] = Person(name, email, person)
        save[len(save) + 1] = (name, email, person)
        
    dyw()
    return


def dyw():
    """Function to ask if the user want to do anything else with the program"""
    YES = {'yes', 'y', 'ye'}
    choice = input('Do you want to do anything else? y/N ').lower()

    if choice in yes:
        wywtd()
    elif choice in no:
        return
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        print()
        dyw()


def wywtd ():
    """Function to ask the user what they want to do."""
    choice = input('What do you want to do? (add, access, edit or exit) ')
    if choice == 'add' or choice == 'Add':
        add_contact()
    elif choice == 'access' or choice == 'Access':
        get_access()
    elif choice == 'edit' or choice == 'Edit':
        edit_contact()
    elif choice == 'exit' or choice == 'Exit':
        return
    else:
        print('Invalid option, try again!')
        wywtd()


def save_archive():
    """Function to save the data."""
    global person
    save_yn = input('Do you want to save the raw data? Y/N ')
    if save_yn == 'y' or save_yn == 'Y':
        global save
        file_name = 'backup_raw_data.txt'
        file_object = open(file_name, 'w')
        file_object.write(str(save))
        file_object.close()
    file_name1 = 'backup.data'
    file_object1 = open(file_name1, 'wb')
    pickle.dump(person, file_object1)
    file_object1.close()


def load_archive():
    """Function to load the previous archived data."""
    global person
    global save
    try:
        infile = open('backup.data', 'rb')
        person = pickle.load(infile)
        infile.close()
        try:
            with open('backup_raw_data.txt') as f:
                save = f
        except:
            print('ERROR in loading raw data')
            print('New archive being created!')
            return

    except:
        print('ERROR in loading')
        print('New archive being created!')
        return


def access_all_contacts():
    """Function to access a list of all contacts."""
    global person
    for i in range(1, len(person) + 1):
        print('Contact {}: '.format(i), person[i].get_name())
    dyw()


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
    wywtd()
    ask_to_save()
