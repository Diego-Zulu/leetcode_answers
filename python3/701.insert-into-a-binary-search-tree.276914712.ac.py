#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (79.25%)
# Likes:    735
# Dislikes: 68
# Total Accepted:    97.6K
# Total Submissions: 123.3K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree will be between 0 and 10^4.
# Each node will have a unique integer value from 0 to -10^8, inclusive.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.
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

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        inserted = False
        while not inserted:
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                    inserted = True
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    inserted = True
                node = node.right
            
        return root
# @lc code=end
