class Car:
    # self = self is replaced with object name like
    # car1.model = model
    num_of_cars = 0

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_of_cars += 1

    def drive(self):
        print(f"You drive the {self.model} {self.year}")

    def stop(self):
        print(f"you stopped the {self.model} {self.year}")

    def describe(self):
        print(f"{self.model} {self.year} {self.color}")
