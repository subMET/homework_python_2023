from Rectangle import Rectangle 

def test_rectangle():
    """
    >>> rectangle1 = Rectangle(1, 2)
    >>> rectangle2 = Rectangle(3)
    >>> print(rectangle1) 
    Rectangle(1, 2)
    >>> print(rectangle2)
    Rectangle(3, 3)
    >>> print(rectangle2 > rectangle1)
    True
    >>> print(rectangle2 - rectangle1)
    Rectangle(1.5, 1.5)
    >>> print(rectangle1 + rectangle2)
    Rectangle(3.0, 6.0)
    >>> rectangle3 = Rectangle(-1, 2)
    Traceback (most recent call last):
    ...
    ValueError: -1 меньше 0
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)