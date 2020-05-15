/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
 *
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (36.94%)
 * Likes:    1218
 * Dislikes: 647
 * Total Accepted:    393.3K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, find its minimum depth.
 * 
 * The minimum depth is the number of nodes along the shortest path from the
 * root node down to the nearest leaf node.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * return its minimum depth = 2.
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
    public int minDepth(TreeNode root) {
        
       return recursiveMinDepth(root);
    }
    
    private int recursiveMinDepth(TreeNode t) {
        
        if (t==null) return 0;
        
        int ld = recursiveMinDepth(t.left);
        int rd = recursiveMinDepth(t.right);
        
        if (rd == 0) return 1+ld;
        
        if(ld == 0) return 1+rd;
        
       return 1+Math.min(ld,rd);
    }
}
// @lc code=end
