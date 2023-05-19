def input_number():
    # input number
    number = int(input('Введите число для изучения: '))
    return number

def greeting(num):
    print(f'Введено число {num} \nИзучаем таблицу умножения на {num}')

def get_answer(mul_1, mul_2):
    answer = int(input(f'Введите ответ на {mul_1} x {mul_2} = ' ))
    return answer

def check_answer(mul_1, mul_2, answer):
    if answer == mul_1 * mul_2:
        print('Верно')
    else:
        print(f'Неверно. Правильный ответ {mul_1 * mul_2}')


number = input_number()
greeting(number)
answer = get_answer(number, 10)
check_answer(number, 10, answer)