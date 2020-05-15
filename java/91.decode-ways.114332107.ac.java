/*
 * @lc app=leetcode id=91 lang=java
 *
 * [91] Decode Ways
 *
 * https://leetcode.com/problems/decode-ways/description/
 *
 * algorithms
 * Medium (24.05%)
 * Likes:    2368
 * Dislikes: 2594
 * Total Accepted:    372.5K
 * Total Submissions: 1.5M
 * Testcase Example:  '"12"'
 *
 * A message containing letters from A-Z is being encoded to numbers using the
 * following mapping:
 * 
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * 
 * Given a non-empty string containing only digits, determine the total number
 * of ways to decode it.
 * 
 * Example 1:
 * 
 * 
 * Input: "12"
 * Output: 2
 * Explanation: It could be decoded as "AB" (1 2) or "L" (12).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "226"
 * Output: 3
 * Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
 * 6).
 * 
 */

// @lc code=start
public class Solution {
    public int numDecodings(String s) {
        
        if (s == null || s.isEmpty()) return 0;
        
                //1234
        
        
        int n = s.length(); //4
        int[] waysOfDecod = new int[n+1]; // { 3, 2, 1,1,1}
        waysOfDecod[n] = 1;
        waysOfDecod[n-1] = s.charAt(n-1) != '0' ? 1 : 0;
        
        for (int i=n-2; i>=0; i--) {
            
            int firstDigit = s.charAt(i) - '0';
            if (firstDigit == 0) continue;
            
            int secondDigit = s.charAt(i+1) - '0';
            waysOfDecod[i] = firstDigit*10 + secondDigit <= 26 ? waysOfDecod[i+1] + waysOfDecod[i+2] : waysOfDecod[i+1];
        }
        
        return waysOfDecod[0];
    }
}
// @lc code=end
