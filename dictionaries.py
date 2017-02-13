oxford = {
    "word": "definition",
    "word2:": "definition"
}

# entries is now a list
entries = oxford.items()

# dictionary for loops
for key, value in oxford.items():
for key, value in entries:

# get all keys
oxford.keys()

# dynamic keys example (keys not defined yet)
word = "shfhalksjabdckelfjwij;alsjdflkskem"
counts = {}
for char in word:
    current_count = counts.get(char, 0)
    counts[char] = current_count + 1

# if value of char is not found in the dictionary, it will return a key error. Example:
# counts[char]

# instead, use .get() which will default to 0 if the key does not exist
# counts.get(char, 0)
