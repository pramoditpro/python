# ---- All other functions defined first ----

def greet_user(name):
    print("Hello, " + name + "!")

def print_sum(a, b):
    result = a + b
    print("Sum =", result)
    return result

def print_square(num):
    print("Square =", num ** 2)

def second_main():
    print("from the second main function! ")

    


# ---- Main function — entry point ----

def mainByPramod(user_name="Pramod"):
    print("Testing some features of Python here! welcome to the world of Python programming Mr. " + user_name)
    greet_user("Pramod")
    print_sum(10, 20)
    print_square(5)


# ---- This line runs main() when file is executed ----

if __name__ == "__main__":
    mainByPramod("PramodTester") # you can change the name here to test with different names
    second_main() #we can decide which method will be second