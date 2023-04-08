a = int(input('Сторона a: '))
b = int(input('Сторона b: '))
c = int(input('Сторона c: '))

if a == b + c or b == a + c or c == a + b:
    print('Это не треугольник. Это линия.')
elif a > b + c or b > a + c or c > a + b:
    print('Такого треугольника не существует')
else:
    print('Такой треугольник существует')
    if a == b or b == c or a == c:
        if a == b and b == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')