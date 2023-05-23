import math
import csv
import json
from random import randint
from typing import Callable

def jsonLog(func: Callable, filename: str):
    def wrapper(*args,**kwargs):
        loginfo = {}
        result = func(*args,**kwargs)
        loginfo['arguments of function'] = [*args]
        for key, value in kwargs.items():
            loginfo[key] = value
        loginfo[f'Function result'] = result
        with open(filename, 'a') as jsonfile:
            json.dump(loginfo,jsonfile)
            jsonfile.write('\n')
        return result
    return wrapper

def csvSolveDecotator(filename):
    numberslist = []
    with open(filename,'r') as csvfile:
        for line in csvfile:
            buffer = line.split(',')
            stringnumbers = []
            for i in range(len(buffer)):
                stringnumbers.append(int(buffer[i]))
            numberslist.append(stringnumbers)
    def deco(func: Callable):
        def wrapper():
            resultslist = []
            for i in range(len(numberslist)):
                result = func(numberslist[i][0],numberslist[i][1],numberslist[i][2])
                resultslist.append(f'a = {numberslist[i][0]}, b = {numberslist[i][1]}, c = {numberslist[i][2]}, roots: {result}')
            return resultslist
        return wrapper
    return deco

def sqrRoots(a,b,c):
    if a == 0:
        return [c/b]
    D = b**2 - 4*a*c
    if D < 0:
        return []
    if D == 0:
        return [-b/(2*a)]
    return [(-b+math.sqrt(D))/(2*a),(-b-math.sqrt(D))/(2*a)]

def csvGenerate(strings, filename):
    with open(f'{filename}.csv','w',newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(strings):
            filewriter.writerow([randint(-100,100),randint(-100,100),randint(-100,100)])


# csvGenerate(100,'numbers')
# solvedlist = csvSolveDecotator('numbers.csv')(sqrRoots)()
# for i in range(len(solvedlist)):
#     print(solvedlist[i])
# jsonLog(sqrRoots,'logSqr.json')(a = 1, b = 1, c = -2)