# Arbitrary arg = Varying amount of arguments,
# we are not sure about how many arg user gonna pass in while invoking the function
# *args = allow you to pass multiple non-key arguments (tuple)
# **kwargs = allow you to pass multiple keyword-arguments (dict)
# * unpacking operator
# * operator unpacks an iterable (like a list, tuple, or string), spreading out its elements.
#

# Ex of unpacking list

nums = [1, 3, 4, 5, 6]
print(nums)
print(*nums)

a = [1, 2]
b = [3, 4]
merge_list = [a, b]
merge_value = [*a, *b]
print(merge_list)
print(merge_value)


def print_name(*args):
    print(*args, end=" ")


print_name("Mr.", "Rocky", "Bhai")
print()


# The ** operator unpacks a dictionary, spreading out its key-value pairs.
# You're passing a dictionary as named arguments to a function.
#
# You want to merge dictionaries.
#
# You want a flexible function that accepts any keyword arguments.


def print_address(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


print_address(street="Vivekanandha Street", dist="Chennai", state="TN", pin="123456")
