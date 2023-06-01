# The Bro Code Python course from youtube

import time

"""
    Variables
"""

# first_name = "bro"
# last_name = "attack on titan"
# print("hello, " + first_name)

# how to get data type
# type()
# print(type(first_name))

# int data type
# height = 250.3 # float
# age = 19 # integer || int

# print(age)
# print(type(age))
# print("your age is " + str(age))

# print("your age is " + str(height) + 'cm')

# human = False

# print(human)
# print("are you a human? : " + str(human))

# print(type(human)) || type: "bool" short for boolean value

"""
    Multiple Assignments
"""

# name = 'bro'
# age = 21
# attractive = True

# name, age, attractive = 'bro', 21, True;

# spongebob, patrick, sandy, squidward = 30
# print(spongebob, patrick, sandy, squidward)

# ================================================================

"""
    String Methods
"""

# print(name.find("t"))
# name = "Brothercodigos"

# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace('codigo', 'intankavel'))
# print(name*3)

# ================================================================

"""
    Type Casting
"""

""" 

x = 1
y = 2.0
z = '3'

x = float(x)
y = int(y)
z = int(z)

"""

# print(x)
# print(y)
# print(z*10)

# inp_name = input("what is your name? \n");
# age = int(input("how old are you? \n"))

# print(inp_name + ', and age is ' + str(age))

# ================================================================

"""
    Numbers in python
"""

import math

pi = 3.14
x, y, z = 1, 2, 3

# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 3))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))

# ================================================================

"""
    String Slicing
    indexing[start:end:step]
    slice()
"""

"""

name = "Vinicius Jose de Morais Rodrigues"

first_name = name[:5]
last_name = name[6:]
funky_name = name[::2]
reverse_name = name[::-1]

print(first_name, last_name, sep=' - ')
print(funky_name)
print(reverse_name)

"""

"""

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website[slice])
print(website2[slice])

"""

# ================================================================

"""
    if statements
"""

# idade = int(input('how old are your? \n'))

# if idade >= 18:
#     print("you are an adult");
# elif idade == 100:
#     print("you are a century old") 
# elif idade < 0:
#     print("you haven't been born yet")
# else: 
#     print("you are a child")

# ================================================================

"""
    Logical Operators
"""

# and, or & not

# temp = int(input("What's the temperature outside? "))

# if temp >= 0 and temp <= 30: 
#     print("temperature is good today!")
#     print("go outside!")
# elif temp < 0 or temp > 30: 
#     print("temperature is bad today!")
#     print("stay inside!")

# ================================================================

"""
    Loops
"""

# while loop: as long as it remain true, it will continue to run;

# name = None

# while not name:
#     name = input("what is your name? \n")

# print("hello,", name)

#
# for loop: limited iterations
#

# for i in range(10): 
#     print(i + 1)

#            Start  end (exclusive) third argument = step

#for i in range(50, 100 + 1):
#    print(i)

# for i in "Andre Simas":
#    print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1) # sleep is = waiting for an given amount of seconds that you pass as argument

# print('Happy new year!!!')

# ================================================================

#
#   Nested Loops
#
"""

rows = int(input('how many rows?'))
columns = int(input('how many columns?'))
symbol = input('enter a symbol to use')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print('\n')

"""

# Loop control statements change loop excecution

# break, continue, pass = 1 - used to terminate the loop; 2 - skip to the next iteration; 3 - act as a placeholder. does nothing;

# while True:
#     name = input('enter your name here:\n')
#     if name != '': break

# phone_number = '123-456-8790'

# for i in phone_number: 
#     if i == '-': continue
#     print(i, end='')

# for i in range(1, 21):
#     if i == 13: pass
#     else: print(i)

# for i in phone_number:
#     if i == '-': pass
#     print(i)

# ================================================================

"""
    Lists
"""

# list: used to store multiple items in a single variable; A.K.A. Array in JavaScript

# food = ["pizza", "cheese", "frango a parmegiana", "hot dog", "figado"]

# food[1] = 'intankavel' = replacement of lists

# for i in food:
#     print(i)

# methods for lists/arrays

# food.append('chocolate')
# food.remove('chocolate') # remove the passed element
# food.pop() # remove last element
# food.insert(0, 'pudding') # insert at a certain position
# food.sort() # sort alphabetically
# food.clear() # remove all elements of the list

# print(food)

# ================================================================

#
#   2D lists = A list of lists
#

# drinks = ["coffee", "water", "soda"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[2][0])

# ================================================================

"""
    get github user's profile picture - Small project just for fun

import requests

git_user = input('type your github username here: ')

url = 'https://api.github.com/users/' + git_user
github_data = requests.get(url)

if github_data.json()['message'] == 'Not Found':
    print('Error! User not found... 😔')
else:
    gitjson = github_data.json()
    avatar_url = gitjson['avatar_url']
    print("o link para url do pfp -> ", avatar_url)
 
"""

# ===================================================

#
#   tuples = ordered and unchangeable collection
#   used to group together related data

# student = ("bro", 21, "male")

# # print(student.count(21))
# print(student.index("male"))

# for x in student:
#     print(x)
 
# if "bro" in student:
#     print('bro is here, my friend')

# ===================================================

#
#  Set = a collection which is unordered, unindexed. No duplicate values
#

# utensils = {"fork", "spoon", "knife"}
# dishes = {'bowl', 'plate', 'cup', 'knife'}

# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
# utensils.update(dishes)
# dinner_table = dishes.union(utensils)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)

# ================================================================

#
#   Dictionaries = A changeable, unordered collection of unique key:value pairs
#                  Fast because they use hashing, allow us to access a value quickly

# capitals = {"USA": "Washington DC",
#             "India": "New Dehli",
#             "China": "Beijing",
#             "Russia": "Moscow"}

# print(capitals["Russia"])

# capitals.update({"Germany": "Berlin"}) # Add a new "object" to the dictionary
# capitals.pop('China')
# capitals.clear()

# print(capitals.get('germany'))
# print(capitals.keys()) # Will print the keys, a.k.a. countries
# print(capitals.values()) # Will print their values, a.k.a. capitals
# print(capitals.items()) # Will print keys and values

# for key,value in capitals.items():
#     print(key + ': ' + value)

# ================================================================

#
#   Indexing = [] -> gives access to a sequence's element (strings, list, tuples)
#

# name = "brother Codigagens da Silva"

# # if (name[0].islower()):
# #     name = name.capitalize()
# #     print(name)

# first_name = name[0:7].upper()
# last_name = name[8:].lower()
# last_character = name[-1]

# print(first_name)
# print(last_name)
# print(last_character)

############################################### End of Section 1 ################################################