"""2.Write a Python script to concatenate the following dictionaries to create a new one. 
Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating all the dictionaries
new_dict = {}

# Update the new dictionary with the key-value pairs from each dictionary
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

# Print the result
print("The concatenated dictionary is:", new_dict)

#OUTPUT
#The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
