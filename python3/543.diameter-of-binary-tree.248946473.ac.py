#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (47.98%)
# Likes:    2733
# Dislikes: 176
# Total Accepted:    308.1K
# Total Submissions: 642K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def diameterOfBinaryTreeAux(root, result):
    if root is None:
        return 0
    left_path = 1 + diameterOfBinaryTreeAux(root.left, result)
    right_path = 1 + diameterOfBinaryTreeAux(root.right, result)
    result[0] = max(result[0], left_path + right_path - 2)
    return max(left_path, right_path)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = [0]
        diameterOfBinaryTreeAux(root, result)
        return result.pop()
# @lc code=end
