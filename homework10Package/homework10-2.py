class User():

    def __init__(self, name, age, id, money = 0):
        self.name = name
        self.age = age
        self.id = id
        self.money = money


class CashMachine():

    def __init__(self, bank_name, address, current_cash):
        self.bank = bank_name
        self.address = address
        self.cash = current_cash
        self.users = []

    def bankomatInfo(self):
        print(f'Банкомат фирмы {self.bank}. Находится по адресу {self.address}. Наличных в банкомате: {self.cash}')

    def registration(self, name, age, money = 0):
        id = len(self.users)
        user = User(name, age, id, money)
        self.users.append(user)

    def userInfo(self, id):
        if id not in range(0, len(self.users)):
            print('Указанного id не существует.')
        else:
            print(f'id:{id}. Имя - {self.users[id].name}. Возраст - {self.users[id].age}. На счету - {self.users[id].money}')

    def collection(self, ammount, operation_type = 'Input'):
        if operation_type == 'Input':
            self.cash += ammount
        elif operation_type == 'Output':
            if self.cash >= ammount:
                self.cash -= ammount
            else:
                print('В банкомате нет столько наличных.')
        else:
            print('Неверный тип операции. Попробуйте ещё раз.')


    def deposit(self, id, ammount):
        if id not in range(0, len(self.users)):
            print('Указанного id не существует.')
        else:
            self.users[id].money += ammount
            self.cash += ammount

    def withdraw(self, id, ammount):
        if id not in range(0, len(self.users)):
            print('Указанного id не существует.')
        else:
            if self.users[id].money < ammount:
                print('Недостаточно денег на счету.')
            else:
                if self.cash < ammount:
                    print('Недостаточно денег в банкомате.')
                else:
                    self.cash -= ammount
                    self.users[id].money -= ammount


cashMachine1 = CashMachine('VTB','House 3', 10000)
cashMachine1.registration('Vasiliy', 19)
cashMachine1.registration('Peter', 54, 95000)
cashMachine1.deposit(0, 100)
cashMachine1.userInfo(0)
cashMachine1.bankomatInfo()
cashMachine1.withdraw(0, 1000)
cashMachine1.withdraw(0, 5)
cashMachine1.userInfo(0)
cashMachine1.bankomatInfo()
cashMachine1.withdraw(1, 50000)
cashMachine1.userInfo(1)
    

