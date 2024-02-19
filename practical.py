class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self._grades = {
            'English': 0,
            'calculus': 0,
            'economics': 0,
            'philosophy': 0
        }

    def add_grade(self, subject, grade):
        if subject in self._grades:
            self._grades[subject] = grade

    def average_grade(self):
        total_grade = 0
        for grade in self._grades.values():
            total_grade += grade
        return total_grade / len(self._grades)

    @property
    def display_details(self):
        return f'{self.student_id} - {self.name}, grades: {self._grades}'


class StudentManagementSystem(Student):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.students = {}

    def add_student(self, student_id, name):
        self.students[student_id] = Student(student_id, name)

    def show_student_details(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_details
        else:
            return 'the student is not studying in our university'

    def show_student_average_grade(self, student_id):
        if student_id in self.students:
            return self.students[student_id].average_grade()
        else:
            return 'the student is not studying in our university'

management = StudentManagementSystem('id','name')
management.add_student("1", "Alice")
management.add_student("2", "Bob")


management.students["1"].add_grade("English", 85)
management.students["1"].add_grade("Calculus", 90)
management.students["2"].add_grade("Economics", 75)
management.students["2"].add_grade("Philosophy", 80)


print(management.show_student_details("1"))
print(management.show_student_details("2"))
print(management.show_student_average_grade("1"))
print(management.show_student_average_grade("2"))