#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.97%)
# Likes:    7261
# Dislikes: 332
# Total Accepted:    961.4K
# Total Submissions: 2.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = 0
        max_sub_sum = -sys.maxsize
        for n in nums:
            sub_sum += n
            max_sub_sum = max(max_sub_sum, sub_sum)
            sub_sum = max(sub_sum, 0)
        return max_sub_sum
        
# @lc code=end
