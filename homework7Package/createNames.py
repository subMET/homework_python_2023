from random import randint
# 97-122

def addRandomNames(file_name, names_amount):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(names_amount):
            j = randint(5,7)
            char_list = []
            while j > 0:
                char_list.append(str(chr(randint(97,122))))
                j-= 1
            name = ''.join(char_list)
            f.write(f'{name}\n')

if __name__ == '__main__':
    addRandomNames('test_file.txt',10) 
