# Duck typing = Another way to achieve polymorphism besides inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck"

class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swimming like a duck 🦆")


class Person:
    def quack(self):
        print("I'm imitating a duck!")

    def swim(self):
        print("I'm swimming... cautiously.")


def in_pond(thing):
    # We only care if 'thing' can quack() and swim(), not its type
    thing.quack()
    thing.swim()


donald = Duck()
alice = Person()

in_pond(donald)  # Quack! / Swimming like a duck 🦆
in_pond(alice)  # I'm imitating a duck! / I'm swimming... cautiously.
