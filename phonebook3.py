import pickle

phonebook_dict = {
    'Julie': '504-616-9063',
    'Blake': '770-873-4404',
    'Aaron': '555-124-3452',
    'Amos': '555-142-4929',
    'Toby': '555-993-1945',
    'Autumn': '555-134-2225'
}

instructions = """
Electronic Phone Book
======================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit """

# Restore entries from previous program run
myfile = open("phonebook.pickle", "r")
phonebook_dict = pickle.load(myfile)
myfile.close()
print "Restored saved entries."

while True:
    print instructions
    try:
        choice = int(raw_input("What do you want to do (1 - 5)? "))
    except ValueError:
        print "That's not a valid input, try again."
        continue

    if choice == 1:
        lookup_name = raw_input("Enter the name you'd like to look up: ")
        print "%s's phone number is %s." % (lookup_name, phonebook_dict.get(lookup_name, "not listed"))

    elif choice == 2:
        set_name = raw_input("Name: ")
        set_number = raw_input("Phone Number: ")
        phonebook_dict[set_name] = set_number
        print "Entry stored for %s." % set_name

    elif choice == 3:
        delete_name = raw_input("Delete who? ")
        if delete_name not in phonebook_dict:
            print "No listing for %s." % delete_name
        else:
            del phonebook_dict[delete_name]
            print "Deleted entry for %s." % delete_name

    elif choice == 4:
        for key, value in phonebook_dict.items():
            print "%s: %s" % (key, value)

    elif choice == 5:
        # Save entries after each program run
        myfile = open("phonebook.pickle", "w")
        pickle.dump(phonebook_dict, myfile)
        myfile.close()
        print "Entries saved to phonebook.pickle"
        print "Bye."
        break

    else:
        print "Not a valid choice, try again."
