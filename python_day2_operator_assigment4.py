#4. Python program to find the area of a triangle whose sides are given

import math
a=3
b=4
c=5
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
area = triangle_area(a, b, c)
print("The area of the triangle is:",area)

#Area of the traingle is 6.0 units
