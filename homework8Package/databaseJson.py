import json


def updateDatabase(database):
    working_dict: dict[int: dict[int:str]] = {}
    with open(database,'r',encoding='utf-8') as db:
        reserved = set()
        try:
            working_dict = json.load(db)
            for level in working_dict:
                for uid in level:
                    reserved.add(uid)
        except:
            pass
    while True:
        name = input('Имя: ')
        if name == '':
            return
        id = -1
        while id <= 0 or id in reserved:  
            id = int(input('id: '))
        reserved.add(id)
        access = 0
        while not access in range(1,8):
            access = int(input('Доступ: '))
        if working_dict.get(access):
            working_dict.get(access).update({id:name})
        else:
            working_dict[access] = {id:name}
        with open(database,'w+',encoding='utf-8') as db:
            json.dump(working_dict,db)



if __name__ == '__main__':
    updateDatabase('json_db.json')
