#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (46.18%)
# Likes:    2721
# Dislikes: 136
# Total Accepted:    300.9K
# Total Submissions: 651K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

LEFT = 0
RIGHT = 1
POSITIONS = [LEFT, RIGHT]

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        bfs = collections.deque([root])
        serial_builder = []
        while len(bfs) > 0:
            curr = bfs.popleft()
            if curr is not None:
                serial_builder.append(str(curr.val))
                bfs.append(curr.left)
                bfs.append(curr.right)
            serial_builder.append(',')
        while len(serial_builder) > 0 and serial_builder[-1] == ',':
            serial_builder.pop()
        return ''.join(reversed(serial_builder))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        deserial = data.split(',')
        root = TreeNode(-1)
        bfs = collections.deque([(root, RIGHT)])
        while len(deserial) > 0:
            curr_serial_val = deserial.pop()
            curr_parent, insert_pos = bfs.popleft()
            if curr_serial_val:
                curr_val = int(curr_serial_val)
                new_node = TreeNode(curr_val)
                if insert_pos == LEFT:
                    curr_parent.left = new_node
                else:
                    curr_parent.right = new_node
                for p in POSITIONS:
                    bfs.append((new_node, p))
        return root.right

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
