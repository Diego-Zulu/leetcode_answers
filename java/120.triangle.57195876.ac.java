/*
 * @lc app=leetcode id=120 lang=java
 *
 * [120] Triangle
 *
 * https://leetcode.com/problems/triangle/description/
 *
 * algorithms
 * Medium (43.08%)
 * Likes:    1771
 * Dislikes: 212
 * Total Accepted:    235.8K
 * Total Submissions: 546.9K
 * Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
 *
 * Given a triangle, find the minimum path sum from top to bottom. Each step
 * you may move to adjacent numbers on the row below.
 * 
 * For example, given the following triangle
 * 
 * 
 * [
 * ⁠    [2],
 * ⁠   [3,4],
 * ⁠  [6,5,7],
 * ⁠ [4,1,8,3]
 * ]
 * 
 * 
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 * 
 * Note:
 * 
 * Bonus point if you are able to do this using only O(n) extra space, where n
 * is the total number of rows in the triangle.
 * 
 */

// @lc code=start
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int i = 0;
        int[] sum = new int[n];
        
        while (i < n) {
         List<Integer> l = triangle.get(i);
         int s = l.size();
         for (int j=s-1; j > -1; j--){
             if (j == 0)
             sum[j]+=l.get(j);
             else if (j == s-1)
             sum[j]+=l.get(j) + sum[j-1];
             else
             sum[j]=sum[j]<sum[j-1]?l.get(j)+sum[j]:l.get(j)+sum[j-1] ;
             
         }
         i++;
        }
        int min = Integer.MAX_VALUE;
    for (int j=0; j < n; j++) {
     if (min > sum[j])
     min = sum[j];
    }
    
    return min;
    }
}
// @lc code=end
