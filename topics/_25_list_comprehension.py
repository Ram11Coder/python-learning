# list comprehension = A concise way to create lists in python
#                     compact and easier to read than traditional loops
# syntax: [expression for value in iterable if condition]

triples = [x * 3 for x in range(0, 11)]
print(triples)

numbers = [1, -2, 3, -4, 5, -6]
print([num for num in numbers if num > 0])
