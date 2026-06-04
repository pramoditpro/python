#input string will directly assign to the name variable and we can use it as a string without any conversion
name = input("What we input is -by default a string : Enter your name: ")
#We can use formatted strings to dynamically insert values into our strings. 
# Formatted strings are created by prefixing a string with the letter 'f' and 
# using curly braces {} to include variables or expressions that we want to be 
# evaluated and included in the string.
print(f"Hello, {name}!")

message = f"Hello, {name}! Welcome to the world of Python programming."
print(message)

print(message.find("Python"))  # Output: 39 (the starting index of "Python" in the message)



smallName = name[1:2] # slicing the string to get the second character
print("Slice of input name is : "+ smallName)
smallName = name[:2] # slicing the string to get the second character
print("Slice of input name is : "+ smallName)
smallName = name[1:] # slicing the string to get the second character
print("Slice of input name is : "+ smallName)