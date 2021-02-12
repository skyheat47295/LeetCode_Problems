"""
58. Length of Last Word
Easy

953

2978

Add to List

Share
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():
            return 0
        return len(s.split()[-1])


solution = Solution()
print(solution.lengthOfLastWord('         '))
