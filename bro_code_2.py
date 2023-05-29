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

def hi(**namespace):
    # print('hello, ' + kwargs['first'] + ' ' + kwargs['last'])
    print('hello', end=' ')
    for key,value in namespace.items():
        print(value, end=' ')

hi(title='Mr.', first='Brother', last='Codigos')


#   str.format() = optional method that gives users
#                  more control when displaying output
#