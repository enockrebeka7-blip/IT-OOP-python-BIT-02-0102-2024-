
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Gradebook:
    def __init__(self):
      
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.score

        average = total / len(self.students)
        return average

student1 = Student("Alice", 80)
student2 = Student("Bob", 70)
student3 = Student("John", 90)

gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_student(student2)
gradebook.add_student(student3)

print("Class Average:", gradebook.get_average())