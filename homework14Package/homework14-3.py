from Rectangle import Rectangle
import pytest

rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3)

def test_string_view():
    assert str(Rectangle(1, 2)) == 'Rectangle(1, 2)'
    assert str(Rectangle(3)) == 'Rectangle(3, 3)'

def test_comparing():
    assert Rectangle(3) > Rectangle(1, 2)

def test_diff():
    assert Rectangle(3) - Rectangle(1, 2) == Rectangle(1.5, 1.5)

def test_sum():
    assert Rectangle(3) + Rectangle(1, 2) == Rectangle(4.5, 4.5)
    assert Rectangle(1, 2) + Rectangle(3) == Rectangle(3.0, 6.0)

def test_negative_length_error():
    with pytest.raises(ValueError):
        Rectangle(-1,2)

if __name__ == '__main__':
    pytest.main()
