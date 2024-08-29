#2.Write a python program finding the factorial of a given number using a while loop

def factorial(n):
    # Initialize result to 1 (factorial of 0 or 1 is 1)
    result = 1
    
    # Check for non-negative integer input
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Calculate factorial using a while loop
    while n > 0:
        result *= n  # Multiply result by the current number
        n -= 1       # Decrement the number by 1
    
    return result

# Input from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
fact = factorial(num)
print(f"The factorial of {num} is {fact}.")

#OUTPUT
'''Enter a number: 5
The factorial of 5 is 120.'''
