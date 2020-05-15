#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (30.99%)
# Likes:    827
# Dislikes: 30
# Total Accepted:    29.9K
# Total Submissions: 96.4K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B. 
# 
# Example 1:
# 
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# 
# 
# Note:
# 
# 2 .
# 0 .
# 1 .
# 
# 
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        low = 0
        high = nums[n-1] - nums[0]
        while low < high:
            mid = int((low + high) / 2)
            left, count = 0, 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low
            
# @lc code=end
