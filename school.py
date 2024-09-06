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
        
        
        
class Course:
    counter = 0
    
    def __init__(self, name :str):
        Course.counter += 1
        self.id = Course.counter
        self.name = name
        self.teacher = 0 #id ucitela, ktore urcite nesmie byt == 0
        self.students = [] #zoznam ziakov - ich id
        
    def add_teacher(self, teacher :Teacher):
        self.teacher = teacher
        
    def add_student(self, student :Student):
        self.students.append(student)
        
    def remove_student(self, student :Student):
        self.students.remove(student)
        
    def info(self):
        return 'Nazov kurzu: ' + self.name + 'Ucitel: ' + self.teacher.name + ' ' + self.teacher.surname


# hlavna trieda
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


    
def print_menu():
    #moznosti menu
    menu_keys = ('1', '11', '12', '2', '21', '22', '3', '31', '32', '33', 'K')
    
    print('MENU:')
    print(school)
    print('*' * 42)
    print('1 - Zobrazenie zoznamu ucitelov')
    print('    11 - Pridat  ucitela')
    print('    12 - Odobrat ucitela')
    print('2 - Zobrazenie zoznamu studentov')
    print('    21 - Pridat  studenta')
    print('    22 - Odobrat studenta')
    print('3 - Zobrazenie zoznamu kurzov')
    print('    31 - Pridat  kurz')
    print('    32 - Odobrat kurz')
    print('    33 - Podrobnosti o kurze podla jeho ID')
    print('*' * 42)
    print('K - Koniec programu\n')
    
    while True:
        result = input('Tvoja volba: ').upper()
        if result in menu_keys:
            return result
        else:
            print('Zadana volba nie je mozna.')


def add_test_data(school :School):
    school.add_teacher(Teacher('Peter', 'Python'))
    school.add_teacher(Teacher('Jozef', 'Csharp'))
    school.add_teacher(Teacher('Anna', 'Java'))
    
    school.add_student(Student('Adam', 'Kovac'))
    school.add_student(Student('Martina', 'Suchacova'))
    school.add_student(Student('Marcel', 'Berkes'))
    school.add_student(Student('Martin', 'Nad'))
    school.add_student(Student('Gabriel', 'Lorincz'))
    school.add_student(Student('Leopold', 'Haverl'))
    school.add_student(Student('Eva', 'Barkocziova'))
    school.add_student(Student('Julia', 'Pazurikova'))
    school.add_student(Student('Patrik', 'Novy'))
    school.add_student(Student('Peter', 'Szabo'))
    school.add_student(Student('Petra', 'Tothova'))
    
    school.add_course(Course('C#'))
    school.courses[0].add_teacher(school.teachers[1])
    school.courses[0].add_student(school.students[0])
    school.courses[0].add_student(school.students[1])
    school.courses[0].add_student(school.students[2])
    
    school.add_course(Course('Java'))
    school.courses[1].add_teacher(school.teachers[2])
    school.courses[1].add_student(school.students[3])
    school.courses[1].add_student(school.students[4])
    school.courses[1].add_student(school.students[5])
    school.courses[1].add_student(school.students[6])
    
    school.add_course(Course('Python'))
    school.courses[2].add_teacher(school.teachers[0])
    school.courses[2].add_student(school.students[8])
    school.courses[2].add_student(school.students[9])
    school.courses[2].add_student(school.students[10])

# code of program
school = School('Test IT')
add_test_data(school)


# nekonecny cyklus programu, ktory skonci na zaklade MENU -> Koniec
while True:
    result = print_menu()
    
    match result:
        case '1':
            school.print_teachers()
        case '11':
            print('Pridanie ucitela:')
            name = input('Meno: ')
            surname = input('Priezvisko: ')
            school.teachers.append(Teacher(name, surname))
            print()
        case '12':
            rs = int(input('Id ucitela (' + school.get_id_str(School.teachers) + '): '))
            school.remove_teacher(school.get_teacher_by_id(rs))
        case '2':
            school.print_students()
        case '21':
            print('Pridanie studenta:')
            name = input('Meno: ')
            surname = input('Priezvisko: ')
            school.students.append(Student(name, surname))
            print()
        case '22':
            rs = int(input('Id studenta (' + school.get_id_str(School.students) + '): '))
            school.remove_student(school.get_student_by_id(rs))
        case '3':
            school.print_courses()
        case '31':
            print('Pridanie kurzu:')
            name = input('Nazov kurzu: ')
            school.print_teachers()
            while True:
                teacher_id = input('Zadaj Id ucitela pre kurz(' + school.get_id_str(School.teachers) + '): ')
                arr=[str(x.id) for x in school.teachers]
                if teacher_id not in arr:
                    print('Nespravne Id ucitela')
                else:
                    break
            cmd = ''
            new_course = Course(name)
            new_course.add_teacher(school.get_teacher_by_id(int(teacher_id)))
            school.print_students()
            while cmd != 'end':
                while True:
                    student_id = input('Zadaj Id studenta pre kurz(' + school.get_id_str(School.students) + ', end=koniec): ')
                    arr=[str(x.id) for x in school.students]
                    arr.append('end')
                    if student_id not in arr:
                        print('Nespravne Id studenta')
                    else:
                        break
                if student_id == 'end':
                    cmd = 'end'
                    break
                else:
                    new_course.add_student(school.get_student_by_id(int(student_id)))
            school.add_course(new_course)
        case '32':
            rs = int(input('Id kurzu (' + school.get_id_str(School.courses) + '): '))
            school.remove_course(school.get_course_by_id(rs))
        case '33':
            while True:
                rs = input('Id kurzu (' + school.get_id_str(school.courses) + '): ')
                arr=[str(x.id) for x in school.courses]
                if rs not in arr:
                    print('Nespravne Id kurzu')
                else:
                    break
            school.print_course(school.get_course_by_id(int(rs)))
        case _: #koniec
            break