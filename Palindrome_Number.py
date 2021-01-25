"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        my_palindrome = 0
        temp_x = x

        while temp_x > 0:
            my_palindrome = my_palindrome * 10 + temp_x % 10
            temp_x //= 10
        if x == my_palindrome:
            return True
        else:
            return False


my_number = int(input('Gimme a number :'))
solution = Solution()
if solution.isPalindrome(my_number):
    print('yep, its a palindrome')
else:
    print('nope not a palindrome')
