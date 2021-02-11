class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        nums_sum = 0
        for num in nums:
            nums_sum += num
            if nums_sum > max_sum:
                max_sum = nums_sum
            if nums_sum < 0:
                nums_sum = 0
        return max_sum


my_nums = [8, -19, 5, -4, 20]
solution = Solution()
print((solution.maxSubArray(my_nums)))
