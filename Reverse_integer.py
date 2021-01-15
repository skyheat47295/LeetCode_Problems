"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
"""


def reverse(x):
    if not (-2 ** 31 <= x <= 2 ** 31 - 1):
        return 0
    else:
        my_string = str(x)
    if x >= 0:
        my_string_reversed = my_string[::-1]
    else:
        temp = my_string[1:]
        temp2 = temp[::-1]
        my_string_reversed = "-" + temp2
    if not (-2 ** 31 <= int(my_string_reversed) <= 2 ** 31 - 1):
        return 0
    else:
        return int(my_string_reversed)


my_number = int(input('Integer'))
print(reverse(my_number))
