class Archive():
    """Создаёт объект: пара число и строка. При создании новых объектов, числа и строки предыдущего помещаются
    в соответсвующие списки-архивы."""
    str_list = []
    int_list = []
    buff_str = None
    buff_int = None

    def __init__(self, a: int, s: str):
        self.num = a
        self.text = s
        if Archive.buff_int != None:
            Archive.int_list.append(Archive.buff_int)
        if Archive.buff_str != None:
            Archive.str_list.append(Archive.buff_str)
        Archive.buff_int = a
        Archive.buff_str = s

    def __str__(self) -> str:
        return f'{self.num}:{self.text}'
    
    def __repr__(self) -> str:
        return f'{self.num} {self.text}'
        

a = Archive(1,'a')
print(Archive.int_list)
print(Archive.str_list)
b = Archive(2,'b')
print(Archive.int_list)
print(Archive.str_list)
c = Archive(3,'c')
print(Archive.int_list)
print(Archive.str_list)