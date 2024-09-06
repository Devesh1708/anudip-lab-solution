#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

# Open the file in read mode
with open("ABC.txt", "r") as file:
    # Read the file line by line
    for line in file:
        # Print each line
        print(line.strip())
    # Close the file
    file.close()

#OUTPUT
"""Hello, Mam!
My name is devesh"""
