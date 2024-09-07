from course import *
from person import Person, Student, Teacher
from school import *

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