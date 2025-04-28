# Keyword argument - an argument preceded by an identifier, helps with readability
# order of argument doesn't matter

def greeting(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


greeting("Hello", first="Rocky", title="Mr.", last="Bhai")

# inbuilt func have keyword arg
print("1", "2", "3", sep="-")