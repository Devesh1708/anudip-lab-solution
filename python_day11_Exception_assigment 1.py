#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers():
    try:
        # Taking input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Attempt to divide
        result = numerator / denominator
        
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
        
    except ValueError:
        # Handle invalid input (non-numeric)
        print("Error: Please enter valid numeric values.")
        
    else:
        # If no exceptions occur, print the result
        print(f"The result is: {result}")

# Call the function
divide_numbers()

#OUTPUT
"""Enter the numerator: 10
Enter the denominator: 0
Error: Division by zero is not allowed."""
