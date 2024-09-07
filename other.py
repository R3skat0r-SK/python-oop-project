from course import *
from person import *
from school import *

def print_menu(school):
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