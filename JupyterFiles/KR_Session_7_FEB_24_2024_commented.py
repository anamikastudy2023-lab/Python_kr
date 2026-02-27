"""
KR Session 7 - February 24, 2024
Topics Covered:
  1. Nested Dictionary & List Access
  2. Searching & Removing Items in a List
  3. Strings - Basics, Immutability, Escape Characters
  4. String Formatting (format() and f-strings)
  5. Raw Strings
  6. Byte Strings (encode/decode)
  7. String Methods (rstrip, lstrip, replace, split, join, startswith, endswith, case methods)
  8. Functions - Definition, Arguments, Default Arguments, *args, **kwargs
  9. Local vs Global Scope
  10. return Statement
  11. Docstrings
"""

# =============================================================================
# 1. NESTED DICTIONARY & LIST ACCESS (Step-by-step)
# =============================================================================

# 'd1' is a dictionary with a key 'people' whose value is a list.
# Inside that list is another dictionary with key 'india', whose value is
# again a list of dictionaries (each having 'id' and 'name').
# Structure: dict -> list -> dict -> list -> dict
d1 = {'people': [{'india': [{'id': 101, 'name': "Amit"}, {'id': 102, 'name': 'Deepak'}]}]}

# Step-by-step access:
d2 = d1['people']       # d2 is a list: [{'india': [...]}]
type(d2)                 # <class 'list'>
d2                       # prints the list

d3 = d2[0]['india']      # d3 is the list of people dicts: [{'id':101,...}, {'id':102,...}]
type(d3)                 # <class 'list'>
d3[0]                    # {'id': 101, 'name': 'Amit'}

d4 = d3[1]               # d4 is the second person dict: {'id': 102, 'name': 'Deepak'}
type(d4)                 # <class 'dict'>
d4['name']               # 'Deepak' — accesses the 'name' key

# =============================================================================
# 1b. SAME ACCESS IN ONE LINE (chained indexing)
# =============================================================================

# Instead of breaking it into steps, we can chain all the accesses together.
# d1['people'] -> list, [0] -> first dict, ['india'] -> list, [1] -> second person, ['name'] -> value
d1 = {'people': [{'india': [{'id': 101, 'name': "Amit"}, {'id': 102, 'name': 'Deepak'}]}]}
d1['people'][0]['india'][1]['name']  # 'Deepak'


# =============================================================================
# 2. FINDING INDICES OF A VALUE IN A LIST
# =============================================================================

# We have a mixed-type list. Goal: find ALL indices where "Delhi" appears.
x = [101, "Amit", 23, "Delhi", 45678, "Delhi", 798, "Delhi"]
list_size = len(x)                # len() returns the total number of elements (8)

for item in range(list_size):     # 'item' goes 0, 1, 2, ..., 7
    if (x[item] == "Delhi"):      # Check if the element at index 'item' equals "Delhi"
        print(item)               # Output: 3, 5, 7 — the indices where "Delhi" is found


# =============================================================================
# 3. REMOVING ALL OCCURRENCES OF A VALUE FROM A LIST
# =============================================================================

# x.count("Delhi") returns how many times "Delhi" appears (3).
# We loop that many times, each time calling x.remove("Delhi") which removes
# the FIRST occurrence of "Delhi" from the list.
x = [101, "Amit", 23, "Delhi", 45678, "Delhi", 798, "Delhi"]
for item in range(x.count("Delhi")):  # Loop runs 3 times
    x.remove("Delhi")                 # Removes the first "Delhi" found each time

x  # [101, 'Amit', 23, 45678, 798] — all "Delhi" entries are gone


# =============================================================================
# 4. ASSIGNMENTS (Practice Problems - Unsolved)
# =============================================================================

list1 = [23, 12, 45, 64, 85, 8, 19, 10, 88, 123, 22]
# Assignment 1: Create a new list and add all EVEN numbers from list1
# Hint: use (num % 2 == 0) to check if a number is even

