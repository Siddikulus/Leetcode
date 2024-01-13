'''
On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.

You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.

Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.



Example 1:


Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
Example 2:


Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]
Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).


Constraints:

1 <= queens.length < 64
queens[i].length == king.length == 2
0 <= xQueeni, yQueeni, xKing, yKing < 8
All the given positions are unique.
'''


class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        l = []
        # to traverse in straight left of king's position
        for i in range(king[1], -1, -1):
            if [king[0], i] in queens:
                l.append([king[0], i])
                break
        # to traverse in straight right of king's position
        for i in range(king[1], 8, 1):
            if [king[0], i] in queens:
                l.append([king[0], i])
                break
        # to traverse staright above king's position
        for i in range(king[0], -1, -1):
            if [i, king[1]] in queens:
                l.append([i, king[1]])
                break
        # to traverse straight down king's position
        for i in range(king[0], 8, 1):
            if [i, king[1]] in queens:
                l.append([i, king[1]])
                break

        # to traverse diagonally right down from king's position
        for i in range(1, 8):
            if [king[0] + i, king[1] + i] in queens:
                l.append([king[0] + i, king[1] + i])
                break
            if king[0] + i > 7 or king[1] + i > 7:
                break
        # to traverse diagonally left up from king's position
        for i in range(1, 8):
            if [king[0] - i, king[1] - i] in queens:
                l.append([king[0] - i, king[1] - i])
                break
            if king[0] - i < 0 or king[1] - i < 0:
                break
        # to traverse diagonally right up from king's position
        for i in range(1, 8):
            if [king[0] - i, king[1] + i] in queens:
                l.append([king[0] - i, king[1] + i])
                break
            if king[0] - i < 0 or king[1] + i > 7:
                break
        # to traverse diagonally left down from king's position
        for i in range(1, 8):
            if [king[0] + i, king[1] - i] in queens:
                l.append([king[0] + i, king[1] - i])
                break
            if king[0] + i > 7 or king[1] - i < 0:
                break

                # below code is performed to remove duplicates and then return
        ans = []
        for i in l:
            if i not in ans:
                ans.append(i)
        return ans
    
print(Solution().queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
