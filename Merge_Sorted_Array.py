"""
88. Merge Sorted Array
Easy

3471

5070

Add to List

Share
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for count in range(n):
            nums1[m + count] = nums2[count]
        nums1.sort()
        return


my_nums1 = [1, 2, 3, 0, 0, 0]
my_m = 3
my_nums2 = [4, 5, 6]
my_n = 3
solution = Solution()
solution.merge(my_nums1, my_m, my_nums2, my_n)
print(my_nums1)