list1 = ["amit", "deepak", "root", "ram", "sham", "mike"]
# Assignment 2: Create a new list and CAPITALIZE the first character of every name from list1
# Hint: use .capitalize() or .title() or string slicing + .upper()

gender = ["male", "female", "male", "male", "female"]
# Assignment 3: Create a new list — add 1 for "male" and 0 for "female"


# =============================================================================
# 5. STRING BASICS
# =============================================================================

# Strings in Python:
#   - Are sequences of characters (like lists, but for text)
#   - Are INDEX-BASED (0-indexed), just like lists
#   - Spaces ARE counted as characters
#   - len() returns the total number of characters including spaces

st = "welcome"
len(st)  # 7 — 'w','e','l','c','o','m','e'


# =============================================================================
# 6. STRING IMMUTABILITY
# =============================================================================

st = "welcome to kr"

# Indexing works just like lists:
# st[-1]    → 'r' (last character)
# st[0:3]   → 'wel' (slicing from index 0 to 2)

# BUT strings are IMMUTABLE — you CANNOT change or delete individual characters:
# st[1] = 'y'   → TypeError! Strings don't support item assignment
# del st[1]     → TypeError! Strings don't support item deletion


# =============================================================================
# 7. STRING FORMATTING (format() and f-strings)
# =============================================================================

# Getting user input and computing the sum:
x = int(input("Enter a number :"))  # int() converts the input string to integer
y = int(input("Enter a number :"))

z = x + y  # Calculate the sum

# METHOD 1: .format() — use {} as placeholders, then pass values in order
# st = "sum of {} and {} is {}".format(x, y, z)

# METHOD 2: f-string (preferred) — prefix the string with 'f', put variables inside {}
st = f"sum of {x} and {y} is {z}"
print(st)  # e.g. "sum of 4 and 5 is 9"


# =============================================================================
# 8. ESCAPE CHARACTERS AND RAW STRINGS
# =============================================================================

# Common escape characters in Python:
# \t  → Tab
# \n  → New line
# \r  → Carriage return
# \b  → Backspace
# \f  → Form feed
# \v  → Vertical tab
# \0  → Null character
# \N  → Unicode character
# \\  → Literal backslash
# \a  → Alert (bell)

# PROBLEM: When writing Windows file paths, backslashes get interpreted as escape chars
# e.g. "D:\python\temp\newfiles\abc.txt" → \p, \t, \n, \a get misinterpreted!

# SOLUTION 1: Use double backslashes to escape them:
# path = "D:\\python\\temp\\newfiles\\abc.txt"

# SOLUTION 2: Use a raw string (prefix with 'r') — backslashes are treated literally:
path = r"D:\python\temp\newfiles\abc.txt"
print(path)  # D:\python\temp\newfiles\abc.txt


# =============================================================================
# 9. BYTE STRINGS — b"..." prefix and encode()/decode()
# =============================================================================

# In socket programming (TCP/UDP), data is sent as BYTES, not text.

# WAY 1: Use b"..." prefix when defining a string literal yourself.
# This directly creates a bytes object.
st = b"hello"
type(st)  # <class 'bytes'>

# WAY 2: Use .encode() when the string comes from user input or a file.
# .encode() converts a str → bytes
st = "welcome"
x = st.encode()   # Converts "welcome" to b'welcome'
type(x)            # <class 'bytes'>

# To convert bytes BACK to a string, use .decode()
y = x.decode()     # Converts b'welcome' back to "welcome"
type(y)            # <class 'str'>


# =============================================================================
# 10. STRING METHODS
# =============================================================================

# --- 10a. rstrip() — Remove characters from the RIGHT side ---
x = "34%"
int(x.rstrip('%'))  # Removes '%' from the right → "34" → int → 34

# --- 10b. lstrip() — Remove characters from the LEFT side ---
y = "$4.99"
# float(y.lstrip('4'))   → WON'T work: '4' is not at the leftmost position, '$' is
# float(y.lstrip('$4'))  → Works: strips any of '$' or '4' from the left → "4.99"
float(y.lstrip('$'))     # Strips '$' from the left → "4.99" → float → 4.99

