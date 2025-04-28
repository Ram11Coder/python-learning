# class var = shared among all instances of class
#               Define outside the constructor
#               Allow you to share data among all objects created from that class
from car import Car
car1 = Car("BMW", 2024, "Black", False)
print(car1.num_of_cars)
# Class variable directly access from Class
print(Car.num_of_cars)
