# Membership operator : used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, dict)
#                       1. in
#                       2. not in


fruit = "APPLE"
ch = input("Enter a character : ")
if ch in fruit:
    print(f"{ch} is present in {fruit}")
else:
    print(f"{ch} is not present in {fruit}")

grade_dict = {"Ram": "A", "Raju": "C", "Rocky": "F", "Revi": "B"}

student = input("Enter the student to get grade details : ")

if student in grade_dict:
    print(f"{student} grade is : {grade_dict[student]}")
else:
    print(f"{student} is not present")
    