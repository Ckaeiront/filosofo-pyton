#   method chaining = calling multiple methods sequentially
#                     each call performs an action on the same object and returns self
#                     (you need to return self in order to the next function to use the object
#                     with the changes made before)

class Car:
    def turn_on(self):
        print('you start the engine')
        return self

    def drive(self):
        print('you drive the car')
        return self

    def brake(self):
        print('you step on the brakes')
        return self

    def turn_off(self):
        print('you turn off the engines')
        return self
    
car = Car()

# car.turn_on().drive()
# car.brake().turn_off()

#   backslash break a line

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
