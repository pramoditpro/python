#We use dictionaries to store key / value pairs.
#constraints on keys:
#- Keys must be unique within a dictionary. If you try to use a key that already exists, 
# the old value will be overwritten.
#- Keys must be immutable (cannot be changed). This means you can use strings, 
# numbers, or tuples as keys, but not lists or other dictionaries. 
#- Values can be of any data type and can be duplicated across different keys.
# We can use strings or numbers to define keys. They
#should be unique. We can use any types for the values. 
# Create a dictionary with string keys and integer values
my_dict = { "apple": 1, "banana": 2, "orange": 3}
print(my_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}    

# Create a dictionary with integer keys and string values
my_dict = { 1: "one", 2: "two", 3: "three"}
print(my_dict)  # Output: {1: 'one', 2: 'two', 3: 'three'}  

# Create a dictionary with mixed keys and values - Like Employee details
employee_dict = {   "name": "John Doe",
    "age": 30,
    "position": "Software Engineer",
    "is_full_time": True,
    "skills": ["Python", "Java", "C++"]
}

print(employee_dict)  # Output: {'name': 'John Doe', 'age': 30, 'position': 'Software Engineer', 'is_full_time': True, 'skills': ['Python', 'Java', 'C++']}     

