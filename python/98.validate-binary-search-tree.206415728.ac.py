#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.39%)
# Likes:    3470
# Dislikes: 497
# Total Accepted:    645.1K
# Total Submissions: 2.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
#

# @lc code=start
def check_bst_with_dfs(root, min_val, max_val):
    if not root:
        return True
    if root.val >= max_val or root.val <= min_val:
        return False
    return check_bst_with_dfs(root.left, min_val, root.val) and \
        check_bst_with_dfs(root.right, root.val, max_val)

class Solution(object):
    def isValidBST(self, root):
        return check_bst_with_dfs(root, -sys.maxsize, sys.maxsize)
# @lc code=end
