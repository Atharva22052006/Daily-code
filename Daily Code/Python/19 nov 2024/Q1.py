# Modules and Functions:

# Write a program that uses the math module to calculate the area and circumference of a circle given its radius. Create a separate function to handle user input and validation.

import math

r=int(input("Enter Radius of Circle: "))

def circumference():
    c=2*r*math.pi
    print(f"Your Circumference is: {c:.2f}")
    return 

def area():
    a=math.pi*r*r
    print(f"Your Area is: {a:.2f}")
    return 

circumference()
area()