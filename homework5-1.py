path = f"C:\\Users\\User\\Desktop\\picture.png "

def pathTuple(path):
    path_list = path.split("\\")
    file_split = (path_list.pop()).split('.')
    c = file_split.pop()
    b = file_split.pop(0)
    for i in range(len(file_split)):
        b = '.'.join([b,file_split.pop(0)])
    a = path_list.pop(0)
    for i in range(len(path_list)):
        a = '\\'.join([a,path_list.pop(0)])
    return (a,b,c)

print(pathTuple(path))