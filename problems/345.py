import math
import sys
sys.path.append("../helpers")
from mathHelper import *

def loadMatrix():
    matrix = []
    with open("../datafiles/problem_345_example.txt") as f:
        for line in f:
            row = line.split()
            matrix.append(row)
    return matrix

def ColumnIsInList(colNumber, list):
    for p in list:
        if p[1] == colNumber:
            return True
    return False


def recurse(matrix, col, pointList, totalSoFar):
    if row == len(matrix): 
        return matrix[row][col] + totalSoFar

    if col == len(matrix):
        return matrix[row][col + 1] + totalSoFar

    totalSum = totalSoFar
    for i in range(col, len(matrix) - 1):
        totalSum += recurse(matrix, i, col + 1, pointList, totalSoFar)
        pointList.append((i, col))



    






problem345()

        






