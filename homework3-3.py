assortment = {
    'Supply': 7,
    'Spare clothes': 6,
    'Aid kit': 3,
    'Tent': 2,
    'Dishes': 2,
    'Snack': 2,
    'Boots': 1,
    'Flashlight': 1,
    'Kindling': 1
}

carrying_weight = 4
min_weight = carrying_weight + 1
for i in assortment.keys():
    if assortment.get(i) < min_weight:
        min_weight = assortment.get(i)

backpacks = []
var_number = 0
i = 0
ext_pos = -1
ext_pos_set = False
keys = []
for i in assortment.keys():
    keys.append(i)
kl = len(keys)
space = carrying_weight
i = 0
j = 1

while i in range(kl):
    if len(backpacks) < var_number + 1:
        backpacks.append([f'Номер рюкзака: {var_number + 1}'])
    if assortment.get(keys[i]) <= space:
        backpacks[var_number].append(keys[i])
        space = space - assortment.get(keys[i])
    else:
        # print(f'{i = },{j = }, {var_number = }, \n {backpacks[var_number]}')
        if i == kl - 1:
            if ext_pos == 0 and j == 0:
                print('break')
                break
            backpacks.append(backpacks[var_number].copy())
            var_number += 1
            backpacks[var_number][0] = f'Номер рюкзака: {var_number + 1}'
            i = keys.index(backpacks[var_number].pop())
            space = space + assortment.get(keys[i])
            if not ext_pos_set:
                ext_pos = len(backpacks[var_number]) - 1
                ext_pos_set = True
            if i == kl - 1 and ext_pos != 0:
                j = len(backpacks[var_number]) - 1
                while j > ext_pos - 1 and i == kl - 1:
                    i = keys.index(backpacks[var_number].pop())
                    space = space + assortment.get(keys[i])
                    j -= 1
                if j == ext_pos:
                    ext_pos -= 1
        # print(f'{i = },{j = }, {var_number = }, \n {backpacks[var_number]}')
        i += 1
        # if i == kl:
        #     i-= 1
        #     print(i)
backpacks.pop()

for i in range(len(backpacks)):
    print(backpacks[i])