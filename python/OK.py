import math
import random

 # () -> parentheses      for tuples
 # [] -> square brackets  for list 
 # {} -> curly braces.   for dictionary and set



# Python is a dynamically typed language, meaning you don't need to declare the type of a variable when you create it.
# The type is determined at runtime based on the value assigned to the variable.
# For example:
x = 5  # x is an integer
y = 3.14  # y is a float
z = "Hello"  # z is a string
# You can change the type of a variable by assigning a new value of a different type:
x = "Now I'm a string"  # x is now a string
# Python supports several built-in data types, including:
# 1. Numeric Types:
#    - int: Integer values (e.g., 5, -3)
#    - float: Floating-point values (e.g., 3.14, -0
# 2. String Type:
#    - str: Sequence of characters (e.g., "Hello", 'Python')
# 3. Sequence Types:
#    - list: Ordered, mutable collection of items (e.g., [1,
# 2, 3], ['a', 'b', 'c'])
#    - tuple: Ordered, immutable collection of items (e.g., (1,
# 2, 3), ('a', 'b', 'c'))
# 4. Set Type:
#    - set: Unordered collection of unique items (e.g., {1, 2, 3}, {'a', 'b', 'c'})
# 5. Mapping Type:
#    - dict: Collection of key-value pairs (e.g., {'name': 'Alice', 'age': 30}, {1: 'one', 2: 'two'})
# 6. Boolean Type:
#    - bool: Represents True or False values (e.g., True, False)
# 7. None Type:
#    - NoneType: Represents the absence of a value (e.g., None)
# 8. Complex Type:
#    - complex: Represents complex numbers (e.g., 3 + 4j,where 'j' is the imaginary unit)


# important note:
# In Python, variables are references to objects in memory.
# When you assign a variable to another variable, you are creating a reference to the same object, not a copy of it.
# This means that if you change the object through one variable, the change will be reflected in the other variable as well.
# varname does not have any type of data type but the value it holds has a type
# set ne empty thi denote karvu hoi set ne to set() lakhvu

#lsd -> mutable
# list set dictionary

# print(dir(set)) to get the methods available for a set
# 🔹 List Methods
# append()       # Add item to end
# extend()       # Add elements from another iterable
# insert()       # Insert at specific index
# remove()       # Remove first matching element
# pop()          # Remove and return item at index (default: last)
# clear()        # Remove all elements
# index()        # Return first index of value
# count()        # Count number of times value appears
# sort()         # Sort the list in-place
# reverse()      # Reverse the list in-place
# copy()         # Shallow copy of the list

# 🔹 Set Methods
# python
# Copy
# Edit
# add()              # Add a single element
# update()           # Add multiple elements
# remove()           # Remove element (error if not present)
# discard()          # Remove element (no error if missing)
# pop()              # Remove and return a random element
# clear()            # Remove all elements
# copy()             # Return a shallow copy

# union()            # Return union (or `|`)
# intersection()     # Return intersection (or `&`)
# difference()       # Return difference (or `-`)
# symmetric_difference()  # Return symmetric difference (or `^`)

# issubset()         # Check if set is subset
# issuperset()       # Check if set is superset
# isdisjoint()       # Check if sets have no elements in common
# 🔹 Dictionary Methods
# python
# Copy
# Edit
# get()              # Return value for key (default: None)
# keys()             # Return list-like view of keys
# values()           # Return list-like view of values
# items()            # Return view of (key, value) pairs
# pop()              # Remove and return value by key
# popitem()          # Remove and return last inserted key-value pair
# clear()            # Remove all items
# update()           # Update dict with another dict/iterable
# setdefault()       # Get value if key exists; otherwise, insert and return default
# copy()             # Shallow copy
# fromkeys()         # Create dict with given keys and one default value
# 🔹 Tuple Methods
# python
# Copy
# Edit
# count()      # Count how many times a value occurs
# index()      # Find index of first occurrence of value
# 🔸 Note: Tuples are immutable, so no methods like append(), remove(), or sort().

print("hello")

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

print(add(2,3))
print(add("e","f"))

[] #brackets
() # parentheses
{} # curly braces


l1 = [1, 2, 3, 4, 5]
l2 = l1

l2[0] = 10
print(l1)  # Output: [10, 2, 3, 4, 5]
l3 = l1.copy()
l3[0] = 20
print(l1)  # Output: [10, 2, 3, 4, 5]
print(l2)
print(l3) # Output: [20, 2, 3, 4, 5]

