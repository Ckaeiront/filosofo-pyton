# multi-level inheritance = when a derived (child) class inherits another derived class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print('this animal is eating')

class Dog(Animal):
    def bark(self):
        print('this dog is barking')

rex = Dog()

# print(rex.alive)
# rex.eat()
# rex.bark()
