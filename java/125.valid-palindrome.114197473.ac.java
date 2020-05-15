/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (35.06%)
 * Likes:    1058
 * Dislikes: 2734
 * Total Accepted:    545.4K
 * Total Submissions: 1.6M
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 * 
 * Note: For the purpose of this problem, we define empty string as valid
 * palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: "A man, a plan, a canal: Panama"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "race a car"
 * Output: false
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean isPalindrome(String s) {
        
        int low = -1;
        int high = s.length();
        while (low < high) {
            
            do 
                low++;
            while (low < s.length() && !Character.isLetterOrDigit(s.charAt(low)));
            do 
                high--;
            while (high >= 0 && !Character.isLetterOrDigit(s.charAt(high)));
            
            if (low < high 
                && Character.toLowerCase(s.charAt(low)) != Character.toLowerCase(s.charAt(high))) 
                return false;
        }
        
        return true;
    }
}
// @lc code=end