p1= [1, 2, 3]
p2 = p1

p2=[1,2,3] # jyare navo p2 arr 
# banavie tyare navu memory address 
# par assign thay bhale same j value hoy
p2[0] = 10
print(p1)  # Output: [1, 2, 3]
print(p2)  # Output: [10, 2, 3]

#
p1= [1, 2, 3]
p2 = p1
p2=[1,2,3]
print(p1 == p2) # Output: True cause values are the same
print(p1 is p2)  # Output: False // cause they are different objects in memory
# p1 and p2 are different objects in memory
# but have the same values

print(1 == 2< 3) # Output: False, because 1 == 2 is False, and False < 3 is True
print(1 == 2 and 2<3) #it is same as upper
print(1 == 2 or 2 < 3)  # Output: True, because 1 == 2 is False, and False < 3 is True
print(True and False)  # Output: False, because True and False is False

print(math.trunc(2.9)) #gives 2 cause it gives int towards the 0
print(math.trunc(-2.9))

print(math.floor(2.9)) 
print(math.floor(-2.4))
print((2 + 3j)*4)  # Output: (8+12j), complex number multiplication

print(0o10)  # Output: 8, octal representation of 8
print(0x10)  # Output: 16, hexadecimal representation of 16
print(0b1010)  # Output: 10, binary representation of 10
print(0b1010 + 0x10)  # Output: 26, binary and hexadecimal addition
print(oct(40))
print(hex(40))  # Output: '0x28', hexadecimal representation of 40
print(bin(40))  # Output: '0b101000', binary representation of 40

print(int('40',8))
print(int('40',16))  # Output: 64, converts hexadecimal '40' to decimal
print(int('10000',2))  # Output: 32, converts binary '40' to decimal
print(int('0x40', 16))  # Output: 64, converts hexadecimal '0x40' to decimal

x = 1
x <<2 # Output: 4, left shift operator, equivalent to multiplying by 2^2

print(random.random() * 10) 
print(random.randint(0,10)) # Output: random integer between 0 and 10

l1 = ['a', 'b', 'c']
random.shuffle(l1)  # Shuffles the list l1 in place
print(l1)  # Output: shuffled list, e.g., ['c', 'a', 'b']
random.choice(l1)  # Output: random element from the list l1
print(random.sample(l1, 2))  # Output: random sample of 2 elements from the list l1

from decimal import Decimal 
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)  # Output: Decimal('0.3'), precise decimal addition

from fractions import Fraction
m1 = Fraction(1, 3) # creates a fraction 1/3
print(m1)

type({})  # Output: <class 'dict'>, dictionary type
type([])  # Output: <class 'list'>, list type
type(())  # Output: <class 'tuple'>, tuple type
type(set())  # Output: <class 'set'>, set type
type(1)  # Output: <class 'int'>, integer type
type(1.0)  # Output: <class 'float'>, float type

s1 = {1, 2, 3,4}
s2 = {4,6,7,8}
print(s1 & s2) # Output: 4
print(s1 | s2)  # Output: {1, 2, 3, 4, 6, 7, 8}, union of sets
print(s1 - s2)  # Output: {1, 2, 3}
print(s1 ^ s2) # Output: {1, 2, 3, 6, 7, 8}, symmetric difference of sets

s3 = {10,11}
print(s1 & s3)  # Output: set(), intersection of sets s1 and s2
# empty thi denote karvu hoi set ne to set() lakhvu
s4 = set()
print(s4) # Output: set(), empty set
True == 1
False == 0
print(True + True)  # Output: 2, True is treated as 1
print(True +4)

nums = "0123456789"
print(nums[:])
print(nums[::2])  # Output: '02468', every second character
print(nums[::-1])  # Output: '9876543210', reversed string

s1 = "hello"
print(s1.upper())  # Output: 'HELLO', converts to uppercase
print(s1.lower())  # Output: 'hello', converts to lowercase
print(s1.capitalize())  # Output: 'Hello', capitalizes the first letter
print(s1.title())  # Output: 'Hello', capitalizes the first letter of each word
print(s1.replace('l', 'x'))  # Output: 'hexxo', replaces 'l' with 'x'
print(s1.find('l'))  # Output: 2, finds the first occurrence of 'l'
print(s1.index('l'))  # Output: 2, finds the first occurrence of 'l'
print(s1.count('l'))  # Output: 2, counts occurrences of 'l'
print(s1.startswith('he'))  # Output: True, checks if string starts with 'he'
print(s1.endswith('lo'))  # Output: True, checks if string ends with 'lo'
print(s1.split('l'))  # Output: ['he', '', 'o'], splits the string by 'l'
print(s1) # Output: 'hello', original string remains unchanged cause strings are immutable

