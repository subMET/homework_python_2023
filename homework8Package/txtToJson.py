import json


def jsonForm(fileR, fileW):
    json_dict = {}
    buffer_list = []
    with open(fileR, 'r', encoding='utf-8') as fileRead:
        for line in fileRead:
            buffer_list.append(line.split(' '))
    for i in range(len(buffer_list)):
        buffer_list[i][1] = buffer_list[i][1].replace('\n', '')
    json_dict.update(buffer_list)
    with open(fileW, 'w', encoding='utf-8') as fileWrite:
        json.dump(json_dict,fileWrite)


if __name__ == '__main__':
    jsonForm('test_file2.txt','json_test.json')
