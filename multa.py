#Таблица умножения
#Задает примеры для решения по таблице умножения. Можно самому настроить диапазон чисел для примеров.

import random


def input_number(text):
    ''' input number for number tasks or start number or finish number'''
    number = input(text).strip()
    while True:
        if check_number(number) == True:
            return number
        else:
            print(f"{number} не является числом. \nВведите новое число \n")
            number = input(text).strip()       


"""def isNumeric(s):
    return s.isdigit()"""


"""def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False"""
        

def check_number(str):
    '''Проверить число или нет'''
    try:
        int(str)
        return True
    except ValueError:
        return False
    

def greeting(user_name, finish):
    print(f'{user_name}, решаем примеры до {finish} \n')


"""def min_max(a, b):
    min_number = min(a, b)
    max_number = max(a, b)
    return min_number, max_number"""


def mult(a, b):
    return a * b


def user_name():
    name = input("Как вас зовут? ")
    return name


def check_user_name(user_name):
    pass


def add_user_name(user_name):
    pass


def pair(finish):
    a = int(random.randint(1, finish))
    b = int(random.randint(1, finish))    
    return a, b


def read_text_file(name_file):
    with open(name_file + '.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_text_file(name_file, mode, list_of_strings):
    with open(name_file + ".txt", mode, encoding="utf-8") as f:
        f.writelines(list_of_strings)


def list_of_strings(dict):
    list_of_strings = []
    for key in dict:
        line = key + ', ' + dict[key] + '\n'
        list_of_strings.append(line)
    return list_of_strings


def list_of_strings_from_list(list):
    list_of_strings = []
    string = ''
    for i in list:
        str = (', ').join(i) + '\n'
        string += str
    list_of_strings.append(string)
    return list_of_strings


def readlines(name_file):
    with open(name_file + '.txt', 'r', encoding='utf-8') as f:
        list = f.readlines()
    return list


def create_list(list):
    text_list = []
    for line in list:
        line = line.strip().split(', ')
        text_list.append(line)
    return text_list


def create_dict(list):
    dict = {}
    for line in list:
        line = line.strip().split(', ')
        name, number = line
        dict[name] = number
    return dict


def diff_stat(user_stat, result_list):
    new_user_stat = user_stat
    for i in result_list:
        a, b, result = i
        new_user_stat[a-1][b-1] = str(round((float(new_user_stat[a-1][b-1]) + result)/2, 2))
    return new_user_stat


def main():
    users = readlines('users')
    user_dict = create_dict(users)
    print(user_dict)
    name = user_name()
    if name in user_dict:
        finish = int(user_dict[name])
    else:
        finish = int(input_number(f'{name}, до какого числа учим таблицу (10, 20)? '))
        user_dict[name] = finish
        write_text_file('users', 'a', [name + ', ' + str(finish) + '\n'])
        # Записать файл для нового пользователя
        new_user_data_list = ['0, ' for i in range(finish-1)] + ['0\n']
        new_user_data_list = new_user_data_list * finish
        print(new_user_data_list)
        write_text_file(name, 'w', new_user_data_list)
        #Добавить пользователя и число до которого решаем примеры в словарь
        #Добавить пользователя и число в файл пользователей
        # продолжаем программу
#    start = input_number('Введи ОТ какого числа будут начинатся примеры: ')
#    finish = int(input_number('Введи ДО какого числа будут примеры: '))
#    start, finish = min_max(start, finish)
    greeting(name, finish)
    tries = int(input_number('Введи кол-во задач: '))
    user_stat = create_list(readlines(name))
#    print(name)
#    print(user_stat)
    countyes = 0
    countno = 0
    result_list = []
    for i in range(tries):
        a, b = pair(finish)
#        a = int(random.randint(start,finish))
#        b = int(random.randint(start,finish))
        print(a, 'X', b, '= ',end=' ')
        answer = int(input_number(""))
        correct = mult(a, b)
        if answer == correct:
            print('Правильно\n')
            countyes += 1
            result_list.append([a, b, 1])
        else:
            print(f'Неправильно. Правильный ответ {correct}\n')
            countno += 1
            result_list.append([a, b, 0])
    print('Всего примеров решено: ', tries)
    print('Правильно решено: ', countyes)
    print('Неправильно решено: ', countno)
#    print(result_list)
    new_stat = diff_stat(user_stat, result_list)
#    print('new_stat', new_stat)
#    print(list_of_strings_from_list(new_stat))
    write_text_file(name, 'w', list_of_strings_from_list(new_stat))
    input('\nВведите Enter, чтобы выйти')


if __name__ == '__main__':
    main()

"""
Найти в файле статистики результаты < 0.8
Привести их к виду [a, b] и записать в список списков
По длине списка случайно выбирать списки [a, b] и фиксировать ответы
Записать ответы в файл статистики
"""