#
# @lc app=leetcode id=270 lang=python
#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (46.99%)
# Likes:    659
# Dislikes: 52
# Total Accepted:    125.5K
# Total Submissions: 266.7K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: 4
# 
# 
#

# @lc code=start
class Solution(object):
    def closestValue(self, root, target):
        closest = (-1, sys.maxsize)
        while root:
            if closest[1] > abs(root.val - target):
                closest = (root.val, abs(root.val - target))
            root = root.left if root.val > target else root.right
        return closest[0]
# @lc code=end
