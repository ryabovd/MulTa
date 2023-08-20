#Таблица умножения
#Задает примеры для решения по таблице умножения. Можно самому настроить диапазон чисел для примеров.

import random


def input_number(text):
    ''' input number for number tasks or start number or finish number'''
    text.strip()
    number = int(input(text))
    return number


def check_number(text):
    '''Проверить число или нет'''
    if text.isnumeric():
        return int(text)
    else:
        pass


def greeting(start, finish):
    print(f'Решаем примеры от {start} до {finish} \n')


def mult(a, b):
    return a * b


def main():
    tries = input_number('Введи кол-во задач: ')
    start = input_number('Введи ОТ какого числа будут начинатся примеры: ')
    finish = input_number('Введи ДО каким числом будут заканчиваться примеры: ')
    greeting(start, finish)
    countyes = 0
    countno = 0
    for i in range(tries):
        a = int(random.randint(start,finish))
        b = int(random.randint(start,finish))
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
