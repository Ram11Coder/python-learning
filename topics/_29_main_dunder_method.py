# if __name__ = __main__: (this script can be imported or run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practise (code is modular,
# helps readability, leaves no global variables, avoid unintended execution)
#
# ex : Library = import lib for functionality
# when running lib directly, display a help page
# In Python, every module has a built-in variable called __name__:
# If the file is being run directly, __name__ == "__main__"
# If the file is being imported, __name__ == "module_name"
#  Why is this useful?
# To separate logic: Keeps function definitions separate from runtime behavior.
# To prevent side effects when importing code.
# To support reusability and testing: You can import functions without accidentally running the whole script.

print(__name__)


def main():
    print("inside main : ")


if __name__ == '__main__':
    main()