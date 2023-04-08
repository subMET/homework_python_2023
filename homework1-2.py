a = int(input('Введите число от 1 до 100000 : '))
while a not in range(1, 100001):
    print('Неверный ввод')
    a = int(input('Введите число от 1 до 100000 : '))

b = 2
check = True
while check and b <= int(a/b):
    if a % b == 0:
        check = False
    b += 1
if check:
    print(f'Число {a} простое.')
else:
    print(f'Число {a} составное.')
