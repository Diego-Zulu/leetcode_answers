#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (47.06%)
# Likes:    2942
# Dislikes: 85
# Total Accepted:    333.7K
# Total Submissions: 708.5K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.p_idx = 0
        self.total_inorder_pos = {v: i for i, v in enumerate(inorder)}
        return self._buildTreeRec(0, len(inorder))
    
    def _buildTreeRec(self, left_in, right_in):
        if left_in == right_in:
            return None
        root = TreeNode(self.preorder[self.p_idx])
        i_idx = self.total_inorder_pos[root.val]
        self.p_idx += 1
        root.left = self._buildTreeRec(left_in, i_idx)
        root.right = self._buildTreeRec(i_idx + 1, right_in)
        return root
    
# @lc code=end
