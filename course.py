from person import *

class Course:
    counter = 0
    
    def __init__(self, name :str):
        Course.counter += 1
        self.id = Course.counter
        self.name = name
        self.teacher = 0 #id ucitela, ktore urcite nesmie byt == 0p
        self.students = [] #zoznam ziakov - ich id
        
    def add_teacher(self, teacher :Teacher):
        self.teacher = teacher
        
    def add_student(self, student :Student):
        self.students.append(student)
        
    def remove_student(self, student :Student):
        self.students.remove(student)
        
    def info(self):
        return 'Nazov kurzu: ' + self.name + 'Ucitel: ' + self.teacher.name + ' ' + self.teacher.surname