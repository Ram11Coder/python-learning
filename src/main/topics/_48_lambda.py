# Lambda
name = "Rocky Bhai"
f1 = lambda func: func.upper()
print(f1(name))

n = lambda x: "positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-5))
print(n(0))

# filter
li = [1, 2, 3, 4, 6, 7, 8, 10]
even = filter(lambda x: x % 2 == 0, li)
print(tuple(even))

square = map(lambda x: x ** 2, li)
print(list(square))
import functools
sum = functools.reduce(lambda x, y: x + y, li)
print(sum)