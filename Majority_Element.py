"""169. Majority Element
Easy

5212

263

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1"""


class Solution:
    def majorityelement(self, nums: list[int]) -> int:
        unique = []
        nums_length = len(nums)
        unique = [x for x in nums if x not in unique and (unique.append(x) or True)]
        for num in unique:
            if nums.count(num) > nums_length / 2:
                return num


my_nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityelement(my_nums))
