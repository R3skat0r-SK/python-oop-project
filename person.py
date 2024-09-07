class Person:
    def __init__(self, name :str, surname :str):
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return self.name + ' ' + self.surname
       
# childs
class Student(Person):
    counter = 0
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Student.counter += 1
        self.id = Student.counter
    
class Teacher(Person):
    counter = 0
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Teacher.counter += 1
        self.id = Teacher.counter