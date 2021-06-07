"""3. Longest Substring Without Repeating Characters
Medium

14826

757

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        substring_length, start = 0, 0
        seen = {}
        for index, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            substring_length = max(substring_length, index - start + 1)
            seen[char] = index
        return substring_length


my_string = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(my_string))


