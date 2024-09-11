"""1.Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} """

# Dictionary of values
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Extract all the values from the dictionary
values = test_dict.values()

# Calculate the sum of the values
total_sum = sum(values)

# Calculate the number of elements (i.e., how many values)
num_elements = len(values)

# Calculate the mean (average)
mean = total_sum / num_elements

# Print the result
print("The mean of the values is:", mean)

#OUTPUT
"""The mean of the values is: 6.2"""


