#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (55.43%)
# Likes:    3207
# Dislikes: 168
# Total Accepted:    644.1K
# Total Submissions: 1.2M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
LETTERS = ord('z') - ord('a') + 1

def get_anagram(s):
    ana = [0] * LETTERS
    for c in s:
        ana[ord(c) - ord('a')] += 1
    return ana

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            ana = str(sorted(s))
            anagrams[ana].append(s)
        return list(anagrams.values())
# @lc code=end
