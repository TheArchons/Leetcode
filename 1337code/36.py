def isValidSudoku(board):
    subBox = []
    rows = []
    for i in range(9):
        subBox.append(set())
        rows.append(set())
    currBox = 0
    for rowPos, row in enumerate(board):
        rowSet = set()
        if rowPos <= 2:
            boxPos = 0
        elif rowPos <= 5:
            boxPos = 3
        else:
            boxPos = 6
        inBoxPos = 0
        for charPos, char in enumerate(row):
            inBoxPos += 1
            #print(charPos, inBoxPos)
            if charPos == 3 or charPos == 6:
                #inBoxPos = 1
                boxPos += 1
                #print(charPos)
            if char == '.':
                continue
            if char in rowSet:
                return False
            rowSet.add(char)
            if char in subBox[boxPos]:
                return False
            subBox[boxPos].add(char)
            if char in rows[charPos]:
                return False
            rows[charPos].add(char)

    return True

board = []
for i in range(9):
    row = input().strip('[]"').split('","')
    row[0] = row[0].strip('[]",')
    row[-1] = row[-1].strip('",[]')
    board.append(row)
print(isValidSudoku(board))