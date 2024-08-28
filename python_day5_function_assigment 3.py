#3.Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

"""Generate 5 random numbers between 1 and 100
Generates a list of 5 random numbers."""
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated numbers
print("Random numbers:", numbers)

# Find the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Display the maximum and minimum values
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#OUTPUT
"""Random numbers: [99, 58, 10, 69, 22]
Maximum value: 99
Minimum value: 10 """


