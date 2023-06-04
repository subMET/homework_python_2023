import csv
from random import randint


class ValidName():
    def __init__(self) -> None:
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value.istitle() and value.isalpha():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError('Неверный формат имени')


class RangeList():

    def __init__(self, min_value=None, max_value=None) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        for i in range(len(value)):
            for j in range(len(value[i])):
                if self.min_value is not None and value[i][j] < self.min_value:
                    raise ValueError(f'{value[i][j]} меньше {self.min_value}')
                if self.max_value is not None and value[i][j] > self.max_value:
                    raise ValueError(f'{value[i][j]} больше {self.max_value}')


class Student():
    first_name = ValidName()
    last_name = ValidName()
    surname = ValidName()
    score = RangeList(2, 5)
    test_score = RangeList(0, 100)

    def __init__(self, first_name, last_name, surname, filename):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        with open(filename, 'r', encoding='utf-8') as lessons:
            csv_file = csv.reader(lessons)
            buffer = []
            for line in csv_file:
                if line != []:
                    buffer.append(line)
        self._csv_lessons = set(buffer[0][0].split())

    @property
    def lessons(self):
        return self.lessons

    @lessons.setter
    def lessons(self, value):
        for item in value:
            if item not in self._csv_lessons:
                raise ValueError(f'{item} - Недопустимый предмет')
        self._lessons = value
        self.score = []
        self.test_score = []
        for i in range(len(self._lessons)):
            self.score.append([])
            self.test_score.append([])

    def setScore(self, lesson, value=None):
        cutted_list = self.score
        if value is None:
            value = randint(2, 5)
        cutted_list[lesson].append(value)
        self.score = cutted_list

    def setTestScore(self, lesson, value=None):
        cutted_list = self.test_score
        if value is None:
            value = randint(0, 100)
        cutted_list[lesson].append(value)
        self.test_score = cutted_list

    def avgScore(self):
        result = ''
        total = 0
        for i in range(len(self._lessons)):
            result += f'Предмет: {self._lessons[i]}. '
            avg = 0
            for j in range(len(self.score[i])):
                avg += self.score[i][j]
            avg /= len(self.score[i])
            total += avg
            result += f'Средняя оценка: {avg:.2f}. '
            avg = 0
            for j in range(len(self.test_score[i])):
                avg += self.test_score[i][j]
            avg /= len(self.test_score[i])
            result += f'Средняя оценка по тестам: {avg:.2f}.\n'
        total /= len(self._lessons)
        result += f'Средний балл по всем предметам: {total:.2f}.\n'
        return result




s1 = Student('Victor', 'Sidorov', 'Andreevich', 'lessons.csv')
# s1.lessons = ['Алгебра','Геометрия','Рус.Язык','Физкультура','Музыка'] # Тест ошибки 1
s1.lessons = ['Алгебра', 'Геометрия', 'Рус.Язык', 'Физкультура']
# s1.setScore(0,0) # Тест ошибки 2
# s1.setScore(0,6) # Тест ошибки 3
for i in range(4):
    s1.setScore(i)
    s1.setScore(i)
    s1.setScore(i,5)
    s1.setTestScore(i)
    s1.setTestScore(i,100)
print(s1.avgScore())
print(s1.__dict__)
