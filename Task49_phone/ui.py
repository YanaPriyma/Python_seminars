from logger import input_data, print_data, filter_data, del_data, replace_data

def interface():
    print("""Выберите режим работы:
             1 - запись данных
             2 - вывод данных
             3 - посик данных по парметрам
             4 - изменение данных
             5 - удаление данных
             """)
    command_number = int(input("Введите номер комманды: "))
    while command_number < 1 or command_number > 5:
        print("Введите корректный номер комманды:")
        command_number = int(input("Введите номер комманды: "))

    if command_number == 1:
        input_data()
    elif command_number == 2:
        print_data()
    elif command_number == 3:
        print("Введите параметры поиска через ';' :")
        filter_string = input()
        filter_data(filter_string)
    elif command_number == 4:
        print("Введите данные, которые хотите изменить: ")
        del_string = input()
        print("Введите данные для замены: ")
        replace_string = input()
        replace_data(del_string, replace_string)
    elif command_number == 5:
        print("Введите данные для удаления через ';' ")
        del_string = input()
        del_data(del_string)