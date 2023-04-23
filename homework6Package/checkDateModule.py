from sys import argv


_monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}


def _leapYear(year):
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True
    return False


def checkDateFromat(date):
    check = False
    splited_date = date.split('.')
    if len(splited_date) == 3:
        if len(splited_date[0]) == 2 and len(splited_date[1]) == 2 and len(splited_date[2]) == 4:
            check = True
    if not check:
        return check
    try:
        a = int(splited_date[0])
        b = int(splited_date[1])
        c = int(splited_date[2])
        if a > 0 and b > 0 and c > 0:
            return True
        else:
            return False
    except:
        return False


def checkDate(date):
    if checkDateFromat(date) is False:
        return False
    splited_date = date.split('.')
    day = int(splited_date[0])
    month = int(splited_date[1])
    year = int(splited_date[2])
    if year not in range(1,10000):
        return False
    if month not in range(1,13):
        return False
    if day not in range(1, _monthDict.get(month) + 1):
        if day == 29 and _leapYear(year) and month == 2:
            return True
        else:
            return False
    return True

def checkDateTerminal():
    if len(argv) < 2:
        return 'Вызовите функцию с датой'
    return checkDate(argv[1])

if __name__ == '__main__':
    print(checkDateTerminal())
    # a = '11.12.0000'
    # print(a, checkDate(a))
    # a = '29.02.2000'
    # print(a, checkDate(a))
    # a = '29.02.2001'
    # print(a, checkDate(a))
    # a = '31.03.1999'
    # print(a, checkDate(a))
    # a = 'dsadasd'
    # print(a, checkDate(a))