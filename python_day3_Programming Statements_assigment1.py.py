#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

num=int(input("Enter a number:")) # Using input() function take one number from the user
result="Number is even" if num%2==0 else "Number is odd"  #using iternary operator
print(result)

#Output
"""Enter a number:5
Number is odd

Enter a number:4
Number is even"""
