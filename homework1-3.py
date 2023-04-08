import random

a = random.randint(0,1000)
attempts = 10
win = False
print('Программа загадала число.')
while attempts > 0 and not win:
    print(f'Угадайте число. Попыток осталось: {attempts}.')
    b = int(input('Введите число: '))
    if b == a:
        win = True
    else:
        if b > a:
            print ('Меньше.')
        if b < a:
            print ('Больше.')
        attempts -= 1
if win:
    print('Поздравляем, вы победили.')
else:
    print('Поражение. Удачи в следующий раз.')
    