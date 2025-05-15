# Homework - 1 
# Task - 1

side = float(input("Enter the side length of the square: "))

perimeter = 4 * side
area = side * side  

print("Perimeter of the square:", perimeter)
print("Area of the square:", area)

# Task - 2
import math

diameter = float(input("Enter the diameter of the circle: "))

circumference = math.pi * diameter

print("Circumference (Length) of the circle:", circumference)

# Task - 3

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

mean = (a + b) / 2

print("Mean of", a, "and", b, "is:", mean)

# Task - 4

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print("Sum of a and b:", sum_ab)
print("Product of a and b:", product_ab)
print("Square of a:", square_a)
print("Square of b:", square_b)
