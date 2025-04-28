# instance var - defined inside the constructor
from car import Car

car1 = Car("BMW", 2024, "Black", False)
print(car1.num_of_cars)
car2 = Car("Jaguar", 2025, "White", True)
car3 = Car("Audi", 2024, "Yellow", False)

car1.describe()
car1.drive()
car1.stop()