# exception = An event that interrupt the flow of a program
# (ZeroDivisionError,TypeError,ValueError)
# 1. try, 2. expect, 3. finally

try:
    num = int(input("Enter the number : "))
    print(1 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("input should be numeric value")
except Exception:
    print("Something went wrong!")
finally:
    print("Clean up activity ")
