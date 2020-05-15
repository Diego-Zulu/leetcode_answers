/*
 * @lc app=leetcode id=201 lang=java
 *
 * [201] Bitwise AND of Numbers Range
 *
 * https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
 *
 * algorithms
 * Medium (39.09%)
 * Likes:    955
 * Dislikes: 120
 * Total Accepted:    148.4K
 * Total Submissions: 379.6K
 * Testcase Example:  '5\n7'
 *
 * Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
 * of all numbers in this range, inclusive.
 * 
 * Example 1:
 * 
 * 
 * Input: [5,7]
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [0,1]
 * Output: 0
 */

// @lc code=start
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        
        int result = m;
        
        m++;
        
        while(m <= n){
             result&=m;
             m++;
        }
        
        return result;
    }
}
// @lc code=end