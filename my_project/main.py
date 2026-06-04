# main.py — using our modules

# -----------------------------------------------
# WAY 1: import the entire module
# Like Java's: import com.company.MathUtils;
# -----------------------------------------------
import math_utils # imports everything from module -> math_utils.py

print(math_utils.add(10, 20))           # 30
print(math_utils.circle_area(5))        # 78.53975
print(math_utils.PI)                    # 3.14159


# -----------------------------------------------
# WAY 2: import specific functions only
# Like Java's: import com.company.MathUtils.add;
# -----------------------------------------------
from math_utils import add, divide

print(add(10, 20))                      # 30  — no prefix needed!
print(divide(100, 4))                   # 25.0


# -----------------------------------------------
# WAY 3: import with an alias (nickname)
# Very common in Data Science / AI libraries
# -----------------------------------------------
import math_utils as mu
import string_utils as su

print(mu.multiply(5, 6))               # 30
print(su.greet("Pramod"))              # Hello, Pramod!
print(su.count_words("I love Python")) # 3


# -----------------------------------------------
# WAY 4: import everything (NOT recommended!)
# -----------------------------------------------
from string_utils import *              # imports ALL functions

print(make_uppercase("hello"))         # HELLO
print(reverse_string("Pramod"))        # domarP


##################### Python ships with hundreds of ready-to-use modules — no installation needed:
print("############## Python standard library modules:")
# import inbuild math module
import math
print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.141592653589793

# random module
import random
print(random.randint(1, 100))   # random number between 1-100

# datetime module
import datetime
today = datetime.date.today()
print(today)                    # 2026-05-08

# os module — interact with operating system
import os
print(os.getcwd())              # current working directory

# json module — work with JSON data
import json
data = {"name": "Pramod", "city": "Noida"}
json_string = json.dumps(data)
print(json_string)              # {"name": "Pramod", "city": "Noida"}