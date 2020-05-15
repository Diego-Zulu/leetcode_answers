/*
 * @lc app=leetcode id=230 lang=java
 *
 * [230] Kth Smallest Element in a BST
 *
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
 *
 * algorithms
 * Medium (57.20%)
 * Likes:    2070
 * Dislikes: 56
 * Total Accepted:    334.8K
 * Total Submissions: 584.8K
 * Testcase Example:  '[3,1,4,null,2]\n1'
 *
 * Given a binary search tree, write a function kthSmallest to find the kth
 * smallest element in it.
 * 
 * Note: 
 * You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
 * 
 * Example 1:
 * 
 * 
 * Input: root = [3,1,4,null,2], k = 1
 * ⁠  3
 * ⁠ / \
 * ⁠1   4
 * ⁠ \
 * 2
 * Output: 1
 * 
 * Example 2:
 * 
 * 
 * Input: root = [5,3,6,2,4,null,null,1], k = 3
 * ⁠      5
 * ⁠     / \
 * ⁠    3   6
 * ⁠   / \
 * ⁠  2   4
 * ⁠ /
 * ⁠1
 * Output: 3
 * 
 * 
 * Follow up:
 * What if the BST is modified (insert/delete operations) often and you need to
 * find the kth smallest frequently? How would you optimize the kthSmallest
 * routine?
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *      int numberOfLeftSons;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        
        if (root == null){
            return -1;
        } 
        int[] resultAndK = {0, k};
        recursiveKthSmallest(root, resultAndK);
        return resultAndK[0];
    }
    
    private void recursiveKthSmallest(TreeNode actualNode, int[] resultAndK) {
        
        checkLeftSubTree(actualNode, resultAndK);
        checkActualNodeIfKthSmallest(actualNode, resultAndK);
        checkRightSubTree(actualNode, resultAndK);
    }
    
    private void checkLeftSubTree(TreeNode actualNode, int[] resultAndK) {
        
        if (actualNode.left != null && resultAndK[1] > 0) {
            
            recursiveKthSmallest(actualNode.left, resultAndK);
        }
    }
    
    private void checkActualNodeIfKthSmallest(TreeNode actualNode, int[] resultAndK) {
        
        resultAndK[1]--;
        if (resultAndK[1] == 0) {
            
            resultAndK[0] = actualNode.val;
            return;
        }
    }
    
    private void checkRightSubTree(TreeNode actualNode, int[] resultAndK) {
        
        if (actualNode.right != null && resultAndK[1] > 0) {
            
            recursiveKthSmallest(actualNode.right, resultAndK);
        }
    }
}
// @lc code=end
