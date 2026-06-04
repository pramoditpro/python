#We use functions to break up our code into small chunks.
#These chunks are easier to read, understand and maintain.
#If there are bugs, it's easier to find bugs in a small chunk
#than the entire program. We can also re-use these chunks.


def first_function():
    print("This is the first function!")

def second_function():
    return 5

## Python — positional (argument order matters)
def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


## Python — first_name, last_name, age are PARAMETERS — placeholders in definition
def greet_user_no_order(first_name, last_name, age):
    print(f"Hello, {first_name} {last_name}! You are {age} years old.")


first_function()  # Output: This is the first function!
result = second_function()  # result will be assigned the value returned by second_function()
print(result)  # Output: 5  

#Parameters are placeholders for the data we can pass to functions. 
#Arguments are the actual values we pass.

#We have two types of arguments:
#1. Positional arguments: their position (order) matters - we must pass them in the same order as the parameters are defined.
greet_user("Pramod", "Chouhan") # we are passing two arguments here


# Without keyword args — you must remember exact order!
# With keyword args — self-documenting, order-independent!
#2. Keywords arguments: position doesn’t matter - we prefix them with the parameter name.
greet_user_no_order(first_name="Pramod", last_name="Chouhan", age=40)   # ✅ Normal order
greet_user_no_order(age=40, first_name="Pramod", last_name="Chouhan")   # ✅ Different order
greet_user_no_order(last_name="Chouhan", age=40, first_name="Pramod")   # ✅ Any order!
greet_user_no_order("Pramod", last_name="Chouhan", age=40)   # ✅ mix order is also fine

greet_user(first_name="Pramod", last_name="Chouhan") 
greet_user( last_name="Chouhan",first_name="Pramod") 
#Think of keyword arguments as named parameters — Python knows exactly which slot to fill based on the name, not the position! 😊


#Our functions can return values. If we don't use the return statement, by default None
#is returned. None is an object that represents the absence of a value.

result = greet_user("Pramod", "Chouhan")  # This will print the greeting but return None
print(result)  # Output: None

def do_something():
    print("Doing something...")
    return None             # same as writing no return statement at all

result = do_something()
print(result)               # None

# None is a real OBJECT in Python — not null, not 0, not empty string!
print(None)             # None
print(type(None))       # <class 'NoneType'>

# None has its own type — NoneType
# There is ONLY ONE None object in all of Python (Singleton!)

# Checking for None — always use "is", not "=="
def get_something():
    # Imagine this function does some work and might return a value or None
    return None  # or return "A value" to test the other case

result = get_something()

if result is None:
    print("Nothing was returned!")
else:
    print("Got a value:", result)


###################### Python can return MULTIPLE values!

def get_user_details():
    name = "Pramod"
    age = 40
    city = "Noida"
    return name, age, city      # returns 3 values!

# Unpack all 3
name, age, city = get_user_details()
print(name)     # Pramod
print(age)      # 40
print(city)     # Noida

# Or capture as a tuple
details = get_user_details()
print("Details: " + str(details))          # ('Pramod', 40, 'Noida')
print("Detail 1: " + details[0])       # Pramod





