import csv
import json


def csvDatabaseTransformer(fileC,fileR):
    with open(fileC,'r',encoding='utf-8') as dbC:
        csv_file = csv.reader(dbC)
        buffer_list = []
        for line in csv_file:
            if line != []:
                buffer_list.append(line)
    buffer_list[0].append('hash')
    for i in range(1,len(buffer_list)):
        buffer_list[i].append(hash(buffer_list[i][1] + buffer_list[i][2]))
        buffer_list[i][1] = f'{buffer_list[i][1]:0>10}'
        buffer_list[i][2] = buffer_list[i][2].title()
    dicts_list = []
    for i in range(1,len(buffer_list)):
        buffer_dict = {buffer_list[0][0]:buffer_list[i][0],buffer_list[0][1]:buffer_list[i][1], \
                       buffer_list[0][2]:buffer_list[i][2],buffer_list[0][3]:buffer_list[i][3],}
        dicts_list.append(buffer_dict)
    with open(fileR,'w',encoding='utf-8') as dbJR:
        json.dump(dicts_list,dbJR)




if __name__ == '__main__':
    csvDatabaseTransformer('csv_db.csv','json_result.json')