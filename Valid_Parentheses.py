"""
20. Valid Parentheses
Easy

6653

269

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        my_stack = []
        open_paren = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in open_paren.keys():
                my_stack.append(char)
            elif my_stack:  # if there is no stack then you have a close without an open
                if open_paren[my_stack[-1]] == char:
                    my_stack.pop()
                else:
                    return False
            else:
                return False
        return my_stack == []


my_input = ")(){}"
solution = Solution()
print(solution.isValid(my_input))
