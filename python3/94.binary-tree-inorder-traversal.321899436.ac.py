#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (61.91%)
# Likes:    2778
# Dislikes: 119
# Total Accepted:    687.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_leaf(c):
    return c.left is None and c.right is None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        dfs = [root]
        res = []
        while dfs:
            curr = dfs.pop()
            if not curr:
                continue
            if isinstance(curr, int):
                res.append(curr)
                continue
            dfs.append(curr.right)
            dfs.append(curr.val)
            dfs.append(curr.left)
        return res
        
# @lc code=end
