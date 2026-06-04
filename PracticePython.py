
print("Testing some features of Python here!") 

print(5 ** 2)   # 5 squared
print(2 ** 7)   # 2 to the power of 7

a = 5
b = 2
print("Before swap: a = " + str(a) + ", b = " + str(b)   + ", a to the power of b = " + str(a ** b))

a , b = b , a
print("After swap: a = " + str(a) + ", b = " + str(b)   + ", a to the power of b = " + str(a ** b))

# for Interective mode use Python IDLE
# to open IDLE - window key + type [Python] > IDLE[Python...] is displayed

squares = [1, 4, 9, 'a', 25]
print(squares[-3])   # third from back side = 9

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

    ############ For loop
    # Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))




# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(status)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for w in active_users:
    print(w, len(w))


    ######### match case
    print("going to test the match")

    def http_error(status):
     match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# Slice Examples
