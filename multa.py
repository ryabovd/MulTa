#Таблица умножения
#Задает примеры для решения по таблице умножения. Можно самому настроить диапазон чисел для примеров.

import random
import datetime
import time
import smtplib
import json


def input_number(text):
    ''' input number for number tasks or start number or finish number'''
    number = input(text).strip()
    while True:
        if check_number(number) == True:
            return number
        else:
            print(f"{number} не является числом. \nВведите новое число \n")
            number = input(text).strip()       
        

def check_number(str):
    '''Проверить число или нет'''
    try:
        int(str)
        return True
    except ValueError:
        return False
    

def greeting(user_name, finish):
    print(f'{user_name}, решаем примеры до {finish} \nНе бойся ошибаться! \nЯ тебя натренирую!')


def mult(a, b):
    return a * b


def user_name():
    name = input("Как тебя зовут? \nВведи имя для загрузки статистики занятий ... ")
    return name


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


def search_stat(user_stat):
    min_result = 0.8
    search_result_list = []
    for a in range(len(user_stat)):
        for b in range(len(user_stat[a])):
            if float(user_stat[a][b]) <= min_result:
                search_result_list.append([a+1, b+1])
            else:
                continue
    return search_result_list


def print_stat(list):
    for el in list:
        print(el)


def send_notification_email(text):
    email = ['dmitryabov@yandex.ru', 'tomas1309@yandex.ru']
    with open('settings.json', 'r', encoding='utf-8') as file:
        settings = json.load(file)
        sender = settings["sender"]
        sender_password = settings["sender_password"]
    mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_lib.login(sender, sender_password)
    for to_item in email:
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
            sender, to_item, 'Изучение таблицы умножения {}'.format(date_today()))
        msg += text
        mail_lib.sendmail(sender, to_item, msg.encode('utf8'))
    print('Данные отправлены на ' + (', ').join(email).upper())
    mail_lib.quit()


def text_for_email(user_name, result_list):
    email_text = f"{user_name} решил {len(result_list)} заданий.\n"
    return email_text


def date_today():
    '''Func that returned today date'''
    today = datetime.date.today()
    return today


def response_time(time_start, time_end):
    return time_end - time_start


def time_now():
    return time.monotonic()


def grade_lesson(tries, countyes):
    mark = 'нет оценки'
    #print('countyes / tries', countyes / tries)
    if countyes / tries >= 0.9:
        mark = 'Отлично! Пять! Пятак! Ты, умничка!'
    elif 0.8 <= countyes / tries < 0.9:
        mark = 'Хорошо! Четыре! Четвертак! Ты, молодец!'
    elif 0.67 <= countyes / tries < 0.8:
        mark = 'Удовлетворительно. Три. Удовл. Трояк.'     
    elif 0.2 <= countyes / tries < 0.67:
        mark = 'Неудовлетворительно. Два. Пара. Гусь. Двояк!'
    elif 0 <= countyes / tries < 0.2:
        mark = 'Кол. Единица. \nЭто фиаско, братан! \nНужно еще поучить.'
    return mark


def right_time(time_answer):
    if time_answer <= 10:
        return True
    else:
        return False
    

def check_users_file():
    try:
        file = open('users.txt')
    except IOError as e:
        #print(u'не удалось открыть файл users.txt\n создаем файл users.txt')
        write_text_file('users', 'w', ['test, 1\n'])
    else:
        pass


def main():
    check_users_file()
    users = readlines('users')
    user_dict = create_dict(users)
    #print(user_dict)
    name = user_name()
    if name in user_dict:
        finish = int(user_dict[name])
    else:
        finish = int(input_number(f'{name}, до какого числа учим таблицу (5, 10, 20, любое число)? '))
        user_dict[name] = finish
        write_text_file('users', 'a', [name + ', ' + str(finish) + '\n'])
        # Записать файл для нового пользователя
        new_user_data_list = ['0, ' for i in range(finish-1)] + ['0\n']
        new_user_data_list = new_user_data_list * finish
        #print(new_user_data_list, '\n')
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
    #print_stat(user_stat)
    #print()
    search_result_list = search_stat(user_stat)
    #print('search_result_list', search_result_list)
