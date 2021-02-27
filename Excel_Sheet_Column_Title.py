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
        place_holder = n
        if n == 0:
            return result
        while place_holder >= 26:
            if place_holder == 26:
                result = 'Z' + result
            else:
                result = chr(place_holder % 26 + 64) + result
            place_holder = place_holder // 26
                #  result += chr(place_holder - 26 + 90)  # if you're past Z then add a digit(letter)
        # result = chr(place_holder % 26 + 64) + result
        result += chr(place_holder % 26 + 64)
        return result


solution = Solution()
print(solution.converttotitle(701))