# --- 10c. replace() — Replace substrings ---
z = "12,67,890"
int(z.replace(',', ''))  # Replaces all commas with nothing → "1267890" → int → 1267890

st = "hello hi how are you"
st.replace('h', 'H')        # Replace ALL 'h' with 'H' → "Hello Hi How are you"
# st.replace('h', 'abc')    # Replace 'h' with multiple chars → "abcello abci abcow are you"
# st.replace('how', '')     # Replace 'how' with nothing (delete it) → "hello hi  are you"
st.replace('h', 'H', 2)     # Replace only the FIRST 2 occurrences → "Hello Hi how are you"

# --- 10d. split() — Split a string into a list ---
st = "hello hi how are you"
st.split()         # Splits by whitespace (default) → ['hello', 'hi', 'how', 'are', 'you']

st = "hello,hi,how,are,you"
st.split(',')      # Splits by comma → ['hello', 'hi', 'how', 'are', 'you']

# --- 10e. Practical Example: Filter files by extension using split() ---
data = ["abc.txt", "data.csv", "dir1", "imag.png", "xyz.txt"]

# Print all file names:
for file in data:
    print(file)

# Print only .txt files by splitting on '.' and checking the last part:
for file in data:
    x = file.split('.')      # e.g. "abc.txt" → ['abc', 'txt']
    if x[-1] == "txt":       # Check if the last element (extension) is "txt"
        print(file)          # Output: abc.txt, xyz.txt

# --- 10f. join() — Join a list of strings into one string ---
st = ['hello', 'hi', 'how', 'are', 'you']
# Syntax: "<separator>".join(list)
# x = ",".join(st)    → "hello,hi,how,are,you"
# x = "/".join(st)    → "hello/hi/how/are/you"
x = " ".join(st)       # → "hello hi how are you"

# --- 10g. startswith() and endswith() — Check prefix/suffix ---
st = "welcome to kr"
st.startswith("wel")   # True — string starts with "wel"
st.endswith("kr")      # True — string ends with "kr"

# Practical: Filter .txt files using endswith() — cleaner than split approach
data = ["abc.txt", "data.csv", "dir1", "imag.png", "xyz.txt"]
for file in data:
    if file.endswith(".txt"):   # Directly check if filename ends with ".txt"
        print(file)             # Output: abc.txt, xyz.txt

    # --- 10h. Case Conversion Methods ---
    st = "welcoMe to kr neTwork"
    print(st.lower())       # "welcome to kr network"      — all lowercase
    print(st.upper())       # "WELCOME TO KR NETWORK"      — all uppercase
    print(st.swapcase())    # "WELCOmE TO KR NEtWORK"      — swap each character's case
    print(st.title())       # "Welcome To Kr Network"       — capitalize first letter of each word
    print(st.capitalize())  # "Welcome to kr network"       — capitalize only the first letter of the string


# =============================================================================
# 11. FUNCTIONS — Basics
# =============================================================================

# A function is a reusable block of code.
# Syntax:
#   def function_name(arguments):
#       # code block

# --- 11a. Function with NO arguments ---
def msg():
    print("welcome to kr")

msg()  # Calling the function → prints "welcome to kr"
msg()  # Can be called multiple times


# --- 11b. Function with POSITIONAL arguments ---
def add(x, y):
    z = x + y     # Add the two arguments
    print(z)      # Print the result

add(3, 4)   # Output: 7  — x=3, y=4
add(5, 6)   # Output: 11 — x=5, y=6
add(7, 8)   # Output: 15 — x=7, y=8


# --- 11c. Function with MULTIPLE arguments ---
def info(id, name, city, salary):
    print("id is :", id)
    print("name is :", name)
    print("city is :", city)
    print("salary is :", salary)

