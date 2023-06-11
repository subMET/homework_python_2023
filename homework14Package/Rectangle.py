class Valid():

    def __init__(self, min_value = None, max_value = None) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self,owner,name):
        self.param_name = '_' + name

    def __get__(self,instance,owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance,self.param_name,value)
    
    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} меньше {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} больше {self.max_value}')

    

class Rectangle():
    """Создаёт объект прямоугольник. Имеет параметры длину и ширину. При сравнении рассматривается площадь."""
    _width = Valid(0)
    _lenght = Valid(0)

    def __init__(self: float, length: float, width=None):
        self._lenght = length
        self._width = width if width else length
        
    def perimetr(self):
        return 2 * (self._lenght + self._width)

    def square(self):
        return self._lenght * self._width

    def __add__(self, other):
        c = self._lenght/self._width
        res = (self.perimetr() + other.perimetr()) / 2
        width = res / (c + 1)
        length = res - width
        return Rectangle(length, width)
    
    def __sub__(self,other):
        c = self._lenght/self._width
        res = (self.perimetr() - other.perimetr()) / 2
        if res <= 0:
            return Rectangle(0, 0)
        width = res / (c + 1)
        length = res - width
        return Rectangle(length, width)
    
    def __eq__(self, other) -> bool:
        return self.square() == other.square()
    
    def __ne__(self, other) -> bool:
        return self.square() != other.square()
    
    def __gt__(self, other) -> bool:
        return self.square() > other.square()
    
    def __ge__(self, other) -> bool:
        return self.square() <= other.square()
    
    def __lt__(self, other) -> bool:
        return self.square() < other.square()
    
    def __le__(self, other) -> bool:
        return self.square() >= other.square()
    
    def __str__(self):
        return f'Rectangle({self._lenght}, {self._width})'
    
