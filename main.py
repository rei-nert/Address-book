# Command-line address-book program
# from contact import Person
from database import Database

def access_contacts(db):
    """Function to access the specific contacts saved in the class Person."""
    
    YES = {'yes', 'y', 'ye'}

    db.get_access()

    user_input_choice = input('Do you want to access any other contact? y/N ').lower()

    if user_input_choice in YES:
        access_contacts(db)

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
    if change == 'email' or change == 'email address':
        new_email = input("Digit the new email address: ")
        db.changeEmail(contact_id, new_email)
        
    elif change == 'phone' or change == 'phone number':
        new_phone = input("Digit the new phone number: ")
        db.changePhone(contact_id, new_phone)

    elif change == 'name':
        newName = input("Digit the new name: ")
        db.changeName(contact_id, newName)
    else:
        print('Invalid value, try again!')
        edit_contact(db)
        return
    
    user_input_choice = input('Do you want to edit another contact? y/N ').lower()

    if user_input_choice in YES:
        edit_contact(db)
        return
    
    userExit(db)
    return


def add_contacts(db):
    """Function to add contacts to the database"""
    contacts = input("Enter the number of contacts that you want to add: ")
    try:
        contacts = int(contacts)

    except e as Exception:
        print(e)
        return
        
    for i in range(1, (contacts+ 1)):
        name = input("Enter the name of the contact {}: ".format(i))
        email = input("Enter the email address of the contact {}: ".format(i))
        phone = input("Enter the phone number of the contact {}: ".format(i))
        db.insertContact(name, email, phone)
        
    userExit(db)
    return


def userExit(db):
    """Function to ask if the user want to do anything else with the program"""
    YES = {'yes', 'y', 'ye'}
    choice = input('Do you want to do anything else? y/N ').lower()

    if choice in YES:
        userChoice(db)
    
    return

def userChoice(db):
    """Function to ask the user what they want to do."""
    
    userChoice = input('What do you want to do? (add, access, edit or EXIT) ').lower()

    if userChoice == 'add':
        add_contacts(db)
    elif userChoice == 'access':
        access_contacts(db)
    elif userChoice == 'edit':
        edit_contact(db)
    else:
        return


def ask_to_save(db):
    db.save()

def ask_to_load(db):
    yes = {'yes', 'y', 'ye'}
    choice_one = input('Do you want to load any previous version? y/N ').lower()
    if choice_one in yes:
        db.load()
    else:    
        print ('Nothing will be loaded')

    return

if __name__ == "__main__":
    database = Database()
    ask_to_load(database)
    userChoice(database)
    ask_to_save(database)
