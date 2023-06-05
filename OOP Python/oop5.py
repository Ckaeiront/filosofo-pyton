#   method overwriting

class Animal:
    def eat(self):
        print('this animal is eating')

class Rabbit(Animal):
    pass