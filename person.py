class Person:
    counter = 0
    
    def __init__(self, name :str, surname :str):
        Person.counter += 1
        self.id = Person.counter
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return self.name + ' ' + self.surname
       
# childs
class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
class Teacher(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)