"""172. Factorial Trailing Zeroes
Easy

1338

1415

Add to List

Share
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0"""


class Solution:
    def trailingzeroes(self, n: int) -> int:
        factorial = 1
        trailing_zeros = 0
        for x in range(1, n + 1):
            factorial = factorial * x
        while factorial > 9:
            remainder = factorial % 10
            factorial = factorial // 10
            if remainder == 0:
                trailing_zeros += 1
            else:
                return trailing_zeros
        return trailing_zeros


my_n = 0
solution = Solution()
print(solution.trailingzeroes(my_n))
#  Works but slow at scale