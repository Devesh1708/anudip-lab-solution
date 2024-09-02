#1.Python program to check if the given string is a palindrome
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitivity
    length = len(s)
    
    # Loop through the string up to the middle
    for i in range(length // 2):
        # Compare characters from start and end
        if s[i] != s[length - i - 1]:
            return False  # Not a palindrome
    
    return True  # String is a palindrome

# Example usage
input_string = input("Enter a string to check: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

#OUTPUT
'''Enter a string to check: amma
'amma' is a palindrome.  '''  
