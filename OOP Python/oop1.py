#   OOP = Object Oriented Programming

from car import Car

car_1 = Car('Mercedes', 'Benz', 2022, 'blue', 'Rubrivira')
car_2 = Car('Ford', 'Mustang', 2022, 'red', 'Azulporã')
car_3 = Car('Mazda', 'Furai', 2001, 'black', 'galinha')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.drive()
# car_1.stop()

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# car_2.drive()
# car_2.stop()

#   class variables

car_2.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
