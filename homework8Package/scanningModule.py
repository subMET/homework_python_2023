import csv
import json
import os



def scanningDirectoria(dir = os.getcwd(), jsonName = None, csvName = None):
    dir_list = [['name','path','type','size','files']]
    for dir_path, dir_name, file_name in os.walk(dir):
        # print(f'{dir_name = }\n{dir_path = }\n{file_name = }\n')
        if os.path.isdir(dir_path):
            file_type = 'dir'
        stats = os.stat(dir_path)
        dir_list.append([fileName(dir_path),filePath(dir_path),file_type,stats.st_size,file_name])
    file_list = []
    for i in range(1,len(dir_list)):
        for j in range(len(dir_list[i][4])):
            stats = os.stat(os.path.join(dir_list[i][1],dir_list[i][0],dir_list[i][4][j]))
            file_list.append([dir_list[i][4][j],os.path.join(dir_list[i][1],dir_list[i][0]),'file',stats.st_size,'-']) 
    scan_list = dir_list + file_list
    if jsonName != None:
        with open(jsonName,'w',encoding='utf-8') as jFile:
            json.dump(scan_list,jFile)
    if csvName != None:
        with open(csvName,'w',encoding='utf-8') as cFile:
            csv_write = csv.writer(cFile,dialect='excel')
            csv_write.writerows(scan_list)
    return scan_list

def filePath(path):
    i = len(path) - 1
    while path[i] != '\\':
        i-= 1
    path = path[0:i]
    return path

def fileName(path):
    name = path
    l = len(name)
    i = l - 1
    while name[i] != '\\':
        i-= 1
    name = name[i+1:l]
    return name


if __name__ == '__main__':
    print(scanningDirectoria(os.path.join(os.getcwd(), 'lessons','l1'),jsonName='json_scan.json',csvName='csv_scan.csv'))
    # print(scanningDirectoria(os.path.join(os.getcwd())))