#    print(name)
#    print(user_stat)
    countyes = 0
    countno = 0
    result_list = []
    best_time = 3600.0
    worst_time = 0
    #print('round(len(search_result_list) * 0.8, 0)', round(len(search_result_list) * 0.8, 0))
    #print('tries', tries)
    i = 1
    while i <= tries * 0.8:
        #print("i", i)
        #print("tries", tries)
        #print("Внутренний цикл")
        if len(search_result_list) == 0:
            break
        elem = int(random.randint(0, len(search_result_list)-1))
        a, b = search_result_list[elem]
        print(a, 'X', b, '= ',end=' ')
        time_start = time_now()
        #print('time_start', time_start)
        answer = int(input_number(""))
        time_end = time_now()
        #print(time_end)
        time_answer = response_time(time_start, time_end)
        #print(time_answer)
        if time_answer < best_time:
            best_time = time_answer
        if time_answer > worst_time:
            worst_time = time_answer
        correct = mult(a, b)
        if answer == correct:
            print('Правильно\n')
            countyes += 1
            if right_time(time_answer) == True:
                result_list.append([a, b, 1])
            else:
                result_list.append([a, b, 0])                
                print(f'Время ответа {time_answer:>.1f}. Решай быстрее!')
        else:
            print(f'Неправильно. Правильный ответ {correct}\n')
            countno += 1
            result_list.append([a, b, 0])
            #print(f'Время ответа {time_answer:>3f}')
        i += 1
        

    for j in range(tries - i + 1):
        #print("Внешний цикл")
        #print("j", j)
        a, b = pair(finish)
#        a = int(random.randint(start,finish))
#        b = int(random.randint(start,finish))
        print(a, 'X', b, '= ',end=' ')
        time_start = time_now()
        #print('time_start', time_start)
        answer = int(input_number(""))
        time_end = time_now()
        #print(time_end)
        time_answer = response_time(time_start, time_end)
        #print(time_answer)
        if time_answer < best_time:
            best_time = time_answer
        if time_answer > worst_time:
            worst_time = time_answer
        #answer = int(input_number(""))
        correct = mult(a, b)
        if answer == correct:
            print('Правильно\n')
            countyes += 1
            if right_time(time_answer) == True:
                result_list.append([a, b, 1])
            else:
                result_list.append([a, b, 0])                
                print(f'Время ответа {time_answer:>.1f}. Решай быстрее!')
        else:
            print(f'Неправильно. Правильный ответ {correct}\n')
            countno += 1
            result_list.append([a, b, 0])
    print('Всего примеров решено: ', tries)
    print('Правильно решено: ', countyes)
    print('Неправильно решено: ', countno)
    print(f'Самый быстрый ответ {best_time:.1f} секунд')
    print(f'Самый долгий ответ {worst_time:.1f} секунд')
    print(grade_lesson(tries, countyes))
    new_stat = diff_stat(user_stat, result_list)
    #print_stat(new_stat)
    write_text_file(name, 'w', list_of_strings_from_list(new_stat))
    email_text = text_for_email(name, result_list)
    #send_notification_email(email_text)
    input('\nВведите Enter, чтобы выйти ')


if __name__ == '__main__':
    main()

"""
Найти в файле статистики результаты < 0.8
Привести их к виду [a, b] и записать в список списков
По длине списка случайно выбирать списки [a, b] и фиксировать ответы
Добавить 20% заданий из общего списка для повторения.
Записать ответы в файл статистики

ВАЖНО
Написать функцию проверки ответа, чтобы сократить код и не повторяться.

Написать функцию, которая оценивает время ответа и, если время больше 10 секунд, то 
для статистики этот ответ засчитывается как неверный.

Написать функцию для отправки результатов на e-mail родителям.

Написать функцию для определения времени ответа на задание.
Написать функции для вывода минимального и максимального времени ответа на задание.

Написать функцию для проверки таблицы результатов и, если коэффициенты больше 0.8, то увеличить область изучаемой таблицы умножения на 1
"""