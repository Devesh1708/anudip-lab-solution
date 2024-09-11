#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# List of numbers
numbers = [23, 1, 45, 12, 99, 4, 67]

# Initialize variables for largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Loop through the list to find largest and smallest
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print the result
print("The largest number is:", largest)
print("The smallest number is:", smallest)

#OUTPUT
"""The largest number is: 99
The smallest number is: 1"""


