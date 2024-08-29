#1.Write a python program to check whether a number is palindrome or not?

def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        # Get the last digit of the number
        digit = number % 10
        # Build the reversed number
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the number
        number = number // 10

    # Compare the original number with the reversed number
    return original_number == reversed_number

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#OUTPUT
 '''Enter a number: 121
121 is a palindrome.  ''' 