s2 = "      hello world "
print(s2.strip())  # Output: 'hello world', removes leading and trailing whitespace
print(s2.lstrip())  # Output: 'hello world ', removes leading whitespace
print(s2.strip().replace("hello","namsate")) # Output: 'namsate world ', replaces 'hello' with 'namsate' 

st = "heelo, golden, fish"
print(st.split(', '))  # Output: ['heelo', ' golden', ' fish'], splits the string by ','
print(st[:])  # Output: 'heelo, golden, fish', original string remains unchanged
print(st.find('just'))  # Output: -1, 'just' not found in the string

order = 'i ordered {} cup of {}' # {} is a placeholder for formatting
quantity = 2
type = 'tea'
print(order.format(quantity, type))  # Output: 'i ordered 2 cup of tea', formats the string with values

#list to string
l1 = ['pizza', 'burger', 'pasta']
str = "".join(l1)  # Joins the list elements into a string
print(str)  # Output: 'pizzaburgerpasta'
#list to string with separator
str_with_sep = ", ".join(l1)  # Joins the list elements into a string with a separator
print(str_with_sep)  # Output: 'pizza, burger, pasta', joins with a comma and space

strr= 'i wasn\'t'
print(strr)  # Output: 'i wasn't', prints the string with an escaped single quote

# # 3 times 'un', followed by 'ium'
# 3 * 'un' + 'ium'
# 'unununium'
# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

# Copy
# 'Py' 'thon'
# 'Python'

# This only works with two literals though, not with variables or expressions:

# Copy
# prefix = 'Py'
# prefix 'thon'  # can't concatenate a variable and a string literal
#   File "<stdin>", line 1
#     prefix 'thon'
#            ^^^^^^
# SyntaxError: invalid syntax
# ('un' * 3) 'ium'
#   File "<stdin>", line 1
#     ('un' * 3) 'ium'
#                ^^^^^
# SyntaxError: invalid syntax

st = 'hello world'
# st[0] = "p" # This will raise an error because strings are immutable
# TypeError: 'str' object does not support item assignment

# \ is a unicode character so we have to escape the backslash in file paths in Python.
# To avoid escaping backslashes, you can use a raw string by prefixing the string with 'r'
path = 'C:\\Users\\user\\Documents\\file.txt'  # Use double backslashes or raw string
# Alternatively, you can use a raw string to avoid escaping backslashes
path = r'C:\Users\user\Documents\file.txt'  # Raw string, no need to escape backslashes
print(path)  # Output: C:\Users\user\Documents\file.txt

chai = "masala chai"
print("masala" in chai)  # Output: True, checks if 'masala' is in 'chai'
print("coffee" not in chai)  # Output: True, checks if 'coffee' is not in 'chai'


# String formatting using f-strings (Python 3.6+)
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is John and I am 30 years old.
# String formatting using format method
print("My name is {} and I am {} years old.".format(name.upper(), age))  # Output: My name is John and I am 30 years old.

# """ """ is uses in loops

st = 'meet \\n oj' # This will print the string with a newline character 
# if we used only \n it would be treated as a newline character
print(st)

name = ['meet','dj','dharm','hardik']
print(name)
name[1:2] = "nilay" # Output: ['meet', 'n', 'i', 'l', 'a', 'y', 'dharm', 'hardik']

name[0:1] = ["nilay"]
print(name)   
# This will replace the elements at index 1 with the characters of "nilay"

name[2:4] = ["jay","pankaj"]
print(name)   

print(name[1:1])
name[1:1] = ["jaun",'minal']
print(name)
name[8:10] = []
print(name)


names = ['meet','dj','dharm','hardik']
names.sort()
print(names)  # Output: ['dharm', 'dj', 'hardik', 'meet'], sorts the list in ascending order
names.sort(reverse=True)  # Sorts the list in descending order
print(names)  # Output: ['meet', 'hardik', 'dj', 'dharm'], sorts the list in descending order
for n in names:
    print(n,end='-')
    
print()

if('meet' in names):
    print("meet is in the list")
else:
    print("meet is not in the list")

