from random import randint, uniform

def addRandomPairs(file_name, lines_amount):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(lines_amount):
            int_a = randint(-1000,1000)
            float_a = uniform(-1000,1000)
            f.write(f'{int_a}|{float_a}\n')

if __name__ == '__main__':
    addRandomPairs('test_file1.txt',10)