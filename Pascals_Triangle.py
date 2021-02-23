"""
118. Pascal's Triangle
Easy

2236

130

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = self.generate(numRows - 1)
        return result + [[1] + [result[-1][i - 1] + result[-1][i] for i in range(1, numRows - 1)] + [1]]


solution = Solution()
print(solution.generate(5))