names.pop()  # Removes and returns the last element of the list
names.append('vijay')  # Adds 'nilay' to the end of the list
names.remove('dj')  # Removes the first occurrence of 'dj' from the list
names.insert(2,'nilay')  # Inserts 'nilay' at index 1
print(names)  

namescopy = names.copy()  # Creates a shallow copy of the list 
                          # it is uses when we want to create new list with same values
                          #but with different memory address
                          
namescopy.append('pankaj')  # Adds 'pankaj' to the end of the copied list
print(namescopy)  # Output: ['dharm', 'nilay', 'nilay
print(names)

y = range(10)  # Creates a range object from 0 to 9
print(y)  # Output: range(0, 10)

squared_num = [x**2 for x in range(11)] # it is a list comprehension that creates a list of squares of numbers from 0 to 10
print(squared_num)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100], squares of numbers from 0 to 10

chai_types = {"masala" : "spicy", "ginger": "strong", "lemon": "refreshing"}
print(chai_types["masala"])  # Output: spicy, retrieves the value for the key "masala"

chai_types["cardamom"] = "aromatic"  # Adds a new key-value pair to the dictionary
print(chai_types.get("cardamom"))  # Output: aromatic, retrieves the value for the key "cardamom"
chai_types["masala"] = "hot and spicy"  # Updates the value for the key "masala"
print(chai_types)  # Output: {'masala': 'hot and spicy', '

del chai_types["ginger"]  # Deletes the key "ginger" from the dictionary

for chai in chai_types:
    print(chai, chai_types[chai])  # Prints each key and its corresponding value

for key,value in chai_types.items():
    print(key, value)  # Prints each key and its corresponding value
    
if "masala" in chai_types:
    print("masala is in the dictionary")
else:
    print("masala is not in the dictionary")
    
print(len(chai_types))

#pop ma shu remove karvu che te kevu pade
print(chai_types.pop("masala"))  # Removes and returns the value for the key "masala"
chai_types.popitem()  # Removes and returns the last inserted key-value pair
print(chai_types)  # Output: {'cardamom': 'aromatic'}, after removing "masala" and the last inserted item

print("     ")
tea_shop = {
    "chai" : {"masala": 10, "ginger": 15, "lemon": 12},
    "coffee" : {"latte": 20,"cuppuccino":25, "black": 18}
}
print(tea_shop["chai"]["masala"])
print(tea_shop["chai"].get("masala"))  # Output: 10, retrieves the price of "masala" chai

squared_num_withnum = {x:x**2 for x in range(11)}  # List comprehension to create a list of squares of numbers from 0 to 10
print(squared_num_withnum)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
squared_num_withnum.clear()  # Clears the dictionary, removes all key-value pairs
print(squared_num_withnum)  # Output: {}, empty dictionary

keys = ["masala", "ginger", "lemon"]
default_key = "unknown"


dictionary = dict.fromkeys(keys, default_key)  # Creates a dictionary with keys from the list and a default value
print(dictionary)  # Output: {'masala': 'unknown', 'ginger':  'unknown', 'lemon': 'unknown'}

dict1 = dict.fromkeys(keys,keys)  # Creates a dictionary with keys from the list and the list itself as the value
print(dict1)  # Output: {'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'], 'lemon': ['masala', 'ginger', 'lemon']}  


tea_types = ("masala", "ginger", "lemon","ginger")  # Tuple of tea types
# tea_types[0] = "cardamom"  # This will raise an error because tuples are immutable
print(tea_types[0])

new_types = ("cardamom", "mint", "honey")  # New tuple of tea types
all_types = new_types + tea_types  # Concatenates the new tuple to the existing tuple
print(all_types)  # Output: ('masala', 'ginger', 'lemon', 'cardamom', 'mint', 'honey') // applies order 

if "masala" in all_types:
    print("masala is in the tuple")
    
new_types.count("golanfi")  # Output: 0, counts occurrences of "golafi" in the tuple
new_types.index("mint")  # Output: 1, finds the index of "mint" in the tuple
print(tea_types.count("ginger")) 

(MASALA, GINGER, LEMON,GINGER) = tea_types  # it is used for tyUnpacking the tuple into variables
print(MASALA)  # Output: masala

tuple = ("meet",(1,2,3,4),"jay")

print(tuple[1][3])  #nesting tuples are allowed


# #q1# This program checks if a person is eligible to vote based on their age
# age = int(input("Enter your age: "))  # Takes input from the user and converts it to an integer

