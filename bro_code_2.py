#   Functions = block of code which is excecuted only when it's called

def hello(first_name, last_name, age):
    print('hello, ' + first_name, last_name + ' and age of ' + str(age))
    print('have a nice day!')

# hello('Brother', 'codigos', 21)

#   Return statement = functions sends python values/objects back to the caller

def multiply(num1, num2):
    result = num1 * num2
    return result


x = multiply(6, 8)

print(x)

#   Keyword arguments = arguments preceded by an identifier when we pass them to a function
#                       the order of the arguments doesn't matter like positional
#                       python knows the name of the arguments that our function recieves

def greet(first, middle, last):
    print("hello " + first, middle, last)

greet(last='Bro', first='Codigos', middle='Teixeira')

#   nested function calls = function calls inside of other functions
#                           innermost function calls are resolved first
#                           returned value is used as argumetn

# num = input('enter a whole positive number: ')
# num = float(num)
# num = abs(num) # convert a negative to positive number
# num = round(num)

num = round(abs(float(input('Enter a whole positive number: '))))
