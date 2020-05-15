/*
 * @lc app=leetcode id=73 lang=java
 *
 * [73] Set Matrix Zeroes
 *
 * https://leetcode.com/problems/set-matrix-zeroes/description/
 *
 * algorithms
 * Medium (42.47%)
 * Likes:    1811
 * Dislikes: 285
 * Total Accepted:    296.6K
 * Total Submissions: 698.3K
 * Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
 *
 * Given a m x n matrix, if an element is 0, set its entire row and column to
 * 0. Do it in-place.
 * 
 * Example 1:
 * 
 * 
 * Input: 
 * [
 * [1,1,1],
 * [1,0,1],
 * [1,1,1]
 * ]
 * Output: 
 * [
 * [1,0,1],
 * [0,0,0],
 * [1,0,1]
 * ]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 
 * [
 * [0,1,2,0],
 * [3,4,5,2],
 * [1,3,1,5]
 * ]
 * Output: 
 * [
 * [0,0,0,0],
 * [0,4,5,0],
 * [0,3,1,0]
 * ]
 * 
 * 
 * Follow up:
 * 
 * 
 * A straight forward solution using O(mn) space is probably a bad idea.
 * A simple improvement uses O(m + n) space, but still not the best
 * solution.
 * Could you devise a constant space solution?
 * 
 * 
 */

// @lc code=start
public class Solution {
    public void setZeroes(int[][] matrix) {
        
        boolean firstc = false;
        boolean firstf = false;
        
        for (int f=0; f<matrix.length; f++) {
            for (int c=0; c<matrix[0].length; c++) {
                
                if (matrix[f][c] == 0) {
                    if (!firstc && c == 0) firstc = true;
                    if (!firstf && f == 0) firstf = true;
                    matrix[0][c] = 0;
                    matrix[f][0] = 0;
                }
            }
        }
        
        for (int f=1; f<matrix.length; f++) {
            for (int c=1; c<matrix[0].length; c++) {
            
                if (matrix[0][c] == 0 || matrix[f][0] == 0) matrix[f][c] = 0;
            }
        }
        
        if (firstf) {
            for (int c=0; c<matrix[0].length; c++) {
                 matrix[0][c] = 0;
            }
        }
        
        if (firstc) {
            for (int f=0; f<matrix.length; f++) {
                 matrix[f][0] = 0;
            }
        }
    }
}
// @lc code=end
