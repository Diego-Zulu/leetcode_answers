/*
 * @lc app=leetcode id=101 lang=java
 *
 * [101] Symmetric Tree
 *
 * https://leetcode.com/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (46.15%)
 * Likes:    3687
 * Dislikes: 87
 * Total Accepted:    608K
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric
 * around its center).
 * 
 * For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
 * 
 * 
 * ⁠   1
 * ⁠  / \
 * ⁠ 2   2
 * ⁠/ \ / \
 * 3  4 4  3
 * 
 * 
 * 
 * 
 * But the following [1,2,2,null,3,null,3] is not:
 * 
 * 
 * ⁠   1
 * ⁠  / \
 * ⁠ 2   2
 * ⁠  \   \
 * ⁠  3    3
 * 
 * 
 * 
 * 
 * Follow up: Solve it both recursively and iteratively.
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
class Solution {
    public boolean isSymmetric(TreeNode root) {
        
        Queue<TreeNode> bfs = new LinkedList<>();
        bfs.add(root);
        bfs.add(root);
        
        while (!bfs.isEmpty()) {
            
            TreeNode t1 = bfs.poll();
            TreeNode t2 = bfs.poll();
            
            if (t1 == null && t2 == null) continue;
            else if (t1 == null || t2 == null || t1.val != t2.val) return false;
            
            bfs.add(t1.left);
            bfs.add(t2.right);
            bfs.add(t1.right);
            bfs.add(t2.left);
        }
        
        return true;
    }
}
// @lc code=end
