"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lcp_string = ""
        strs_min = min(strs)
        strs_max = max(strs)
        for x in range(len(strs_min)):
            if strs_min[x] == strs_max[x]:
                lcp_string += strs_min[x]
            else:
                break
        return lcp_string


my_string = ["dog", "racecar", "car"]
solution = Solution()
print(solution.longestCommonPrefix(my_string))
