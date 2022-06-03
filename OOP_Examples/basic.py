class Student:
    def __init__(self):
        self.name = "MiamiHacker"
        self.grades = (64, 54, 71, 42, 89)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student()

print(student.name)
print(student.average())