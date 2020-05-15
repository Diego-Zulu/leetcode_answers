/*
 * @lc app=leetcode id=258 lang=java
 *
 * [258] Add Digits
 *
 * https://leetcode.com/problems/add-digits/description/
 *
 * algorithms
 * Easy (55.99%)
 * Likes:    653
 * Dislikes: 1007
 * Total Accepted:    279.7K
 * Total Submissions: 499.4K
 * Testcase Example:  '38'
 *
 * Given a non-negative integer num, repeatedly add all its digits until the
 * result has only one digit.
 * 
 * Example:
 * 
 * 
 * Input: 38
 * Output: 2 
 * Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
 * Since 2 has only one digit, return it.
 * 
 * 
 * Follow up:
 * Could you do it without any loop/recursion in O(1) runtime?
 */

// @lc code=start
public class Solution {
    public int addDigits(int num) {
        int result = num;
        if (num >= 9) {
            
            if (num % 9 == 0) result = 9;
            else result = num%9;
        }
        
        return result;
    }
}
// @lc code=end
