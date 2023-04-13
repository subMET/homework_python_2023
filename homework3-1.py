original_list = [1,2,3,1,2,4,5,5,4,7,0,0]

list_set = set()
for i in range(len(original_list)):
    list_set.add(original_list[i])
result_list = []
for i in list_set:
    if original_list.count(i) > 1:
        result_list.append(i)
print(result_list)