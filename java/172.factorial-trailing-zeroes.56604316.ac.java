/*
 * @lc app=leetcode id=172 lang=java
 *
 * [172] Factorial Trailing Zeroes
 *
 * https://leetcode.com/problems/factorial-trailing-zeroes/description/
 *
 * algorithms
 * Easy (37.68%)
 * Likes:    744
 * Dislikes: 1028
 * Total Accepted:    199.5K
 * Total Submissions: 529.4K
 * Testcase Example:  '3'
 *
 * Given an integer n, return the number of trailing zeroes in n!.
 * 
 * Example 1:
 * 
 * 
 * Input: 3
 * Output: 0
 * Explanation: 3! = 6, no trailing zero.
 * 
 * Example 2:
 * 
 * 
 * Input: 5
 * Output: 1
 * Explanation: 5! = 120, one trailing zero.
 * 
 * Note: Your solution should be in logarithmic time complexity.
 * 
 */

// @lc code=start
public class Solution {
    public int trailingZeroes(int n) {
        
        int trailingzeroes= 0;
        
        while (n > 4) {
            
            n /= 5;
            trailingzeroes+=n;
        }
        
        return trailingzeroes;
    }
}
// @lc code=end
