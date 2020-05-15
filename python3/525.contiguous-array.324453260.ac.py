#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (40.05%)
# Likes:    1821
# Dislikes: 106
# Total Accepted:    125.4K
# Total Submissions: 313.1K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        save = {0: -1}
        count = 0
        max_l = 0
        for i, n in enumerate(nums):
            if n:
                count += 1
            else:
                count -= 1
            if count in save:
                max_l = max(max_l, i - save[count])
            else:
                save[count] = i
        return max_l
# @lc code=end
