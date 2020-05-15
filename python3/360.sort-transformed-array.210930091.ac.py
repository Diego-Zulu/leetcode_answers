#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (48.32%)
# Likes:    314
# Dislikes: 95
# Total Accepted:    33.5K
# Total Submissions: 69.2K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# Given a sorted array of integers nums and integer values a, b and c. Apply a
# quadratic function of the form f(x) = ax^2 + bx + c to each element x in the
# array.
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]
# 
# 
# 
#

# @lc code=start
def apply(num, a, b, c):
    return a*num*num + b*num + c

def sortLinear(nums, len_nums, b, c):
    it = range(len_nums)
    transformed = []
    if b < 0:
        it = reversed(it)
    for i in it:
        transformed.append(nums[i])
    return transformed

def sortFromTheOutsides(nums, len_nums, a, b, c):
    low = 0
    high = len_nums - 1
    transformed = []
    while low <= high:
        transformed_low = nums[low]
        transformed_high = nums[high]
        if transformed_low < transformed_high:
            transformed.append(transformed_low)
            low += 1
        else:
            transformed.append(transformed_high)
            high -= 1
    return transformed

def sortFromMin(nums, len_nums, a, b, c):
    transformed = []
    min_y = nums[0]
    low = 0
    for i in range(1, len_nums):
        n_transformed = nums[i]
        if min_y >= n_transformed:
            min_y = n_transformed
            low = i
        else:
            break
    high = low + 1
    while low >= 0 and high < len(nums):
        transformed_low = nums[low]
        transformed_high = nums[high]
        if transformed_low < transformed_high:
            transformed.append(transformed_low)
            low -= 1
        else:
            transformed.append(transformed_high)
            high += 1
    for i in range(high, len(nums)):
        transformed.append(nums[i])
    for i in range(low, -1, -1):
        transformed.append(nums[i])
    return transformed
        

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if not nums: return []
        len_nums = len(nums)
        nums = list(map(lambda x: apply(x, a, b, c), nums))
        if a < 0: return sortFromTheOutsides(nums, len_nums, a, b, c)
        elif a > 0: return sortFromMin(nums, len_nums, a, b, c)
        else: return sortLinear(nums, len_nums, b, c)
# @lc code=end
