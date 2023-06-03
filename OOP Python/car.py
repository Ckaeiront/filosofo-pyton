# classes = blueprint for objects

class Car:
    def __init__(self, make, model, year, color, motor): # self is already in the class and we don't need to pass it as argument
        self.make = make 
        self.model = model
        self.year = year
        self.color = color
        self.motor = motor

    def drive(self): # self is the object that is using this method
        print('this ' + self.model + ' is driving')

    def stop(self):
        print('this ' + self.model + ' is stopped')

# self = this in javascript
