#   method overwriting
#   just copy the parent's method and it's parameters
#   a class will use a method that is closer to it's source than it's parent

class Animal:
    def eat(self):
        print('this animal is eating')

class Rabbit(Animal):
    def eat(self):
        print('this rabbit is eating a carrot')

rabbit = Rabbit()
rabbit.eat()
