import random
import time

def queensCrossing(i1,j1,i2,j2):
    if i1 == i2 or j1 == j2 or abs(i1-i2) == abs(j1-j2):
        return True
    return False


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()


def checkBoard(board):
    queens = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                queens.append([i,j])
    for i in range(len(queens)):
        for j in range(len(queens)):
            if i != j:
                if queensCrossing(queens[i][0],queens[i][1],queens[j][0],queens[j][1]):
                    return False
    return True


def checkCoordinateList(coordinates):
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                if queensCrossing(coordinates[i][0],coordinates[i][1],coordinates[j][0],coordinates[j][1]):
                    return False
    return True


def fillBoard(): # При заполнении досок этим методом, они слишком часто оказываются неподходящими.
    randomCoordinates = []
    i = 8
    while i > 0:
        a = [random.randint(1,8),random.randint(1,8)]
        if a not in randomCoordinates:
            randomCoordinates.append(a)
            i-= 1
    return randomCoordinates


def fillBoardMk2():
    randomCoordinates = []
    coord_1 = [1,2,3,4,5,6,7,8]
    coord_2 = [1,2,3,4,5,6,7,8]
    for i in range(8):
        a = [random.choice(coord_1),random.choice(coord_2)]
        coord_1.remove(a[0])
        coord_2.remove(a[1])
        # print(a)
        # print(coord_1)
        # print(coord_2)
        randomCoordinates.append(a)
    return randomCoordinates


def acceptablePlacement(j):
    variants = []
    count = 0
    while count < j:
        a = fillBoardMk2()
        if checkCoordinateList(a):
            variants.append(a)
            count += 1
    return variants


def coordinateListToBoard(coordinateList):
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)
    for i in range(len(coordinateList)):
        board[coordinateList[i][0] - 1][coordinateList[i][1] - 1] = 1
    return board


if __name__ == '__main__':
    coordinateList = [[1,3],[2,6],[3,4],[4,1],[5,8],[6,5],[7,7],[8,2]]
    print(coordinateList)
    print(checkCoordinateList(coordinateList))
    coordinateList = fillBoardMk2()
    print(coordinateList)
    print(checkCoordinateList(coordinateList))


    variants = acceptablePlacement(4)
    for i in range(len(variants)):
        print(variants[i])
        # print(checkCoordinateList(variants[i])) # Проверка расстоновки
        # printBoard(coordinateListToBoard(variants[i])) # Демонстрация досок



    # Другой вариант записи

    # board = [[0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0], \
    #         [0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0]]
    # printBoard(board)
    # print(checkBoard(board))
    # board = [[0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0], \
    #         [0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0]]
    # printBoard(board)
    # print(checkBoard(board))