import dict_exercises
# # Exercise 1
# file_name = raw_input("Enter a file name: ")
#
# myfile = open(file_name)
# file_contents = myfile.read()
# myfile.close()
#
# print file_contents
#
#
# # Exercise 2
# import pickle
#
# file_name = raw_input("Enter a file name: ")
# file_contents = raw_input("Enter contents for the file: ")
#
# myfile = open(file_name, "w")
# myfile.write(file_contents)
# myfile.close()
#
# print "File saved!"


# Exercise 3
file_name = raw_input("Enter a file name: ")

myfile = open(file_name)
file_contents = myfile.read()
dict_exercises.word_histogram(file_contents)
myfile.close()
