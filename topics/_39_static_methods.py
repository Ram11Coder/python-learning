
# Static methods = A method that belong to a class rather than any object from that class(instance) usually used for
# general utility functions
#
# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method
    def emp_details(self):
        return f"{self.name} = {self.position}"

    # Static method
    @staticmethod
    def is_valid_job_position(position):
        job_positions = ["Developer", "Tester", "Manager"]
        return position in job_positions


print(Employee.is_valid_job_position("Manager"))
print(Employee.is_valid_job_position("Architect"))

emp1 = Employee("Ram", "Developer")
emp2 = Employee("Rocky", "Tester")

print(emp1.emp_details())
print(emp2.emp_details())
print(emp1.is_valid_job_position("Tester"))
