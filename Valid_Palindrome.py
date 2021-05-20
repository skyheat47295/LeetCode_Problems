"""125. Valid Palindrome
Easy

2006

3852

Add to List

Share
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stripped = ''
        for char in s:
            if char.isalnum():
                s_stripped += char.lower()
        if s_stripped == s_stripped[::-1]:
            return True
        else:
            return False


my_string = "race a car"
solution = Solution()
print(solution.isPalindrome(my_string))
