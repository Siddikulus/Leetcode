'''
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.



Example 1:


Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
Example 2:

Input: wall = [[1],[1],[1]]
Output: 3


Constraints:

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1
'''


class Solution:
    #Brute Force approach

    # def leastBricks(self, wall: list[list[int]]) -> int:
    #     #Take a random value that acts as the minimum
    #     min_crossed = len(wall)
    #
    #     #Store the total width of the wall in a variable
    #     totalwidth = sum(wall[0])
    #
    #     minrowbricks = max([len(row) for row in wall])
    #
    #     if totalwidth > 1 and minrowbricks > 1:
    #         #For each unit width in the total width
    #         for width in range(1, totalwidth):
    #             count = 0
    #             #For each row of bricks
    #             for row_index in range(len(wall)):
    #                 #Take count that is to decide the number of bricks touched
    #                 #Take sum_rows, iterate over each row, if the sum from left to right matches the width, then continue, else count+1
    #                 sum_rows = 0
    #
    #                 for brick in wall[row_index]:
    #                     sum_rows += brick
    #                     if sum_rows == width:
    #                         break
    #
    #                 if sum_rows != width and min_crossed >= count:
    #                     count += 1
    #
    #             # print(width, count, min_crossed)
    #             if min_crossed >= count:
    #                 min_crossed = count
    #     return min_crossed

    #Count Gaps approach
    def leastBricks(self, wall: list[list[int]]) -> int:
        countGap = { 0 : 0 }

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())

print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
