"""
53. Maximum Subarray
Easy

10705

514

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
"""


class Solution:
    @staticmethod
    def maxSubArray(nums: list[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum += num
            max_sum = max(current_sum, max_sum, num)
            current_sum = max(current_sum, num)
        return max_sum


# my_nums = [-2, -6, -2, -13, -4]
my_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# my_nums = [8, -19, 5, -4, 20]
solution = Solution()
print((solution.maxSubArray(my_nums)))
