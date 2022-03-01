INPUT = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
MAGIC_SQUARE = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]


def rotate_90_matrix(givenMatrix):
    rotatedMatrix = []
    for i in range(len(givenMatrix)):
        newRow = []
        for ii in range(len(givenMatrix)):
            newRow.append(givenMatrix[2 - ii][i])
        rotatedMatrix.append(newRow)
    return rotatedMatrix


def flipX(givenMatrix):
    rotatedMatrix = []
    for i in range(len(givenMatrix)):
        newRow = []
        for ii in range(len(givenMatrix)):
            newRow.append(givenMatrix[i][2 - ii])
        rotatedMatrix.append(newRow)
    return rotatedMatrix


minVal = 99
for i in range(4):
    for ii in range(2):

        sub2List = [
            elemIN - elemMGC
            for rowIN, rowMGC in zip(INPUT, MAGIC_SQUARE)
            for elemIN, elemMGC in zip(rowIN, rowMGC)
        ]
        absList = [abs(elem) for elem in sub2List]
        sumList = sum(absList)

        if sumList < minVal:
            minVal = sumList

        INPUT = flipX(INPUT)

    INPUT = rotate_90_matrix(INPUT)

print(minVal)
