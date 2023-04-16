def create_dict(**kwargs):
    """Создаёт словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
    В случае, если несколько аргументов будут иметь одно и то же значение, 
    в словарь будет добавлен последний переданный аргумент."""
    res_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, set, dict)):
            res_dict[str(value)] = key
        else:
            res_dict[value] = key
    return res_dict


dict_1 = create_dict(a=1, b=2, c=[2, 2], d=2)
print(dict_1)
