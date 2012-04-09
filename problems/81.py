#!/usr/bin/python

from time import sleep

def getMatrix():
    matrix = []
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
    if x == edge and y == edge:
        return matrix[x][y]

    rightSum = -1 
    if x < edge:
        rightSum = matrix[x][y] + recurs(matrix, x + 1, y)

    downSum = -1
    if y < edge:
        downSum = matrix[x][y] + recurs(matrix, x, y + 1)

    if rightSum == -1 and downSum == -1:
        return matrix[x][y]
    elif downSum == -1:
        return rightSum
    elif rightSum == -1:
        return downSum
    elif rightSum < downSum:
        return rightSum
    else:
        return downSum
    
def prob81():
    matrix = getMatrix()

    answer = recurs(matrix, 0, 0)

    print("Sum: %s" % answer)


prob81()


