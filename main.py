# Command-line address-book program
import sqlite3
from contact import Person
from database import Database

def access_contacts(db):
    """Function to access the specific contacts saved in the class Person."""
    
    YES = {'yes', 'y', 'ye'}

    contact_id = input('Which contact do you want to access? ')
    
    try:
        contact_id = int(contact_id)

    except er as Exception:
        print(er)

    db.info(contact_id)
        
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
