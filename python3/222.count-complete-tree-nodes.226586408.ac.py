#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (42.38%)
# Likes:    1762
# Dislikes: 187
# Total Accepted:    196.2K
# Total Submissions: 462.4K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def get_height(root):
    height = 0
    while root:
        height += 1
        root = root.left
    return height

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if left_height != right_height:
            return 2**(right_height) + self.countNodes(root.left)
        else:
            return 2**(left_height) + self.countNodes(root.right)
# @lc code=end
