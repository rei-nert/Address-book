# Command-line address-book program
import pickle


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


def access_contacts():
    """Function to access the contacts saved in the class Person."""
    while True:
        a = input('Which contact do you want to access? ')
        person[int(a)].info()
        b = input('Do you want to access any other contact? Y/N ')
        if b == 'Y' or b == 'y':
            continue
        else:
            dyw()
            break
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
        l = input('Do you want to edit another contact? Y/N ')
        if l == 'y' or l == 'Y':
            continue
        dyw()
        break
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
    w = input('Do you want to do anything else? Y/N ')
    if w == 'y' or w == 'Y':
        while True:
            h = input('What do you want to do? (add, access or edit) ')
            if h == 'add' or h == 'Add':
                add_contact()
            elif h == 'access' or h == 'Access':
                access_contacts()
            elif h == 'edit' or h == 'Edit':
                edit_contact()
            else:
                print('Invalid option, try again!')
    else:
        return


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


person = {}
save = {}
a = input('Do you want to load any previous version? Y/N ')
if a == 'y' or a == 'Y':
    load_archive()
add_contact()
b = input('Do you want to save the values? Y/N ')
if b == 'y' or b == 'Y':
    save_archive()
