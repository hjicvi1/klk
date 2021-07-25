# -*- coding: utf-8 -*-
import random
import os
import jsonpickle

jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)
file_name = 'schools.json'

class FileProvider:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data

    def append(self, path, data):
        file = open(path, 'a')
        data = file.write(data)
        file.close()

    def writelines(self, path, data):
        file = open(path, 'w')
        data = file.write(data)
        file.close()

    def exists(self, path):
        return os.path.exists(path)

    def clear(self, path):
        file = open(path, 'w')
        file.write("")
        file.close()




class School:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.students = []

# GET говорит нам о том, что функция доолжна возвращать студентов. не печатать, а именно возвращать. Печать это отдельная задача
    def get_all_students(self, select_item):
        name = 'Имя ученика'
        age = 'Возраст'
        class_number = 'Номер класса'
        print(f'{name:15}{age:10}{class_number:10}')

        students = select_item
        for player in students:
            print(f'{player.students.name:15}{player.students.age:10}{player.students.class_number:10}')

    


class Storage:
    def __init__(self, path):
        self.file_path = path

    def get_all(self):
        if not file_provider.exists(self.file_path):
            schools = []
            self.safe_data(schools)

        data = file_provider.get(self.file_path)
        schools = jsonpickle.decode(data)
        return schools

    def add_data(self, school):
        schools = self.get_all()
        schools.append(school)
        self.safe_data(schools)

    def safe_data(self, schools):
        json_data = jsonpickle.encode(schools)
        file_provider.writelines(self.file_path, json_data)

    def edit_data(self, schools_list):
        schools = self.get_all()
        schools = schools_list
        self.safe_data(schools)

class Student:
    def __init__(self, name, age, class_number):
        self.name = name
        self.age = age
        self.class_number = class_number


file_provider = FileProvider()
storage = Storage(file_name)

def print_schools():
    school_list = storage.get_all()
    for schools in school_list:
        print(f'{schools.name:15}{schools.adress:15}')



while True:
    print('Выберите что вы хотите сделать:')
    print("1. Добавить данные о новой школе:")
    print("2. Получение полной информации о школе:")
    print("3. Изменение информации о школе")
    print("4. Просмотр учеников школы в виде таблицы")
    print("5. Добавление нового ученика школы")
    print("6. Удаление имеющегося ученика школы")
    print("0. выйти из программы")
    cmd = input("Выберите пункт: ")

#Общее замечание, то что в теле if, лучше вынести в отдельныее функции, а тут вызывать их, чтобы код  был более читаемым и чистым

    if cmd == "1":
        print('Давайте введем информацио о школе')
        name = input('Введите название школы \n')
        adress = input('Введите адресс школы \n')
        #Как выглядет проверка в общем случае?
        '''
        while True:
            name = input()
            if name == '':
                print('error')
            else:
                break
        '''
        if name == '' or adress == '':
            print('Вы ввели пустую строку')
            continue
        school = School(name, adress)
        storage.add_data(school)
    elif cmd == "2":
        school_list = storage.get_all()
# Вот тут ведь правильно организовал проверку
        while True:
            print('Выберите школу о которой хотите получить информацию:')
            for i in range(len(school_list)):
                print(f'{i + 1}.{school_list[i].name:15}')
            user_input = input('\n')
# я бы еще проверил, что такое число школ есть. Например школ всего 3, а ввели число 7
            if not user_input.isdigit():
                print('Вы ввели не число')
                continue
            index = int(user_input) - 1
            select_item = school_list[index]
            print(f'{select_item.name:15}{select_item.adress:15}')
            break
    elif cmd == "3":
        school_list = storage.get_all()
        print('Выберите школу которую хотите изменить')
        for i in range(len(school_list)):
            print(f'{i + 1}.{school_list[i].name:15}{school_list[i].adress:15}')
        user_input = input('\n')
