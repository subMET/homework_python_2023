a = int(input('Введите целое число: '))
d = {0:0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, \
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
b = a
inverse = ''
hex_a = ''
while b > 0:
    inverse += str(d.get(b%16))
    b = b//16
for i in range(len(inverse)):
    hex_a += inverse[-i-1]
print(hex_a, hex(a))