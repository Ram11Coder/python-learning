
# function = A block of reusable code
#            place () after the function name to invoke it


def call_me(name):
    print(f"Hey! call me as {name}")


call_me("Rocky")


# return = statement used to end a function and send a result back to caller


def second_max(li):
    li = list(set(li))
    li.sort(reverse=True)
    return li[1]


arg = [3, 2, 1, 6, 3, 6]
print(second_max(arg))