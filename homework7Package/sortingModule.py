import os

def sortingFiles(extensions):
    catalog = []
    dir_list = os.listdir()
    for obj in dir_list:
        if os.path.isfile(obj):
            catalog.append(obj)
    for item in extensions:
        if not os.path.exists(item):
            os.mkdir(item)
        for item2 in catalog:
            if item2.split('.')[1] == item:
                os.replace(item2, os.path.join(os.getcwd(),item,item2))


if __name__ == '__main__':
    sortingFiles(['rar','jar','png'])
