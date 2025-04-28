# python file detection

import os

# Relative file path :exercise\test.txt
#  Absolute file path : C:\Users\intel\PycharmProjects\python-learning\src\main\exercise\test.txt
file_path = "exercise\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' is exist!")
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a folder")
else:
    print("The location does not exist")

# File writing (.txt, .json, .csv)

txt_data = "I like pizza!"
file_path = "output.txt"

# using with -> it automatically file also
# open parameter return the file object
with open(file=file_path, mode='w') as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")

# mode (x) - create a file if not exists, if it already exists then throws FileExistsError exception
# mode (r) - read the file
# mode (a) - append the file
# mode (w) - It will override the file

import json

employee = {
    "name": "Rocky",
    "age": 27,
    "Job": "Developer"
}
json_file_path = "emp.json"
try:
    with open(file=json_file_path, mode='x') as file:
        json.dump(employee, file, indent=4)
        print(f"json file {json_file_path} was created")
except FileExistsError:
    print("The file already exist")

import csv

employee_list = [["Name", "Age", "Job"],
                 ["Ram", 27, "Senior developer"],
                 ["Vicky", 28, "Senior UI developer"],
                 ["Siva", 30, "Tester"], ]
csv_file_path = "emp.csv"
try:
    with open(file=csv_file_path, mode='w', newline="") as file:
        writer = csv.writer(file)
        for row in employee_list:
            writer.writerow(row)
        print(f"csv file {csv_file_path} was created")
except FileExistsError:
    print("The file already exist")

# file reading

# text file read
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')

# Json file read
try:
    with open(json_file_path, 'r') as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')

# Json file read
try:
    with open(csv_file_path, 'r') as file:
        for line in csv.reader(file):
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')
