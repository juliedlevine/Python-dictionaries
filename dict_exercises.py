#Exercise 1:
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
#
# print phonebook_dict['Elizabeth']
# phonebook_dict["Kareem"] = "938-489-1234"
# del phonebook_dict["Alice"]
# phonebook_dict["Bob"] = '968-345-2345'
# print phonebook_dict

#Execise 2: Nested Dictionaries
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
#
# print ramit["email"]
# print ramit["interests"][0]
# print ramit["friends"][0]["email"]
# print ramit["friends"][1]["interests"][1]

# Letter Summary
# letter_count = {}
#
# def letter_histogram(word):
#     for char in word:
#         current_count = letter_count.get(char, 0)
#         letter_count[char] = current_count + 1
#     print letter_count
#
# letter_histogram("banana")


# Word Summary
# word_count_dict = {}
# def word_histogram(sentence):
#     # make the sentence a list that is iterable
#     sentence_list = sentence.split()
#     # loop over each word in the sentence list
#     for i in sentence_list:
#         # word_count_dict.get() returns value for key [i], if no key exists (ie - new word in the sentence), it will default to a count of 0
#         current_count = word_count_dict.get(i, 0)
#         word_count_dict[i] = current_count + 1
#     print word_count_dict
#
# word_histogram("To be or not to be")


# Bonus
word_count_dict = {}
def word_histogram(sentence):
    sentence_list = sentence.lower().split()
    for i in sentence_list:
        current_count = word_count_dict.get(i, 0)
        word_count_dict[i] = current_count + 1

    sorted_tuples = sorted(word_count_dict.items(), key=lambda x:x[1], reverse = True)

    top_1 = sorted_tuples[0]
    top_2 = sorted_tuples[1]
    top_3 = sorted_tuples[2]

    print "The top 3 most used words are %s, %s, and %s." % (top_1, top_2, top_3)

word_histogram("To be or not to be be be not to or or or or")
