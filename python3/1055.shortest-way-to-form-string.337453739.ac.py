#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#
# https://leetcode.com/problems/shortest-way-to-form-string/description/
#
# algorithms
# Medium (56.99%)
# Likes:    424
# Dislikes: 28
# Total Accepted:    28.4K
# Total Submissions: 49.8K
# Testcase Example:  '"abc"\n"abcbc"'
#
# From any string, we can form a subsequence of that string by deleting some
# number of characters (possibly no deletions).
# 
# Given two strings source and target, return the minimum number of
# subsequences of source such that their concatenation equals target. If the
# task is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
# subsequences of source "abc".
# 
# 
# Example 2:
# 
# 
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of
# source string due to the character "d" in target string.
# 
# 
# Example 3:
# 
# 
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" +
# "xz".
# 
# 
# Constraints:
# 
# 
# Both the source and target strings consist of only lowercase English letters
# from "a"-"z".
# The lengths of source and target string are between 1 and 1000.
# 
#

# @lc code=start
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourced_letters = set(source)
        next_letter = collections.deque()
        last_dict = {}
        for i in range(len(source)-1,-1,-1):
            c = source[i]
            new_dict = last_dict.copy()
            new_dict[c] = i
            next_letter.appendleft(new_dict)
            last_dict = new_dict
        way = 1
        source_pos = -1
        for t in target:
            if t not in sourced_letters:
                return -1
            next_pos = source_pos + 1
            if next_pos >= len(source):
                next_pos = 0
                way += 1
            source_pos = next_letter[next_pos].get(t, -1)
            if source_pos == -1:
                way += 1
                source_pos = next_letter[0][t]
        return way
# @lc code=end
