"""
168. Excel Sheet Column Title
Easy

1583

289

Add to List

Share
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution:
    def converttotitle(self, n: int) -> str:
        result = ''
        if n == 0:
            return result
        while n >= 26:
            if n % 26 > 0:
                result = chr(n % 26 + 64) + result
            else:
                result = 'Z' + result
                n -= 1
            n = n // 26
        if n > 0:
            result = chr(n % 26 + 64) + result
        return result


solution = Solution()
print(solution.converttotitle(676))
