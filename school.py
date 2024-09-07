from person import *
from school import *
from course import *

class School:
    students = []
    teachers = []
    courses = []
    
    def __init__(self, name :str):
        self.name = name
        
    def add_teacher(self, teacher :Teacher):
        School.teachers.append(teacher)
    
    def remove_teacher(self, teacher :Teacher):
        School.teachers.remove(teacher)
        
    def get_teacher_by_id(self, id):
        for item in School.teachers:
            if item.id == id:
                return item
        return None
    
    def add_student(self, student :Student):
        School.students.append(student)
        
    def remove_student(self, student :Student):
        School.students.remove(student)
        
    def get_student_by_id(self, id):
        for item in School.students:
            if item.id == id:
                return item
        return None
        
    def add_course(self, course :Course):
        School.courses.append(course)
        
    def remove_course(self, course :Course):
        School.courses.remove(course)

    def get_course_by_id(self, id):
        for item in School.courses:
            if item.id == id:
                return item
        return None
    
    def print_teachers(self):
        print(f'Zoznam ucitelov skoly: {self.name}')
        for teacher in self.teachers:
            print(f'Id: {teacher.id}, Meno: {teacher}')
        print()
        
    def print_students(self):
        print(f'Zoznam studentov skoly: {self.name}')
        for student in self.students:
            print(f'Id: {student.id}, Meno: {student}')
        print()
        
    def print_courses(self):
        print(f'Zoznam kurzov skoly: {self.name}')
        for course in self.courses:
            print(f'Id: {course.id}, Nazov kurzu: {course.name}')
        print()
        
    def print_course(self, course :Course):
        print(f'Nazov kurzu: {course.name}')
        print(f'Prednasajuci: {course.teacher}')
        print(f'Zoznam studentov:')
        for student in course.students:
            print(f'Id: {student.id}, Meno: {student}')
        print()
    
    def get_id_str(self, arr :list):
        f_lambda = lambda arr: ",".join(str(item.id) for item in arr)
        return f_lambda(arr)
        
    def __str__(self):
        return 'Nazov skoly: ' + self.name