# def age_check(age):
#     if age < 18 :
#         print("You are not eligible to vote")
#     elif age >= 18 and age < 60:
#         print("You are eligible to vote")
#     else:
#         print("You are eligible to vote and you are a senior citizen")
        
# age_check(age)


# #q2 # This program calculates the ticket price based on the day of the week and the person's age
# age = int(input("Enter your age: "))  # Takes input from the user and converts it to an integer
# s = "wednesday"

# def age_ticket(age):
#     price = 12 if age >= 18 else 8  # Ternary operator to set price based on age
#     if s == "wednesday":
#         price -= 2
#         return price
        
# price = age_ticket(age)
# print(f"Your ticket price is $",price)  # Prints the ticket price
        
#q3 
fruit = "banana"
color = "yellow"
if fruit!= "banana":
    print("This is not a banana")
    exit()

if fruit == "banana" and color == "yellow":
    print("The banana is ripe")
elif fruit == "banana" and color == "brown":
    print("The banana is overripe")
else: 
    print("The banana is not ripe")
    
    
#q4
order_size = "medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee without an extra shot"
    
print(f"Your order is: {coffee}")  # Prints the coffee order based on size and extra shot

#q5
passis = "nubuuebfiuheoifw"
length =len(passis)
if(length == 0):
    print("Password is empty")
    exit()

if length < 4:
    print("Password is weak")
elif length < 10:
    print("Password is medium")
else:
    print("Password is strong")
    

#q6
# This program checks if a year is a leap year or not
leap_year = 2024
if (leap_year % 400 == 0) or (leap_year % 100 != 0 and leap_year % 4 == 0):
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")
    
    
    
pos_count = 0
nums = [1,-2,43,-2,3,-3,-6,2,-9,4,5,6,7,8,9]
for num in nums:
    if num >0:
       pos_count +=1
#for loop scope ends here       
print("the count of pos number is", pos_count)  # Output: the count of pos number is 10



# nums = [1,-2,43,-2,3,-3,-6,2,-9,4,5,6,7,8,9]
# for num in nums:
#     if num >0:
#         print(num, end=' ')
 #        / if loop scope ends here
 #    / for loop scope ends here



n =10
sum =0

for i in range(1,n+1):
    if i%2 == 0:
        sum +=i
print("The sum of positive even numbers is", sum)  # Output: The sum of positive even numbers is 20        

multiple = 10
table_of =3

for i in range(1, multiple + 1):
    if i == 5: 
        continue
    # print(f"{table_of} x {i} = {table_of * i}")  # Prints the multiplication table of 10 from 1 to 10
    print(table_of,'x',i,'=',table_of * i) # both are same
    
    
print(" ")

s= "meet"
rev_str = ""

for i in s:
    rev_str = i + rev_str  # Reverses the string by adding each character to the front
print(rev_str)  # Output: teem, reversed string    

rev_str = rev_str[::-1]  # Reverses the string using slicing
print(rev_str)  # Output: teem, reversed string using slicing



input_str = "meemt"
for i in input_str:
    if input_str.count(i) == 1:
        print(f"{i} is non-repeating first character")  # Prints the first non-repeating character
        break
    
    
    
n = 5
mul =1
while n>0 :
    mul *= n  # Calculates the factorial of n
    n -= 1
print(f"the fact is {mul}")  # Output: the fact of 5 is 120



# while True:
#     number = int(input("enter a num b/w 1 to 10: "))
#     if 1 <= number <= 10:
#         print("You entered a valid number:", number)
#         break
#     else:
#         print("Invalid number, please try again.")
       
       
       
        
n = 29
# if n% 1 == 0 and n % n == 0:
#     print(f"{n} is a prime number")  # Output: 10 is a prime number
# else:
#     print(f"{n} is not a prime number")
is_prime = True
if n>1:
    for i in range(2,n): # n+1 means number itself is not included in the range cause num is divisible by itself
        if n % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
if(is_prime): 
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
    
    
    
items = ["apple","banana","lichi","apple"]
unique_items = set() # set takesn only unique elements

for item in items:
    if item in unique_items: # jo unique ele hashe to j loop ni inside aavshe
        print("Duplicate item is:",item)
        break
    unique_items.add(item)
    
import time

tries = 0
max_tries=5
wait_time =1

while tries < max_tries:
    print("attempt",tries+1,"-wait time:",  wait_time)
    time.sleep(wait_time)
    wait_time *=2
    tries +=1

