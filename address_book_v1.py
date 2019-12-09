# Command-line address-book program
import pickle
import sys


class Person:
    """A class to archive information about the people, such as name, email address and phone number."""

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        print()
        print("Added person {} to the list".format(self.name))
        print()

    def newemail(self, nemail):
        """Change the email address."""
        if nemail == self.email:
            print('The new email is the same as the old one!')
            z = input("Digit a new email address: ")
            self.newemail(z)
        else:
            self.email = nemail
            print('The new email is:', nemail)

    def newphone(self, nphone):
        """Change the phone number"""
        if nphone == self.phone:
            print('The new phone number is the same as the old one!')
            y = input('Digit a new phone number: ')
            self.newphone(y)
        else:
            self.phone = nphone
            print('The new phone number is:', nphone)

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
    while True:
        inicial_access = input('Which contact do you want to access? ')
        person[int(inicial_access)].info()
        yes = {'yes', 'y', 'Yes', 'ye', 'Ye'}
        no = {'No', 'no', 'N', 'n', ''}
        choice = input('Do you want to access any other contact? Y/N ')
        if choice in yes:
            continue
        elif choice in no:
            dyw()
            break
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")
    return


def edit_contact():
    """Function to edit the contacts saved in the class Person"""
    while True:
        c = input('Which contact do you want to edit? ')
        d = input("What do you want to edit in contact {}? ".format(c))
        if d == 'email' or d == 'email address':
            e = input("Digit the new email address: ")
            person[int(c)].newemail(e)
        elif d == 'phone' or d == 'phone number':
            e = input("Digit the new phone number: ")
            person[int(c)].newphone(e)
        else:
            print('Invalid value, try again!')
            continue
        yes = {'yes', 'y', 'Yes', 'ye', 'Ye'}
        no = {'No', 'no', 'N', 'n', ''}
        choice = input('Do you want to edit another contact? Y/N ')
        if choice in yes:
            continue
        elif choice in no:
            dyw()
            break
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")
            print()
    return


def add_contact():
    """Function to add contacts to the class Person"""
    global person
    global save
    c = input("Enter the number of contacts that you want to add: ")
    for contact in range(1, int(c) + 1):
        n = input("Enter the name of the contact {}: ".format(len(person) + 1))
        e = input("Enter the email address of the contact {}: ".format(len(person) + 1))
        p = input("Enter the phone number of the contact {}: ".format(len(person) + 1))
        person[len(person) + 1] = Person(n, e, p)
        save[len(save) + 1] = (n, e, p)
    dyw()
    return


def dyw():
    """Function to ask if the user want to do anything else with the program"""
    yes = {'yes', 'y', 'Yes', 'ye', 'Ye'}
    no = {'No', 'no', 'N', 'n', ''}
    choice = input('Do you want to do anything else? Y/N ')
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

person = {}
save = {}
ask_to_load()
wywtd()
ask_to_save()
