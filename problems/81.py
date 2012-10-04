#!/usr/bin/python

from time import sleep

def getMatrix():
    matrix = []
    #with open("../datafiles/problem81_example.txt") as f:
    with open("../datafiles/problem81_matrix.txt") as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                row = line.split(',')
                rowNum = [int(i.strip()) for i in row]
                matrix.append(rowNum)
    return matrix

def recurs(matrix, x, y):
    edge = len(matrix) - 1
    if x > edge: return -1
    if y > edge: return -1

    if x == edge and y == edge:
        return matrix[x][y]

    rightNum = recurs(matrix, x + 1, y)
    downNum = recurs(matrix, x, y + 1)
    if rightNum == -1 and downNum == -1:
        return -1

    if rightNum == -1:
        return matrix[x][y] + downNum
    elif downNum == -1:
        return matrix[x][y] + rightNum
    elif rightNum < downNum:
        return matrix[x][y] + rightNum
    else:
        return matrix[x][y] + downNum 

    
def prob81():
    matrix = getMatrix()

    answer = recurs(matrix, 0, 0)

    print("Sum: %s" % answer)


prob81()


