"""
Add Binary
Easy

2493

325

Add to List

Share
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a), int(b)
        c = a+b
        e = str(c)
        while "2" in e:
            e = str(c)
            for i in range(len(e)):
                if e[-1-i] == "2":
                    c += 8*10**i
        return str(c)


my_a = '11'
my_b = '1'
solution = Solution()
print(solution.addBinary(my_a, my_b))
