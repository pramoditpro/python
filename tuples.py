#They are like read-only lists. We use them to store a list of
#items. But once we define a tuple, we cannot add or remove
#items or change the existing items.

coordinates = (10.0, 20.0)  # A tuple representing a point in 2D space
print(coordinates)  # Output: (10.0, 20.0)

coordinates = (10.0, 20.0, 30.0)  # A tuple representing a point in 3D space
print(coordinates)  # Output: (10.0, 20.0, 30.0)

x, y, z = coordinates  # Unpacking the tuple into individual variables
print("x =", x)  # Output: x = 10.0
print("y =", y)  # Output: y = 20.0
print("z =", z)  # Output: z = 30.0 

# Tuples can also be used to return multiple values from a function
def get_coordinates():
    return (10.0, 20.0) # Returning a tuple

x, y = get_coordinates()  # Unpacking the returned tuple
print("x =", x)  # Output: x = 10.0     
print("y =", y)  # Output: y = 20.0