#а тут опять не правильно
        if not user_input.isdigit():
            print('Вы ввели не число')
            continue
        index = int(user_input) - 1
        select_item = school_list[index]
        select_item.name = input('Введите новое название \n')
        if select_item.name == '':
            print('Вы ввели пустую строку')
            continue
        select_item.adress = input('Введите новый адресс \n')
        if select_item.adress == '':
            print('Вы ввели пустую строку')
            continue
#  не понял логику, что ты тут нагородил.
#Тебе надо у scool_list[index] переприсвоить имя и адрес. Причем я бы сделал так. Если имя или адрес не введен (пустая строка), то не переприсваивать
        school_list[index] = select_item
        for i in range(len(school_list)):
            storage.edit_data(school_list)
    elif cmd == "4":
        schools = storage.get_all()
    #У тебя вывод списка школ и запрос номера повторяется везде. Можно вынести в отдельную функцию, которая принимает schools и возвращает номер, который выбран
        print('Выберите школу в которой хотите посмотреть учеников')
        for i in range(len(schools)):
            print(f'{i + 1}.{schools[i].name:15}{schools[i].adress:15}')
    #Проверь что будет если введешь не число
        user_input = input('\n')
        while True:
            if not user_input.isdigit():
                print('Вы ввели не число')
                continue
            break
        index = int(user_input) - 1
        select_item = schools[index]
        name = 'Имя ученика'
        age = 'Возраст'
        class_number = 'Номер класса'
        print(f'{name:15}{age:10}{class_number:10}')

        students = select_item.students
        for i in range(len(students)):
            print(f'{i + 1}.{students[i].name:15}{students[i].age:10}{students[i].class_number:10}')
    elif cmd == "5":
    
#Тоже проверка не прваильная. См пример выше.
        student_name = input('Введите ФИО ученика \n')
        if student_name == '':
            print('Вы ввели пустую строку')
            continue
        student_age = input('Введите возраст ученика \n')
        if student_age == '' or not student_age.isdigit():
            print('Вы ввели некоректные данные')
            continue
        class_number = input('Введите номер класса \n')
        if class_number == '' or not class_number.isdigit():
            print('Вы ввели некоректные данные')
            continue
        new_student = Student(student_name, student_age, class_number)
        schools = storage.get_all()
        print('Выберите школу в которую хотите добавить ученика')
        for i in range(len(schools)):
            print(f'{i + 1}.{schools[i].name:15}{schools[i].adress:15}')
        user_input = input('\n')
        while True:
            if not user_input.isdigit():
                print('Вы ввели не число')
                continue
            break
        index = int(user_input) - 1
        select_item = schools[index]
        select_item.students.append(new_student)
        schools[index] = select_item
        for i in range(len(schools)):
            storage.edit_data(schools)
    elif cmd == "6":
        schools = storage.get_all()
        print('Выберите школу в которой хотите удалить ученика')
        for i in range(len(schools)):
            print(f'{i + 1}.{schools[i].name:15}{schools[i].adress:15}')
        user_input = input('\n')
        while True:
            if not user_input.isdigit():
                print('Вы ввели не число')
                continue
            break
        index = int(user_input) - 1
        select_item = schools[index]
        name = 'Имя ученика'
        age = 'Возраст'
        class_number = 'Номер класса'
        print(f'{name:15}{age:10}{class_number:10}')
        students = select_item.students
        for i in range(len(students)):
            print(f'{i + 1}.{students[i].name:15}{students[i].age:10}{students[i].class_number:10}')
        print('Выберите ученика')

    #Опять что будет если введешь не число?
        user_select = input('\n')
        while True:
            if not user_select.isdigit():
                print('Вы ввели не число')
                continue
            break
        select = int(user_select) - 1
        students.pop(select)
        for i in range(len(schools)):
            storage.edit_data(schools)
    elif cmd == "0":
        break
    else:
        print("Вы ввели не правильное значение")
    break