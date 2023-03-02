# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = 'data.txt'

def print_data():
    if os.path.exists(file_name):
        print("Вывoд данных из файла: ")
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("Файла не существует.")

def input_data():
    print("Введите данные для добавления в файл: ")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{name}; {surname}; {phone}; {adress}\n')


def filter_data(filter_string):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        if ';' in filter_string:
            list_filter = filter_string.split(';')
        else:
            list_filter = [filter_string]
        is_found = False

        for element in list_data:
            temp_record = element.split(';')
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower() and len(element_filter.lower())==len(record.lower()):
                        count += 1
            if count == len(list_filter):
                print(element)
                is_found = True
    if not is_found:
        print("Таких засисей нет. ")

# домашнее задание

def del_data(del_string):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        is_found = False
        out_data = []
        for element in list_data:
            temp_record = element.split(';')
            for record in temp_record:
                if del_string.lower() == record.lower():
                    out_data.append(element)
                    print(
                        f"Удалить запись? {temp_record}? \n Введите ДА/НЕТ")
                    if input().lower() == "да".lower():
                        out_data.remove(element)
                        is_found = True
                        print(f"Запись {temp_record} удалена.\n")
        if not is_found:
            print("Запись не существует. ")
        else:
            with open(file_name, 'w', encoding='utf-8') as file:
                for line in out_data:
                    file.write(line)


def replace_data(del_string, replace_string):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        is_found = False
        for i in range(len(list_data)):
            temp_record = list_data[i].split(';')
            for j in range(len(temp_record)):
                if temp_record[j].lower() == del_string.lower():
                    print(
                        f"Заменить запись {del_string} на {replace_string}?\n Введите ДА/НЕТ")
                    if input().lower() == "да".lower():
                        temp_record[j] = replace_string
                        is_found = True
                        print(f"Запись {temp_record} изменена.\n")
                        list_data.remove(list_data[i])
                        list_data.insert(i, ';'.join(temp_record))
        if not is_found:
            print("Запись не существует. ")
        else:
            with open(file_name, 'w', encoding='utf-8') as file:
                for line in list_data:
                    file.write(line)