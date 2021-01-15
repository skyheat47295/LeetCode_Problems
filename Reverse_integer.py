class Solution(object):
    def __init__(self, x):
        self.x = x

    def reverse(self, x):
        self.x = x
        """
        :type x: int
        :rtype: int
        """
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
my_solution = Solution
my_solution.reverse(my_number)
print(my_solution)
