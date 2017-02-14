import pickle

class Phonebook(object):
    def __init__(self):
        self.phonebook_dict = {}

    def lookup_name(self):
        name = raw_input("Enter the name you'd like to look up: ")
        print "%s's phone number is %s." % (name, self.phonebook_dict.get(name, "not listed"))

    def set_entry(self):
        name = raw_input("Name: ")
        number = raw_input("Phone Number: ")
        self.phonebook_dict[name] = number
        print "Entry stored for %s." % name

    def delete_entry(self):
        name = raw_input("Delete who? ")
        if name not in self.phonebook_dict:
            print "No listing for %s." % name
        else:
            del self.phonebook_dict[name]
            print "Deleted entry for %s." % name

    def list_entries(self):
        for key, value in self.phonebook_dict.items():
            print "%s: %s" % (key, value)
        if self.phonebook_dict == {}:
            print "No phonebook entries, try restoring a saved Phonebook (6)"

    def save_entries(self):
        myfile = open("phonebook.pickle", "w")
        pickle.dump(self.phonebook_dict, myfile)
        myfile.close()
        print "Entries saved to phonebook.pickle"

    def restore_entries(self):
        myfile = open("phonebook.pickle", "r")
        self.phonebook_dict = pickle.load(myfile)
        myfile.close()
        print "Restored saved entries."

    def quit(self):
        print "Bye."

    def main(self):
        instructions = """
Electronic Phone Book
======================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit """
        print instructions
        while True:
            try:
                choice = raw_input("""
What do you want to do (1 - 7)?
Type "help" to see the menu.
> """)
            except ValueError:
                print "That's not a valid input, try again."
                continue

            if choice == "1":
                self.lookup_name()
            elif choice == "2":
                self.set_entry()
            elif choice == "3":
                self.delete_entry()
            elif choice == "4":
                self.list_entries()
            elif choice == "5":
                self.save_entries()
            elif choice == "6":
                self.restore_entries()
            elif choice == "7":
                self.quit()
                break
            elif choice == "help":
                print instructions
            else:
                print "Not a valid choice, try again."

julies_phonebook = Phonebook()
julies_phonebook.main()
