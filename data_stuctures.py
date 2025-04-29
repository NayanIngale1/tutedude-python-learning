# data_structures.py

# -----------------------------
# 1. LISTS
# -----------------------------
# Lists are mutable, ordered collections.
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output: ['apple', 'banana', 'cherry']

fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.insert(1, 'mango')
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']

fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'mango', 'orange']

fruits.reverse()
print(fruits)  # Output: ['orange', 'mango', 'cherry', 'apple']

# -----------------------------
# 2. TUPLES
# -----------------------------
# Tuples are immutable, ordered collections.
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

print(coordinates[0])  # Output: 10
print(len(coordinates))  # Output: 2

# -----------------------------
# 3. SETS
# -----------------------------
# Sets are unordered collections with no duplicate elements.
colors = {'red', 'green', 'blue'}
print(colors)  # Output: {'red', 'green', 'blue'} (order may vary)

colors.add('yellow')
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'} (order may vary)

colors.discard('green')
print(colors)  # Output: {'red', 'blue', 'yellow'} (order may vary)

# Set operations
colors2 = {'black', 'blue', 'red'}
print(colors & colors2)  # Output: {'blue', 'red'} (intersection)
print(colors | colors2)  # Output: {'black', 'blue', 'red', 'yellow'} (union)

# -----------------------------
# 4. DICTIONARIES
# -----------------------------
# Dictionaries store data in key-value pairs.
student = {'name': 'Alice', 'age': 21, 'grade': 'A'}
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

print(student['name'])  # Output: Alice

student['age'] = 22
print(student)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'A'}

student['city'] = 'New York'
# Output: {'name': 'Alice', 'age': 22, 'grade': 'A', 'city': 'New York'}
print(student)

print(student.keys())  # Output: dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # Output: dict_values(['Alice', 22, 'A', 'New York'])
# Output: dict_items([('name', 'Alice'), ('age', 22), ('grade', 'A'), ('city', 'New York')])
print(student.items())

# -----------------------------
# 5. STRINGS
# -----------------------------
# Strings are immutable sequences of characters.
text = "Hello, Python!"
print(text.upper())  # Output: HELLO, PYTHON!

print(text.lower())  # Output: hello, python!

print(text.replace("Python", "World"))  # Output: Hello, World!

print(text.split(","))  # Output: ['Hello', ' Python!']

print(text.find("Python"))  # Output: 7

print(len(text))  # Output: 14

print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))  # Output: True
print(text.strip("!"))  # Output: Hello, Python

# -----------------------------
# End of data_structures.py
