#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not
#a valid integer.

def get_integer_input():
    try:
        # Prompt the user to input an integer
        user_input = input("Enter an integer: ")
        
        # Attempt to convert the input to an integer
        number = int(user_input)
        print(f"You entered the integer: {number}")
        
    except ValueError:
        # Raise a ValueError if the input is not a valid integer
        raise ValueError("Invalid input! Please enter a valid integer.")

# Call the function
try:
    get_integer_input()
except ValueError as e:
    print(e)

#OUTPUT
"""Enter an integer: devesh
Invalid input! Please enter a valid integer."""
