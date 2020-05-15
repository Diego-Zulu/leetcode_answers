/*
 * @lc app=leetcode id=543 lang=java
 *
 * [543] Diameter of Binary Tree
 *
 * https://leetcode.com/problems/diameter-of-binary-tree/description/
 *
 * algorithms
 * Easy (47.98%)
 * Likes:    2733
 * Dislikes: 176
 * Total Accepted:    308.1K
 * Total Submissions: 642K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 
 * Given a binary tree, you need to compute the length of the diameter of the
 * tree. The diameter of a binary tree is the length of the longest path
 * between any two nodes in a tree. This path may or may not pass through the
 * root.
 * 
 * 
 * 
 * Example:
 * Given a binary tree 
 * 
 * ⁠         1
 * ⁠        / \
 * ⁠       2   3
 * ⁠      / \     
 * ⁠     4   5    
 * 
 * 
 * 
 * Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
 * 
 * 
 * Note:
 * The length of path between two nodes is represented by the number of edges
 * between them.
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
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0; 
        int[] diameter = new int[1];
        diameterOfBinaryTreeAux(root, diameter);
        return diameter[0];
    }
    
    private int diameterOfBinaryTreeAux(TreeNode root, int[] diameter) {
        int leftHeight = 0;
        int rightHeight = 0;
        if (root.left != null) {
            leftHeight = diameterOfBinaryTreeAux(root.left, diameter);
        }
        if (root.right != null) {
            rightHeight = diameterOfBinaryTreeAux(root.right, diameter);
        }
        
        diameter[0] = leftHeight + rightHeight > diameter[0] ?
            leftHeight + rightHeight : diameter[0];
        
        return leftHeight > rightHeight ? leftHeight + 1 : rightHeight + 1;
    }
}
// @lc code=end
