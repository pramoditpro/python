# math_utils.py
# This file IS a module — no special declaration needed!

# A module-level variable
PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def circle_area(radius):
    return PI * radius ** 2