import json
import csv

def jsonToCsv(fileJ, fileC):
    with open(fileJ,'r',encoding='utf-8') as dbj:
        working_dict = json.load(dbj)
    print(working_dict)
    csv_table = [['access','id','name']]
    for access in working_dict:
        for id in working_dict[access]:
            csv_table.append([int(access),int(id),working_dict[access][id]])
    print(csv_table)
    with open(fileC,'w',encoding='utf-8') as dbc:
        csv_write = csv.writer(dbc,dialect='excel')
        csv_write.writerows(csv_table)
    


if __name__ == '__main__':
    jsonToCsv('json_db.json','csv_db.csv')