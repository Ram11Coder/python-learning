# Default argument = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces no of arguments
#                    1. Positional, 2.Default, 3. Keyword, 4. arbitrary

import time
def net_price(price, discount=0, tax=0.05):
    return price * (1 - discount) * (1 + tax)


print(net_price(500, 0.1))
print(net_price(500))


def time_counter(end, start=0):  # default argument preceded with non-default argument
    for i in range(start, end):
        time.sleep(1)
        print(i)


time_counter(2)