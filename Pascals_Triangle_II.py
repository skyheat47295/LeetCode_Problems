"""
119. Pascal's Triangle II
Easy

1249

220

Add to List

Share
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
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1] * (rowIndex + 1)
        prev_row = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            result[i] = prev_row[i - 1] + prev_row[i]
        return result


solution = Solution()
print(solution.getRow(5))
