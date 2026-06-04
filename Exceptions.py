#Exceptions are errors that crash our programs.
#They often happen because of bad input or programming errors. 
# It’s our job to anticipate and handle these exceptions to prevent our programs from crashing.

#When something goes wrong at runtime, Python stops the program and raises an Exception. If you don't handle it — the program crashes.
#Example of an unhandled exception:
# This program CRASHES — unhandled exception
number = int(input("Enter a number: "))   # User types "hello"
print(10 / number)                         # User types 0

# Python throws:
# ValueError  — if user types "hello" (bad input) [as integer value is expected but string is given]
# ZeroDivisionError — if user types 0 (programming logic error)

user = {"name": "Pramod", "city": "Noida"}

# Key "age" doesn't exist!
#print(user["age"])
print(user["city"])  # This line will never be reached due to the exception on the previous line

# Output:
# KeyError: 'age'



################### Real Python Code with Exception Handling
def divide(a, b):
    try:
        result = a / b                          # might crash if b=0

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
        return None

    else:
        print(f"✅ Result = {result}")           # only runs if no error
        return result

    finally:
        print("➡️ divide() function finished")   # always runs


# Test 1 — Normal case
divide(10, 2)
# ✅ Result = 5.0
# ➡️ divide() function finished

# Test 2 — Bad input
divide(10, 0)
# ❌ Error: Cannot divide by zero!
# ➡️ divide() function finished

