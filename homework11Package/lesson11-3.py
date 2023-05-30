class Rectangle():
    """Создаёт объект прямоугольник. Имеет параметры длину и ширину. При сравнении рассматривается площадь."""

    def __init__(self: float, length: float, width=None):
        self.lenght = length
        self.width = width if width else length

    def perimetr(self):
        return 2 * (self.lenght + self.width)

    def square(self):
        return self.lenght * self.width

    def __add__(self, other):
        c = self.lenght/self.width
        res = (self.perimetr() + other.perimetr()) / 2
        width = res / (c + 1)
        length = res - width
        return Rectangle(length, width)
    
    def __sub__(self,other):
        c = self.lenght/self.width
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
        return f'Rectangle({self.lenght}, {self.width})'


rectangle1 = Rectangle(1, 2)
square1 = Rectangle(3)
print(square1 > rectangle1)
print(square1 - rectangle1)
