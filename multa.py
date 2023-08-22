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

def isNumeric(s):
    return s.isdigit()


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
        

def check_number(str):
    '''Проверить число или нет'''
    try:
        int(str)
        return True
    except ValueError:
        return False
    

def greeting(name, finish):
    print(f'{name}, решаем примеры до {finish} \n')


def min_max(a, b):
    min_number = min(a, b)
    max_number = max(a, b)
    return min_number, max_number


def mult(a, b):
    return a * b


def name():
    n = input("Как вас зовут? ")
    return n


def pair(finish):
    a = int(random.randint(1, finish))
    b = int(random.randint(1, 10))    
    return a, b


def main():
    user = name()
    tries = int(input_number('Введи кол-во задач: '))
#    start = input_number('Введи ОТ какого числа будут начинатся примеры: ')
    finish = int(input_number('Введи ДО какого числа будут примеры: '))
#    start, finish = min_max(start, finish)
    greeting(user, finish)
    countyes = 0
    countno = 0
    for i in range(tries):
        a, b = pair(finish)
#        a = int(random.randint(start,finish))
#        b = int(random.randint(start,finish))
        print(a, 'X', b, '= ',end=' ')
        answer = int(input())
        correct = mult(a, b)
        if answer == correct:
            print('Правильно\n')
            countyes += 1
        else:
            print(f'Неправильно. Правильный ответ {correct}\n')
            countno += 1
    print('Всего примеров решено: ', tries)
    print('Правильно решено: ', countyes)
    print('Неправильно решено: ', countno)
    input('\nВведите Enter, чтобы выйти')


if __name__ == '__main__':
    main()
