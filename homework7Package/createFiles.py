import os
from random import randint

def createRandomFiles(extension, directoria = '', minLen = 6, maxLen = 30, minByte = 256, maxByte = 4096, count = 42):
    for i in range(count):
        char_list = []
        rand_length = randint(6,30)
        rand_byte = randint(256,4096)
        for j in range(rand_length):
            char_list.append(str(chr(randint(97,122))))
        rand_name = ''.join(char_list)
        if directoria == '':
            if not os.path.exists(f'{rand_name}.{extension}'):
                with open(f'{rand_name}.{extension}','wb') as rf:
                    rf.write(b'X' * rand_byte)
        else:
            if not os.path.exists(directoria):
                os.mkdir(directoria)
            if not os.path.exists(f'{directoria}/{rand_name}.{extension}'):
                with open(f'{directoria}/{rand_name}.{extension}','wb') as rf:
                    rf.write(b'X' * rand_byte)           
    
def createRandomFiles2(extensions):
    for i in range(len(extensions)):
        createRandomFiles(extension = extensions[i][0],count = extensions[i][1])


if __name__ == '__main__':
    createRandomFiles('txt',count = 1) 
    # createRandomFiles2([['txt',3],['py',2]])
