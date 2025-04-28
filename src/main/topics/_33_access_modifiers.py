# Python by default not support the private,public and protected attribute
# but we can use naming convention to achieve it

class Animal:
    family = "Animal family"
    _statement = "I love animals"

    def __init__(self, type):
        self.type = type
        self.__name = "Max"


cat = Animal("cat")
print(f"Instannce var = {cat.type}")
print(f"Class var = {Animal.family}")

# protected means we don't want to access this statement outside of this class
print(f"Protected var = {Animal._statement}")


# private access = _[clas_name].__[var_name]
# print(f"private var = {cat._Animal.__name}")
