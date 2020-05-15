#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.08%)
# Likes:    3037
# Dislikes: 1085
# Total Accepted:    348K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        len_nums = len(nums)
        descending_break = -1
        for i in reversed(range(len_nums-1)):
            if nums[i] < nums[i+1]:
                descending_break = i
                break
        if descending_break >= 0:
            changed = False
            for i in range(descending_break+1, len_nums):
                if nums[descending_break] >= nums[i]:
                    nums[descending_break], nums[i-1] = nums[i-1], nums[descending_break]
                    changed = True
                    break
            if not changed:
                nums[descending_break], nums[len_nums-1] =  nums[len_nums-1], nums[descending_break]
        left = descending_break+1
        right = len_nums-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
# @lc code=end
