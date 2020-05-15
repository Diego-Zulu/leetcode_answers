#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.75%)
# Likes:    4183
# Dislikes: 133
# Total Accepted:    285.5K
# Total Submissions: 652.3K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        curr_sum = 0
        count = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in sums:
                count += sums[curr_sum - k]
            sums[curr_sum] += 1
        return count

# @lc code=end
