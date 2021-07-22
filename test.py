import os
import jsonpickle
jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)


class School_attribute:
    def __init__(self,  attribute, data):
        self.attribute = attribute
        self.data = data


class Check:
    def check_empty_space(string):
        string = str(string)
        if len(string) == 0:
            print('Данный пункт не может быть пустым, введите корректное данные')
            return True
        else:
            if string.isspace():
                print('Данный пункт не может состоять из пробелов, введите корректное данные')
                return True
            else:
                return False

    def check_alpha(string):
        string = str(string)
        replace_string = string.replace(' ','-')
        split_string = replace_string.split('-')
        # можно лучше: Добавить тримминг пробелов, чтобы строка "Иванов " верифицировалась как корректная
        for element in range(len(split_string)):
            if not split_string[element].isalpha():
                print('Данный пункт должен состоять из букв, введите корректные данные')
                return False
        return True


class School_attribute_Storage:
    def __init__(self):
        self.file_name = 'school.json'

    def overwriting():
        while True:
            name_school = input('Введите название школы: ')
            if Check.check_empty_space(name_school):                
                continue
            else:
                break

        while True:
            adress_school = input('Введите адрес школы: ')
            if Check.check_empty_space(adress_school):
                continue
            else:
                break

        school = [School_attribute('Название школы:', name_school), School_attribute('Адрес школы:', adress_school)]
        data = jsonpickle.encode(school)
        FileProvider.update_file('school.json', data)

    def get_all():
        code_school = FileProvider.get('school.json')
        school = jsonpickle.decode(code_school)
        for attribute in range(len(school)):
            print(school[attribute].attribute, school[attribute].data)

        #Можно лучше: Количество студентов хранить в поле класса, чтобы лишний раз не дергать файл.
        if not FileProvider.exist('students.json'):
            print('Количество учеников: 0')
        else:            
            code_students = FileProvider.get('students.json')
            students = jsonpickle.decode(code_students)
            number_of_students = len(students)
            print('Количество учеников:', number_of_students)


class FileProvider:
    def exist(path):
        return os.path.exists(path)

    def get(path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data

    def update_file(path, data):        
        file = open(path, 'w')
        file.write(data)
        file.close()


class Student:
    def __init__(self, student_name, age, class_number):
        self.student_name = student_name
        self.age = age
        self.class_number = class_number

    def add_student():
        while True:
            name = input('Введите ФИО ученика: ').title()
            if Check.check_empty_space(name):
                continue
            if not Check.check_alpha(name):
                continue
            else:
                break

        while True:
            age = input('Введите возраст ученика: ')
            if not age.isdigit():
                print('Данный пункт должен состоять из числа, введите корректные данные')
                continue
            #Примечание. Не ошибка, но лучше не переприсваивать значение переменной другого типа. Сначала в age у нас строка, потом число. лучше использовать разные переменные
            age = int(age)
            if age < 5 or age >= 100:
                print('Возраст ученика не может быть меньше 5 и больше 99 лет, введите корректные данные')
                continue
            else:
                break
        age = str(age)

        while True:
            class_number = input('Введите номер класса в котором обучается ученик: ')
            # Поправить!!! Класс может быть с буквой. Например 5а, 6г и т.п. ну и классов максимум 12
            if not class_number.isdigit():
                print('Данный пункт должен состоять из числа, введите корректные данные')
                continue
            class_number = int(class_number)
            if class_number < 1 or class_number > 20:
                print('Номер класса не может быть менее 1 и более 20, введите корректные данные')
                continue
            else:
                break
        class_number = str(class_number)

        new_student = Student(name, age, class_number)

        #Можно лучше: не помешала бы оптимизация. вывод в файл можно вынести за if
        if not FileProvider.exist('students.json'):
            new_student = [new_student]
            code_new_student = jsonpickle.encode(new_student)
            FileProvider.update_file('students.json', code_new_student)
        else:
            code_students = FileProvider.get('students.json')
            students = jsonpickle.decode(code_students)
            students.append(new_student)
            new_code_students = jsonpickle.encode(students)
            FileProvider.update_file('students.json', new_code_students)

    def del_student():
        if not FileProvider.exist('students.json'):
            print('Нет доступных учеников для удаления!')
        else:
            code_students = FileProvider.get('students.json')
            students = jsonpickle.decode(code_students)
            if len(students) == 0:
                print('Нет доступных учеников для удаления!')
            else:
                for student in range(len(students)):
                    print(student+1, students[student].student_name)

                while True:
                    number_student = input('Введите номер ученика для удаления: ')
                    if not number_student.isdigit():
                        print('Данный пункт должен состоять из числа, введите корректные данные')
                        continue
                    else:
                        number_student = int(number_student)
                        if number_student < 1 or number_student > len(students):
                            print('Введите номер ученика от 1 до', len(students))
                        else:
                            break

                students.pop(number_student-1)
                new_dell_code_students = jsonpickle.encode(students)
                FileProvider.update_file('students.json', new_dell_code_students)

    def show_students():
        if not FileProvider.exist('students.json'):
            print('В школе нет учеников!')
        else:
            code_students = FileProvider.get('students.json')
            students = jsonpickle.decode(code_students)
            if len(students) == 0:
                print('В школе нет учеников!')
            else:                

#Если нужно выровнять по центру, можно написать типа такого: f'{value:^30}. Тогда под вывод выделится 30 знакомест, а value встанет по середине

                print(f'{"НОМЕР":30}{"ИМЯ":40}{"ВОЗРАСТ":30}{"НОМЕР КЛАССА":30}')
                for student in students:
                    print(f'{str(students.index(student)+1):22}{student.student_name:52}{student.age:33}{student.class_number:10}')


class Menu:
    def main_menu(self):
        while True:
            print()
            main_menu = ['Получение полной информации о школе', 'Изменение информации о школе', 'Просмотр учеников школы', 'Добавление нового ученика школы', 'Удаление имеющегося ученика школы', 'Выход из программы']
            for element in range(len(main_menu)):
                print(element+1, main_menu[element])

            print()
            while True:
                command = input('Введите номер команды: ')
                if not command.isdigit():
                    print('Данный пункт должен состоять из числа, введите корректные данные')
                    continue
                else:
                    command = int(command)
                    if command < 1 or command > len(main_menu):
                        print('Введите номер команды от 1 до', len(main_menu))
                        continue
                    else:
                        break

            print()
            if command == 1:
                School_attribute_Storage.get_all()
            if command == 2:
                School_attribute_Storage.overwriting()
            if command == 3:
                Student.show_students()
            if command == 4:
                Student.add_student()
            if command == 5:
                Student.del_student()
            if command == 6:
                print('До свидания!')
                break


main_menu = Menu()
print('Здравствуйте')

if not FileProvider.exist('school.json'):
    School_attribute_Storage.overwriting()

main_menu.main_menu()