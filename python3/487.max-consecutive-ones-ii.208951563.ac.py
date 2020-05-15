#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (48.51%)
# Likes:    504
# Dislikes: 7
# Total Accepted:    34.4K
# Total Submissions: 70.9K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
# 
# 
# Example 1:
# 
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
# 
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
# 
#

# @lc code=start
from collections import deque

class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        zero_pos = deque([-1, -1, -1])
        max_ones = 0
        for i, n in filter(lambda x: x[1] == 0, enumerate(nums)):
            zero_pos.popleft()
            zero_pos.append(i)
            max_ones = max(max_ones, zero_pos[2] - zero_pos[0] - 1)
        zero_pos.popleft()
        zero_pos.append(len(nums))
        return max(max_ones, zero_pos[2] - zero_pos[0] - 1)
# @lc code=end
