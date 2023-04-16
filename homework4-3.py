# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

sum = 0
turn = False
log = []
count = 0


def tax_for_rich():
    global sum
    global log
    if sum >= 5_000_000:
        tax = sum * 0.1
        sum -= tax
        log.append(f'Снятие налога на богатство: -{tax}. Текущая сумма: {sum}')


def deposit():
    global count
    global sum
    count += 1
    if count == 3:
        dep = sum * 0.03
        sum += dep
        count = 0
        global log
        log.append(f'Начисление процентов: +{dep}. Текущая сумма: {sum}')


def top_up(fill):
    global sum
    if fill % 50 != 0 or fill <= 0:
        print('Введена некорректная сумма')
    else:
        sum += fill
        print(f'Сумма пополнения: {fill}')
        global log
        log.append(f'Клиент пополнил счёт: +{fill}. Текущая сумма: {sum}')
        deposit()
    tax_for_rich()
    print(f'Текущая сумма на счету: {sum}')


def withdraw(loss):
    global sum
    if loss % 50 != 0 or loss <= 0:
        print('Введена некорректная сумма')
        return None
    else:
        tax = loss*0.015
        if tax < 30.0:
            tax = 30.0
        if tax > 600.0:
            tax = 600.0
        if sum >= loss + tax:
            sum -= loss + tax
            print(f'Сумма снятия: {loss}. Налоговый вычет: {tax}')
            global log
            log.append(f'Клиент снял со счёта: -{loss}. Налоговый вычет: -{tax}. Текущая сумма: {sum}')
            deposit()
        else:
            print(f'Недостаточно средств для снятия.')
    tax_for_rich()
    print(f'Текущая сумма на счету: {sum}')


def login():
    global turn
    if turn:
        turn = False
        print('Всего доброго. Приходите к нам ещё.')
    else:
        turn = True
        print('Добро пожаловать.')

top_up(1)
top_up(50)
withdraw(50)
top_up(50)
withdraw(50)
top_up(5000000)
withdraw(50000)
withdraw(50)
withdraw(50)
print(log)