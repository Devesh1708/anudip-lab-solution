"""1. Write a Python program to count the occurrences of each word in a given sentence 

string = “To change the overall look of your document. To change the look available in the gallery”"""

# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase to make the word count case-insensitive
string = string.lower()

# Replace the period with an empty space
string = string.replace(".", "")

# Split the string into words
words = string.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1  # If the word is already in the dictionary, increment its count
    else:
        word_count[word] = 1  # If the word is not in the dictionary, add it with a count of 1

# Print the word count
for word in word_count:
    print(word, ":", word_count[word])

#OUTPUT
"""to : 2
change : 2
the : 3
overall : 1
look : 2
of : 1
your : 1
document : 1
available : 1
in : 1
gallery : 1"""
