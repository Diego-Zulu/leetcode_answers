#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (53.66%)
# Likes:    3347
# Dislikes: 232
# Total Accepted:    584.5K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            insert = low - 1
            selected_pivot = random.randint(low, high)
            nums[high], nums[selected_pivot] = nums[selected_pivot], nums[high]
            pivot = nums[high]
            for i in range(low, high):
                if nums[i] >= pivot:
                    insert += 1
                    nums[i], nums[insert] = nums[insert], nums[i]
            insert += 1
            nums[high], nums[insert] = nums[insert], nums[high]
            if k-1 < insert:
                high = insert - 1
            elif k-1 > insert:
                low = insert + 1
            else:
                return nums[insert]
        return nums[low]
# @lc code=end
