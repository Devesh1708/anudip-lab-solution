"""3. Write a Python program to reverse words in a string 
String = “Deeptech Python Training”"""

# Given string
string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the list of words
words_reversed = words[::-1]

# Join the reversed words back into a string
reversed_string = " ".join(words_reversed)

# Print the result
print(reversed_string)

#OUTPUT
#Training Python Deeptech
