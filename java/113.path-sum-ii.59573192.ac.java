/*
 * @lc app=leetcode id=113 lang=java
 *
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (45.29%)
 * Likes:    1531
 * Dislikes: 55
 * Total Accepted:    312.8K
 * Total Submissions: 690K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given a binary tree and a sum, find all root-to-leaf paths where each path's
 * sum equals the given sum.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given the below binary tree and sum = 22,
 * 
 * 
 * ⁠     5
 * ⁠    / \
 * ⁠   4   8
 * ⁠  /   / \
 * ⁠ 11  13  4
 * ⁠/  \    / \
 * 7    2  5   1
 * 
 * 
 * Return:
 * 
 * 
 * [
 * ⁠  [5,4,11,2],
 * ⁠  [5,8,4,5]
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
 
class TreeNodeH {
      int val;
      TreeNode left;
      TreeNode right;
      int height;
      TreeNodeH(int x) {val = x; height = 0;}
      TreeNodeH(TreeNode x, int y) { val = x.val; height = y; left = x.left;
            right = x.right;}
 }
 
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        Stack<TreeNodeH> dfs = new Stack<>();
        List<List<Integer>> result = new ArrayList<>();
        List<TreeNodeH> actualPath = new ArrayList<>();
        if (root == null) return result;
        int totalSum = 0;
        dfs.push(new TreeNodeH(root, 0));
        
        while (!dfs.isEmpty()) {
            
            TreeNodeH actualNode = dfs.pop();
            
            while (!actualPath.isEmpty() && actualPath.get(actualPath.size()-1).height + 1 != actualNode.height) {
                
                TreeNodeH aux = actualPath.remove(actualPath.size()-1);
                totalSum-=aux.val;
            }
            if (actualNode.val + totalSum == sum && actualNode.left == null && actualNode.right == null) {
                int index = actualPath.size();
                actualPath.add(actualNode);
                List<Integer> actualPathClone = new ArrayList<>();
                for (int i=0; i<actualPath.size(); i++) {
                    actualPathClone.add(actualPath.get(i).val);
                }
                result.add(actualPathClone);
                actualPath.remove(index);
            } else {
                
                actualPath.add(actualNode);
                totalSum += actualNode.val;
                if (actualNode.right != null) {
                    dfs.push(new TreeNodeH(actualNode.right, actualNode.height+1));
                }
                if (actualNode.left != null) {
                    dfs.push(new TreeNodeH(actualNode.left, actualNode.height+1));
                }
            } 
        }
        
        return result;
    }
}
// @lc code=end
