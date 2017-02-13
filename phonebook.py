phonebook = {
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

while True:
    print instructions
    choice = int(raw_input("What do you want to do (1 - 5)? "))

    if choice == 1:
        lookup_name = raw_input("Enter the name you'd like to look up: ")
        print "Julie's phone number is %s." % phonebook[lookup_name]
    elif choice == 2:
        set_name = raw_input("Name: ")
        set_number = raw_input("Phone Number: ")
        print "Entry stored for %s." % set_name
    elif choice == 3:
        delete_name = raw_input("Delete who? ")
        del phonebook[delete_name]
        print "Deleted entry for %s." % delete_name
    elif choice == 4:
        for key, value in phonebook.items():
            print "%s: %s" % (key, value)
    elif choice == 5:
        print "Bye."
        break
