/*
 * @lc app=leetcode id=409 lang=java
 *
 * [409] Longest Palindrome
 *
 * https://leetcode.com/problems/longest-palindrome/description/
 *
 * algorithms
 * Easy (49.88%)
 * Likes:    853
 * Dislikes: 78
 * Total Accepted:    134.5K
 * Total Submissions: 269.5K
 * Testcase Example:  '"abccccdd"'
 *
 * Given a string which consists of lowercase or uppercase letters, find the
 * length of the longest palindromes that can be built with those letters.
 * 
 * This is case sensitive, for example "Aa" is not considered a palindrome
 * here.
 * 
 * Note:
 * Assume the length of given string will not exceed 1,010.
 * 
 * 
 * Example: 
 * 
 * Input:
 * "abccccdd"
 * 
 * Output:
 * 7
 * 
 * Explanation:
 * One longest palindrome that can be built is "dccaccd", whose length is 7.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int longestPalindrome(String s) {
        
        int[] evenTimes = new int['z' - 'A' + 1];
        boolean[] alreadyHasOdd = new boolean['z' - 'A' + 1];
        
        for (int i=0; i<s.length(); i++) {
            
            char thisChar = s.charAt(i);
            int pos = thisChar - 'A';
            
            if (alreadyHasOdd[pos]) {
                evenTimes[pos]+=2;
            }
            alreadyHasOdd[pos] = !alreadyHasOdd[pos];
        }
        
        boolean atLeastOneOdd = false;
        int length = 0;
        
        for (int i=0; i<evenTimes.length; i++) {
            length+=evenTimes[i];
            if (alreadyHasOdd[i]) {
                atLeastOneOdd = true;
            }
        }
        
        return atLeastOneOdd ? length + 1 : length;
    }
}
// @lc code=end