# Calling with positional arguments (order matters!):
info(101, "Amit", "Delhi", 5678)


# --- 11d. KEYWORD arguments — pass arguments by name (order doesn't matter) ---
info(name="Amit", id=101, salary=567854, city="Delhi")
# Even though the order is different, each value goes to the correct parameter


# --- 11e. DEFAULT argument values ---
# Parameters with default values MUST come AFTER parameters without defaults.
def info(id, name, city="Delhi", salary=25000):
    print("id is :", id)
    print("name is :", name)
    print("city is :", city)
    print("salary is :", salary)

# If you don't provide city/salary, defaults are used:
# info(101, "Amit")                     → city="Delhi", salary=25000
# info(101, "Amit", "Noida", 56000)     → overrides both defaults
info(101, "Amit", salary=67000)          # city="Delhi" (default), salary=67000 (overridden)


# =============================================================================
# 12. *args — Variable-length POSITIONAL arguments
# =============================================================================

# *x collects all extra positional arguments into a TUPLE.
# This allows the function to accept ANY number of arguments.
def add(*x):
    result = 0
    for i in x:            # Iterate through all received arguments
        result = result + i  # Sum them up
    print(result)

add(4, 5, 4, 5)   # Output: 18 — works with 4 arguments
add(4, 5, 6)       # Output: 15 — works with 3 arguments
add(6, 5, 4)       # Output: 15 — works with 3 arguments

# You can also access *args by index (it's a tuple):
def adduser(*var):
    print(var[0])   # First argument
    print(var[1])   # Second argument

adduser("redhat", "root")  # Output: redhat, root


# =============================================================================
# 13. **kwargs — Variable-length KEYWORD arguments
# =============================================================================

# **var collects all keyword arguments into a DICTIONARY.
# The keys are the argument names, the values are the argument values.
def adduser(**var):
    print(var['username'])   # Access by key name

adduser(password="redhat", gid=501, username="root")
# var = {'password': 'redhat', 'gid': 501, 'username': 'root'}
# Output: root


# =============================================================================
# 14. LOCAL vs GLOBAL SCOPE
# =============================================================================

# local  : A variable defined INSIDE a function — accessible only within that function
# global : A variable defined OUTSIDE any function — accessible everywhere

# EXAMPLE 1: Local variable 'q' is NOT accessible outside m1()
p = 100  # global variable

def m1():
    q = 200  # local variable — only exists inside m1()
    print(p, q)  # Can access both global 'p' and local 'q' → 100 200

def m2():
    print(p)   # Can access global 'p' → 100
    # print(q) # ERROR! 'q' is local to m1(), not accessible here → NameError

m1()  # Output: 100 200
# m2()  # Would cause: NameError: name 'q' is not defined


# EXAMPLE 2: Using 'global' keyword to make a local variable GLOBAL
p = 100  # global

def m1():
    global q       # Declares 'q' as a GLOBAL variable
    q = 200        # Now 'q' is global, accessible everywhere after m1() runs
    print(p, q)    # 100 200

def m2():
    print(p)       # 100
    print(q)       # 200 — now accessible because 'q' was declared global in m1()

m1()  # Must run m1() first to create the global 'q'
m2()  # Output: 100, then 200


# =============================================================================
# 15. return STATEMENT
# =============================================================================

# Instead of printing the result inside the function, we can RETURN it.
# This lets us store the result in a variable and use it later.
def add(*x):
    result = 0
    for i in x:
        result = result + i
    return result    # Sends the result back to the caller

a = add(3, 4, 6)    # a now holds the returned value: 13
a                    # 13


# =============================================================================
# 16. DOCSTRINGS
# =============================================================================

# A docstring is a string placed as the FIRST statement in a function.
# It documents what the function does. Accessible via help(function_name).
def add(x, y):
    '''x and y must need to be int value'''  # This is the docstring
    z = x + y
    print(z)

help(add)
# Output:
# Help on function add in module __main__:
#
# add(x, y)
#     x and y must need to be int value
