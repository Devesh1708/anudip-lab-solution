# 2. Using input function take two number and then swap the number

# Taking input from the user
a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
#Displaying the original Numbers
print("Original Numbers: a =",a,"b =",b)
#Swapping the numbers
a,b=b,a
#Display the swapped numbers
print("Swapped Numbers:a = ",a,"b =",b)

#OUTPUT
"""Enter number a:5
Enter number b:10
Original Numbers: a = 5 b = 10
Swapped Numbers:a =  10 b = 5"""
