#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (33.64%)
# Likes:    3282
# Dislikes: 266
# Total Accepted:    343.6K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxPathSumAux(root, max_sum):
    
    if not root:
        return 0
    
    max_sum_left = maxPathSumAux(root.left, max_sum)
    max_sum_right = maxPathSumAux(root.right, max_sum)
    
    max_sum.val = max(max_sum.val, max_sum_left+max_sum_right+root.val, max_sum_left+root.val, max_sum_right+root.val, root.val)
    
    return max(max_sum_left + root.val, max_sum_right + root.val, root.val)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = TreeNode(-sys.maxsize-1)
        maxPathSumAux(root, max_sum)
        return max_sum.val
# @lc code=end
