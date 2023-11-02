'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        zero_row = [1]
        all_rows = []
        all_rows.append(zero_row[:])
        for row in range(1, rowIndex+1):
            zero_row.append(0)
            zero_row.insert(0, 0)
            new_row = []
            for index in range(len(zero_row) - 1):
                new_row.append(zero_row[index] + zero_row[index + 1])
            # print(zero_row, new_row, len(zero_row)-1)
            all_rows.append(new_row)
            zero_row[:] = new_row
        return all_rows[rowIndex]

print(Solution().getRow(3))
