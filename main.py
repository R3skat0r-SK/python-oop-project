from course import *
from person import *
from school import *
from other import *


# code of program
school = School('Test IT')
add_test_data(school)


# nekonecny cyklus programu, ktory skonci na zaklade MENU -> Koniec
while True:
    result = print_menu(school)
    
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