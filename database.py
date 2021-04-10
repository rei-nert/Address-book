import sqlite3

class Database:
    def __init__(self):
        """Start sqlite database in memory"""
        self.con = sqlite3.connect(":memory:")
        self.db = self.con.cursor()
        self.db.execute("""CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT)""")
        self.con.commit()

    def __del__(self):
        self.con.commit()
        self.con.close()


    def createDb(self):
        con = sqlite3.connect('./contacts.sqlite')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT)""")
        con.commit()
        con.close()

    def insertContact(self, name, email, phone):
        self.db.execute("""INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)""", (name, email, phone))
        return

    def save(self):
        """Function to save the data in an sqlite database."""
        YES = ['yes', 'ye', 'y']

        saveDb = input("Do you want to save the contacts? y/N ").lower()

        if saveDb in YES:
            self.createDb()
            contacts = self.db.execute("SELECT ALL FROM contacts")
            self.con = sqlite3.connect('./contacts.sqlite')
            self.db = con.cursor()
            self.db.executemany("INSERT INTO contacts VALUES (?, ?, ?, ?)", contacts)
            self.con.commit()

        return

    def load(self):
        """Function to load the previous archived data."""
        self.con = sqlite3.connect('./contacts.sqlite')
        self.db = con.cursor()

    def accessContacts(self):
        """Function to access a list of all contacts."""

        self.db.execute("SELECT ALL id FROM contacts")
        contacts = self.db.fetchone()
        print(contacts)

        for id in range(1, len(contacts)+1):
            self.info(id)

        userExit(self)
        return


    def acessSpecificContact(self):
        """Function to get the specific contact"""
        userId = input("Type the user id: ")

        try: 
            userId = int(userId)
        except e as Exception:
            print(e)
            return

        self.info(userId)
        return

    def get_access(self):
        """Function to get the option of the user in which type of access they want."""
        userChoice = input("Do you want to access all contacts or specific contacts? (a for all, s for specific) ").lower()
        if userChoice == 'a' or userChoice == 'all':
            self.accessContacts()
        else:
            self.acessSpecificContacts()
        return


    def info(self, id):
        self.db.execute("SELECT * FROM contacts WHERE id=?", (id, ))
        contact = self.db.fetchone()
        print(contact)
        return

    def changeEmail(self, id, email):
        self.db.execute("""UPDATE FROM contacts SET email=? WHERE id=?""", (email, id))
        return

    def changePhone(self, id, phone):
        self.db.execute("""UPDATE FROM contacts SET phone=? WHERE id=?""", (phone, id))
        return

    def changeName(self, id, name):
        self.db.execute("""UPDATE FROM contacts SET name=? WHERE id=?""", (name, id))
        return

