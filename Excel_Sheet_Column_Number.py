"""
171. Excel Sheet Column Number
Easy

1559

190

Add to List

Share
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution:
    def titletonumber(self, s: str) -> int:
        result = 0
        for x in range(len(s)):
            result += 26 ** (len(s) - x - 1) * (ord(s[x]) - 64)
        return result


solution = Solution()
print(solution.titletonumber('AF'))
