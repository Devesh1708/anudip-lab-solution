'''2. Convert the below list into a numpy array then display the array then display the first
and last index and then multiply each element by 2 and display the result.
Input: my_list = [1, 2, 3, 4, 5]'''

#importing numpy library as np
import numpy as np
my_list = [1, 2, 3, 4, 5]
#converting the list into array
arr=np.array([1, 2, 3, 4, 5])
#displaying the array
print(arr)
#displaying the first and the last index value
print("first index value",arr[0])
print("last index value",arr[-1])
#displaying the multiplication of each element by 2 in an array
print(arr*2)

#OUTPUT
'''[1 2 3 4 5]
first index value 1
last index value 5
[ 2  4  6  8 10]'''

