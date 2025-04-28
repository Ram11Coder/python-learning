# Class Method = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself
# Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        print(f"{self.name} = {self.gpa}")

    @classmethod
    def get_count(cls):
        print(f"Total student count : {cls.count}")

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa of total students : {cls.total_gpa / cls.count:.2f}"


student1 = Student("David", 3.4)
student2 = Student("Vikram", 2.5)
student3 = Student("Manoj", 2.4)

student1.get_info()
student2.get_info()
student3.get_info()

print(Student.get_average_gpa())
Student.get_count()