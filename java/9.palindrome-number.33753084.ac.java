/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 *
 * https://leetcode.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (47.46%)
 * Likes:    2149
 * Dislikes: 1511
 * Total Accepted:    881.1K
 * Total Submissions: 1.9M
 * Testcase Example:  '121'
 *
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 * 
 * Example 1:
 * 
 * 
 * Input: 121
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it
 * becomes 121-. Therefore it is not a palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a
 * palindrome.
 * 
 * 
 * Follow up:
 * 
 * Coud you solve it without converting the integer to a string?
 * 
 */

// @lc code=start
public class Solution {
    public boolean isPalindrome(int x) {
       
        if (x<0) return false;
        int copy = x;
        int reverse = 0;
        int rest = 0;
        
        while (copy != 0) {
            rest = copy%10;
            reverse = reverse*10 + rest;
            copy = copy/10;
        }
        
        return reverse == x;
    }
}
// @lc code=end
