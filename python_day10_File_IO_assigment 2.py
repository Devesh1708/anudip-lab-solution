#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
# Open the file in read mode
file = open('ABC.txt', 'r')

# Initialize the word count
word_count = 0

# Loop through each line in the file
for line in file:
    # Split the line into words
    words = line.split()
    # Count the number of words in the line and add to the total count
    word_count += len(words)

# Close the file
file.close()

# Display the total number of words
print("Total number of words:", word_count)

#OUTPUT
#Total number of words: 6

