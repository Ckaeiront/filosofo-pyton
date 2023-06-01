#   Functions = block of code which is excecuted only when it's called

# def hello(first_name, last_name, age):
#     print('hello, ' + first_name, last_name + ' and age of ' + str(age))
#     print('have a nice day!')

# hello('Brother', 'codigos', 21)

#   Return statement = functions sends python values/objects back to the caller

def multiply(num1, num2):
    result = num1 * num2
    return result


# x = multiply(6, 8)

# print(x)

#   Keyword arguments = arguments preceded by an identifier when we pass them to a function
#                       the order of the arguments doesn't matter like positional
#                       python knows the name of the arguments that our function recieves

def greet(first, middle, last):
    print("hello " + first, middle, last)

# greet(last='Bro', first='Codigos', middle='Teixeira')

#   nested function calls = function calls inside of other functions
#                           innermost function calls are resolved first
#                           returned value is used as argumetn

# num = input('enter a whole positive number: ')
# num = float(num)
# num = abs(num) # convert a negative to positive number
# num = round(num)

# num = round(abs(float(input('Enter a whole positive number: '))))

#   variable scope = the region that a variable is recognized
#                    a variable is only available from inside the region it is created
#                    a global and locally scoped versions of a variable can be created

# name = 'Brother'

# def display_name():
    # name = 'code'
    # print(name)

# print(name)
# display_name()

#   *args = parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 2
    for i in args:
        sum += i
    return sum

# somados = add(1, 4, 7, 8, 39, 40)
# print(somados)

#   **kwargs = parameter that will pack all arguments into a dictionary
#              useful so that a function can accept a varying amount of keyword arguments

# def hi(**namespace):
#     # print('hello, ' + kwargs['first'] + ' ' + kwargs['last'])
#     print('hello', end=' ')
#     for key,value in namespace.items():
#         print(value, end=' ')

# hi(title='Mr.', first='Brother', last='Codigos')


#   str.format() = optional method that gives users
#                  more control when displaying output
#

# animal = 'cow'
# item = 'moon'

# print("the {} jumped over the {}".format(animal, item))
# print("the {1} jumped over the {0}".format(animal, item)) # positional argument
# print("the {animal} jumped over the {item}".format(animal = 'cow', item = 'moon')) # keyword argument
# print("the {item} jumped over the {animal}".format(animal = 'cow', item = 'moon')) # keyword argument

# text = "the {} jumped over the {}"

# print(text.format(animal, item))

# name = 'brother'

# print('hello, my name is {}'.format(name))
# print('hello, my name is {:20}, nice.'.format(name))
# print('padding to {:>20} codigos rapazes'.format(name))
# print('padding to {:<20} codigos rapazes'.format(name))
# print('padding to {:^20} codigos rapazes'.format(name))

# format numbers

# number = 100000

# print('the number of pi is {:.3f}'.format(number))
# print('the number of pi is {:,}'.format(number))
# print('the number of pi is {:b}'.format(number))
# print('the number of pi is {:o}'.format(number))
# print('the number of pi is {:x}'.format(number))
# print('number is {:E}'.format(number))



#   random

import random

# x = random.randint(1, 7)
# y = round(random.random() * 10)

# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)

# print(z)

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']

# random.shuffle(cards)

# print(cards)



# exceptions = events detected duting execution that interrupt the flow of a program

# 👇 code prone to have an error, like dividing by zero, so we wrap into a try except block, like try catch in javascript

# try:
#     numerator = int(input('enter a number to divide: '))
#     denominator = int(input('enter a number to divide by: '))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print('cannot divide a number by zero')
# except ValueError as error:
#     print(error)
#     print('enter only numbers, please')
# except Exception as intankavel:
#     print(intankavel)
#     print('something went wrong with your inputs')
# else:
#     print(result)
#     print('vai tomar no cu, fdp')

#  👆 only works if no error is encoutered
# finally:
#     print('files of any bitches')

#  👆 always execute, no matter what 

#   file detection = finnaly we're going to use os module to play with files in our computer
#

import os

# path = 'C:\\Users\\soule\\Documents\\filosofo pyton\\proTrial.txt'

# if os.path.exists(path):
#     print('that location exists')
#     if os.path.isfile(path):
#         print('that\'s a file')
#     elif os.path.isdir(path):
#         print('that\'s a directory')
# else:
#     print('cannot locate this location')

#   reading files in pitón

# try:
#     with open('proTrial.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('the file was not found')

#   writing files in paitón, so sit back, relax and enjoy the show

# texto = "fala galeraaa blz aqui quem fala dnv e o andromeda jogos"
# text2 = '\nain q epistemologia'

# with open('falagalera.txt', 'w') as file: # w = write
#     file.write(texto)

# with open('falagalera.txt', 'a') as file: # a = append
#     file.write(text2)

# with open('falagalera.txt') as file:
#     print(file.read())




#   copying files in paiton
#   copyfile() copies content of a file
#   copy() copyfile + permission mode + destination can be a directory
#   copy2() copy + copies metadata (file creation and modification times)

import shutil
                # Source          # destination
# shutil.copyfile('falagalera.txt', 'taro.txt') 
shutil.copy('falagalera.txt', 'C:\\Users\\soule\\OneDrive\\Área de Trabalho\\vinicius.txt') 
# same with copy2



#   moving files in pay thón

# source = 'src'
# destination = 'C:\\Users\\soule\\OneDrive\\Área de Trabalho\\src'

# try:
#     if os.path.exists(destination):
#         print('there\'s already a file there')
#     else:
#         os.replace(source, destination)
#         print(source + ' was moved')
# except FileNotFoundError:
#     print(destination + ' not found')




#   delete files with py ton

# path = 'pesetas'

# try:
#     # os.remove(path)
#     # os.remove() # no permission to delete empty folders
#     os.rmdir(path)
#     # shutil.rmtree(path) # delete an directory and all files in it, so, be careful!!
# except FileNotFoundError:
#     print(path + ' not found')
# except PermissionError:
#     print('you do not have permission to delete that')
# except OSError:
#     print('you cannot delete it using that function.')
# else:
#     print(path + ' was deleted')

#   OBS: EXCEPTION ERRORS APPEAR ON THE CONSOLE
# os.remove('deletar.txt')



#   MODULES IN PYTHOOOOON

#   modules = a file containing python code. May contain functions, classes, etc.
#   used with modular programming, which is to separate program into parts

# import module1 as msg
from module1 import hello, bye


hello()
bye()

help("modules")

# ==================== end of section 2 ====================
