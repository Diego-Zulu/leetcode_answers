/*
 * @lc app=leetcode id=100 lang=java
 *
 * [100] Same Tree
 *
 * https://leetcode.com/problems/same-tree/description/
 *
 * algorithms
 * Easy (52.25%)
 * Likes:    1870
 * Dislikes: 56
 * Total Accepted:    519.1K
 * Total Submissions: 993.3K
 * Testcase Example:  '[1,2,3]\n[1,2,3]'
 *
 * Given two binary trees, write a function to check if they are the same or
 * not.
 * 
 * Two binary trees are considered the same if they are structurally identical
 * and the nodes have the same value.
 * 
 * Example 1:
 * 
 * 
 * Input:     1         1
 * ⁠         / \       / \
 * ⁠        2   3     2   3
 * 
 * ⁠       [1,2,3],   [1,2,3]
 * 
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:     1         1
 * ⁠         /           \
 * ⁠        2             2
 * 
 * ⁠       [1,2],     [1,null,2]
 * 
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * Input:     1         1
 * ⁠         / \       / \
 * ⁠        2   1     1   2
 * 
 * ⁠       [1,2,1],   [1,1,2]
 * 
 * Output: false
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        //SOLUCIÓN GERMÁN
        
        LinkedList<TreeNode> t1 = new LinkedList<TreeNode>();
        LinkedList<TreeNode> t2 = new LinkedList<TreeNode>();
                       
        t1.add(p);
        t2.add(q);
       
        while(!t1.isEmpty() && !t2.isEmpty()){
            TreeNode c1 = t1.remove();
            TreeNode c2 = t2.remove();
            if ((c1 == null && c2!= null) ||
                (c1 != null && c2== null)) {
                    return false;
            }
            if (c1 != null && c2!= null) {
                if (c1.val != c2.val) {
                    return false;
                }
                t1.add(c1.left);
                t1.add(c1.right);
                t2.add(c2.left);
                t2.add(c2.right);
            }
        }
        return t1.size() == t1.size();
    }
}
// @lc code=end
