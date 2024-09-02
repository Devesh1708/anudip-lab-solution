"""2. Write a Python program to remove a newline in Python

 String = "\nBest \nDeeptech \nPython \nTraining\n" """

# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines using the replace method
string_no_newlines = string.replace("\n", " ")

# Alternatively, you can remove newlines and strip leading/trailing spaces
string_no_newlines = string.replace("\n", " ").strip()

# Print the result
print(string_no_newlines)

#OUTPUT
#Best  Deeptech  Python  Training
