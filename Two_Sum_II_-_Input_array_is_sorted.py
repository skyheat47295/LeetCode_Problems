"""167. Two Sum II - Input array is sorted
Easy

2714

737

Add to List

Share
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution."""


class Solution:
    def twosum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1
        while numbers[start] <= target:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1


my_numbers = [2, 7, 11, 15]
my_target = 9
solution = Solution()
print(solution.twosum(my_numbers, my_target))
#  This solution worked, but timed out. Let's make it more efficient.
