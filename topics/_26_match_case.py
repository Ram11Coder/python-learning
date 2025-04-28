
# Match-case statement (switch)= An alternative to using many elif statements
# Execute some code if a value match 'case'
# Benefits : cleaner and syntax is more readable
# case - => wildcard


def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "It's not valid day"


print(day_of_week(1))
print(day_of_week("Pizza"))
print(day_of_week("Pizza"))