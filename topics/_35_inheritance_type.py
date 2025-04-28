# Multiple inheritance = Inherit from more than one parent class
# 						Ex: C(A,B)
# Multilevel Inheritance = Inherit from the parent which inherit from another parent
# 						Ex: C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

    def alive(self):
        print(f"Prey {self.name} is alive")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

    def alive(self):
        print(f"Predator {self.name} is alive")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Predator, Prey):
    pass


rabbit = Rabbit("Tony")
rabbit.flee()
rabbit.eat()
rabbit.sleep()

hawk = Hawk("Hawky")
hawk.eat()
hawk.sleep()
hawk.hunt()

fish = Fish("Nemo")
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()
fish.alive()

