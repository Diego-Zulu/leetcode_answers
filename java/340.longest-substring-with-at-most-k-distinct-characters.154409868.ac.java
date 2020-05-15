/*
 * @lc app=leetcode id=340 lang=java
 *
 * [340] Longest Substring with At Most K Distinct Characters
 *
 * https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
 *
 * algorithms
 * Hard (43.34%)
 * Likes:    985
 * Dislikes: 35
 * Total Accepted:    123.6K
 * Total Submissions: 285K
 * Testcase Example:  '"eceba"\n2'
 *
 * Given a string, find the length of the longest substring T that contains at
 * most k distinct characters.
 * 
 * Example 1:
 * 
 * 
 * 
 * Input: s = "eceba", k = 2
 * Output: 3
 * Explanation: T is "ece" which its length is 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "aa", k = 1
 * Output: 2
 * Explanation: T is "aa" which its length is 2.
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        
        if (s == null || s.equals("") || k <= 0) return 0;
        
        int[] currentChars = new int['~' - '!' + 1];
        int distintChars = 0;
        int maxLength = Integer.MIN_VALUE;
        
        int left = 0;
        int right = -1;
        
        while (right < s.length() - 1) {
            
            if (distintChars > k) {
                int leftCharPos = '~' - s.charAt(left);
                currentChars[leftCharPos]--;
                
                if (currentChars[leftCharPos] == 0) {
                    distintChars--;
                }
                left++;
            } else {
                right++;
                int rightCharPos = '~' - s.charAt(right);
                currentChars[rightCharPos]++;
                
                if (currentChars[rightCharPos] == 1) {
                    distintChars++;
                }
                
                if (distintChars <= k) {
                    maxLength = Math.max(maxLength, right - left + 1);
                }
            }
        }
        
        return maxLength;
    }
}
// @lc code=end
