#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (38.73%)
# Likes:    1961
# Dislikes: 3902
# Total Accepted:    548.5K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1, pos2, insert = m-1, n-1, n+m-1
        while pos1 >= 0 and pos2 >= 0:
            if nums1[pos1] > nums2[pos2]:
                nums1[insert] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[insert] = nums2[pos2]
                pos2 -= 1
            insert -= 1
        while pos2 >= 0:
            nums1[insert] = nums2[pos2]
            pos2 -= 1
            insert -= 1
        
# @lc code=end
