#2.Python program to check if a given number is an Armstrong number
def is_armstrong_number(number):
    # Convert number to string to iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Example usage
input_number = int(input("Enter a number to check: "))
if is_armstrong_number(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")

#OUTPUT
'''Enter a number to check: 153
153 is an Armstrong number.'''
