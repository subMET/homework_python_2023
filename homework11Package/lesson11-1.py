from time import time

class MyStr(str):
    """Расширяет класс str, фиксируя время создания строки и добавляет возможность ввести имя автора строки."""

    def __new__(cls, text, author = None, *args,**kwargs):
        instance = str().__new__(cls, text,*args,**kwargs)
        instance.author = author
        instance.time = time()
        return instance

s = MyStr('lala', author = 'tester123')
print(s)
print(s.time)
print(s.author)
d = MyStr('lala')
print(d.time)
print(d.author)