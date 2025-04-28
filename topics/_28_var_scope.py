# variable scope : Where a variable is visible and accessible
# scope resolution : (LEGB) Local -> Enclosed -> Global -> Built-in

# local
def func():
    x = 1
    print(x)

func()

# enclosed
def func1():
    x = 2

    def func2():
        print(x)

    func2()

func1()

# Global - outside of any func()
x = 3

def func3():
    print(x)

func3()

from math import e
print(e)
