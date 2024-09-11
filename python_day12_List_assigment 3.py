#3.Write a Python program to find duplicate values from a list and display those
# List of numbers with some duplicates
numbers = [10, 20, 30, 40, 20, 10, 50, 60, 30]

# Create an empty list to store duplicates
duplicates = []

# Loop through the list to find duplicates
for num in numbers:
    # If the number appears more than once and is not already in duplicates
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Print the list of duplicates
print("Duplicate values in the list are:", duplicates)

#OUTPUT
#Duplicate values in the list are: [10, 20, 30]
       
