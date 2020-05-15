/*
 * @lc app=leetcode id=102 lang=java
 *
 * [102] Binary Tree Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (53.24%)
 * Likes:    2645
 * Dislikes: 65
 * Total Accepted:    571.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, return the level order traversal of its nodes' values.
 * (ie, from left to right, level by level).
 * 
 * 
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 
 * return its level order traversal as:
 * 
 * [
 * ⁠ [3],
 * ⁠ [9,20],
 * ⁠ [15,7]
 * ]
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> result = new LinkedList<>();
        Queue<TreeNode> bfs = new LinkedList<>();
        Queue<Integer> height = new LinkedList<>();
        bfs.add(root);
        height.add(0);
        
        LinkedList<Integer> current = new LinkedList<>();
        
        while (bfs.peek() != null) {
            
            TreeNode actualNode = bfs.remove();
            Integer actualHeight = height.remove();
            Integer nextHeight = height.peek();
            current.add(actualNode.val);
            
            if (nextHeight == null) {
                result.add(new LinkedList<>(current));
                current.clear();
            } else {
                if (actualHeight != nextHeight) {
                    
                    result.add(new LinkedList<>(current));
                    current.clear();
                }
            }
            
            if (actualNode.left != null) {
                bfs.add(actualNode.left);
                height.add(actualHeight+1);
            }
            
            if (actualNode.right != null) {
                bfs.add(actualNode.right);
                height.add(actualHeight+1);
            }
            
        }
        
        return result;
    }
}
// @lc code=end
