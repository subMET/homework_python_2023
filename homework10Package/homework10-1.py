class Animal():

    def __init__(self, name, weight, age, type):
        self.name = name
        self.weight = weight
        self.age = age
        self.type = type

    def presentName(self):
        print(f'Познакомьтесь, это {self.type} по имени {self.name}.')

class Fish(Animal):

    def __init__(self, name, weight, age, body_length):
        Animal.__init__(self, name, weight, age, 'Fish')
        self.body_lenght = body_length

    def outputInfo(self):
        print(f'Рыбка {self.name}. Возраст {self.age}. Вес {self.weight} кг. Длина тела {self.body_lenght} см.')

class Bird(Animal):

    def __init__(self, name, weight, age, wingspan):
        Animal.__init__(self, name, weight, age, 'Bird')
        self.wingspan = wingspan

    def outputInfo(self):
        print(f'Птица {self.name}. Возраст {self.age}. Вес {self.weight} кг. Размах крыльев {self.wingspan} см.')

class Factory():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []

    def addAnimal(self, type, *args):
        if type == 'Fish':
            animal = Fish(*args)
        elif type == 'Bird':
            animal = Bird(*args)
        else:
            animal = Animal(*args)
        self.animals.append(animal)

    def getAnimal(self, position):
        if len(self.animals) < position:
            return None
        else:
            return self.animals[position - 1]



factory1 = Factory('Zoo','St.Saint 5')
factory1.addAnimal('Bird','Кеша', 1, 2, 30)
bird1 = factory1.getAnimal(1)
factory1.getAnimal(1).presentName()
bird1.outputInfo()
# fish1 = Fish('Долли', 2, 3, 25)
# fish1.presentName()
# fish1.outputInfo()