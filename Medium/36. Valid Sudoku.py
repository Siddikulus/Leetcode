'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

import ast
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        l1= ast.literal_eval(board)

        # check if unique numbers in row
        for i in range(len(l1)):
            rowcheck = []
            for j in range(len(l1)):
                # print(l1[i][j], i, j, rowcheck)
                if l1[i][j] != '.' and l1[i][j] not in rowcheck:
                    rowcheck.append(l1[i][j])
                # print(check)
                elif l1[i][j] == '.':
                    continue
                else:
                    return False


        # check if unique numbers in column
        for i in range(len(l1)):
            columncheck = []
            for j in range(len(l1)):
                # print(l1[j][i], j, i, columncheck)
                if l1[j][i] != '.' and l1[j][i] not in columncheck:
                    columncheck.append(l1[j][i])
                # print(check)
                elif l1[j][i] == '.':
                    continue
                else:
                    return False


        #For each 3x3 matrix, divide total rows by 3 and divide total columns by 3.
        jmat = [0,3,6,9]
        for index1 in range(len(jmat)-1):
            matcheck = []
            for i in range(jmat[index1], jmat[index1+1]):
                for j in range(0, 3):
                    # print(l1[j][i], j, i, columncheck)
                    if l1[j][i] != '.' and l1[j][i] not in matcheck:
                        matcheck.append(l1[j][i])
                    # print(check)
                    elif l1[j][i] == '.':
                        continue
                    else:
                        return False

        jmat = [0, 3, 6, 9]
        for index1 in range(len(jmat) - 1):
            matcheck = []
            for i in range(jmat[index1], jmat[index1 + 1]):
                for j in range(3, 6):
                    # print(l1[j][i], j, i, columncheck)
                    if l1[j][i] != '.' and l1[j][i] not in matcheck:
                        matcheck.append(l1[j][i])
                    # print(check)
                    elif l1[j][i] == '.':
                        continue
                    else:
                        return False

        jmat = [0, 3, 6, 9]
        for index1 in range(len(jmat) - 1):
            matcheck = []
            for i in range(jmat[index1], jmat[index1 + 1]):
                for j in range(6, 9):
                    # print(l1[j][i], j, i, columncheck)
                    if l1[j][i] != '.' and l1[j][i] not in matcheck:
                        matcheck.append(l1[j][i])
                    # print(check)
                    elif l1[j][i] == '.':
                        continue
                    else:
                        return False
        return True

s1 = '''[[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]'''
print(Solution().isValidSudoku(s1))