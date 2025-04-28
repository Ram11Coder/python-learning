# Inheritance = Allow a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               ex: class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} : WOOF!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} : MEOW!")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} : SQUEEK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Cherry")
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()
cat.speak()
mouse.speak()
