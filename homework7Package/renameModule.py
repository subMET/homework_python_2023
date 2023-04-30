import os

def renameFiles(ext_c, ext_r, newName = '', nums = 3, letters = None):
    catalog = []
    dir_list = os.listdir()
    count = 1
    count_string = ''
    for obj in dir_list:
        if os.path.isfile(obj):
            catalog.append(obj)
    for item in catalog:
        if item.split('.')[1] == ext_c:
            name = ''
            if letters != None:
                if letters[0] <= len(item.split('.')[0]):
                    j = letters[0] - 1
                    while j < letters[1] and j < len(item.split('.')[0]):
                        name += item.split('.')[0][j]
                        j+= 1
            count_string = str(count)
            while len(count_string) < nums:
                count_string = '0' + count_string
            name = name + newName + count_string + '.' + ext_r
            count = count + 1
            os.rename(item, name)



if __name__ == '__main__':
    renameFiles(newName = 'picture', ext_c = 'png', ext_r = 'jpg')
