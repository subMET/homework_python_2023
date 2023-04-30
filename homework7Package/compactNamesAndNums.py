def compactFile(num_file, name_file, res_file):
    with open(num_file, 'r', encoding='utf-8') as fn1, \
            open(name_file, 'r', encoding='utf-8') as fn2, \
            open(res_file, 'a', encoding='utf-8') as fr:
        num_list_buff = []
        name_list = []
        num_list = []
        for line in fn1:
            if line != '':
                num_list_buff.append((line.replace('\n','')).split('|'))
        for i in range(len(num_list_buff)):
            num_list.append(int(num_list_buff[i][0])*float(num_list_buff[i][1]))
        for line in fn2:
            if line != '':
                name_list.append(line.replace('\n',''))
        len_num = len(num_list)
        len_name = len(name_list)
        short_index = 0
        if len_num >= len_name:
            for i in range(len_num):
                if short_index == len_name:
                    short_index = 0
                if num_list[i] >= 0:
                    fr.write(f'{name_list[short_index].upper()} {round(num_list[i], 0)}')
                    fr.write(f'\n')
                else:
                    fr.write(f'{name_list[short_index].lower()} {abs(num_list[i])}')
                    fr.write(f'\n')
                short_index += 1
        else:
            for i in range(len_name):
                if short_index == len_num:
                    short_index = 0
                if num_list[short_index] >= 0:
                    fr.write(f'{name_list[i].upper()} {round(num_list[short_index], 0)}')
                    fr.write(f'\n')
                else:
                    fr.write(f'{name_list[i].lower()} {abs(num_list[short_index])}')
                    fr.write(f'\n')
                short_index += 1



if __name__ == '__main__':
    compactFile('test_file1.txt','test_file.txt','test_file2.txt') 