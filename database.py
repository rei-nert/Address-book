import sqlite3

class Database:
    def __init__(self):
        """Start sqlite database in memory"""
        self.memoryDatabase = sqlite3.connect(:memory:)
        self.db = self.memoryDatabase.cursor()


    def createDb(self):
        con = sqlite3.connect('./contacts.sqlite')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT)""")
        con.commit()
        con.close()

    def save(self):
        """Function to save the data in an sqlite database."""
        YES = ['yes', 'ye', 'y']

        saveDb = input("Do you want to save the contacts? y/N ").lower()
        
        if saveDb in YES:
            self.createDb()
            con = sqlite3.connect('./contacts.sqlite')
            contacts = self.db.execute("SELECT ALL FROM contacts")
            self.db = con.cursor()
            self.db.executemany("INSERT INTO contacts VALUES (?, ?, ?, ?)", contacts)
            con.commit()
            con.close()

        return

    def load(self):
        """Function to load the previous archived data."""
        con = sqlite3.connect('./contacts.sqlite')
        self.db = con.cursor()

    def accessContacts(self):
        """Function to access a list of all contacts."""

        contacts = self.db.execute("SELECT ALL FROM contacts")

        for i in range(contacts):
            print('Contact {}: '.format(i+1), contact[i].get_name())

        userExit(self)


    def acessSpecificContact(self):
        """Function to get the specific contact"""
        userId = input("Type the user id: ")
        
        try: 
            userId = int(userId)
        except e as Exception:
            print(e)
            return
        
        user = self.db.execute("SELECT * FROM contacts WHERE id=?",  userId)
        print(user)
        return

    def get_access(self):
        """Function to get the option of the user in which type of access they want."""
    d = input("Do you want to access all contacts or specific contacts? (a for all, s for specific) ").lower()
    if d == 'a' or d == 'all':
        self.accessContacts()
    else:
        self.acessSpecificContacts()
