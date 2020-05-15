/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (29.94%)
 * Likes:    8656
 * Dislikes: 525
 * Total Accepted:    1.5M
 * Total Submissions: 4.9M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string, find the length of the longest substring without repeating
 * characters.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "abcabcbb"
 * Output: 3 
 * Explanation: The answer is "abc", with the length of 3. 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3. 
 * ⁠            Note that the answer must be a substring, "pwke" is a
 * subsequence and not a substring.
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if (s == null) return 0;
        
        HashMap<Character, Integer> charAppearings = new HashMap<>();
        int left = 0;
        int max = 0;
        
        for (int right=0; right<s.length(); right++) {
            char actualChar = s.charAt(right);
            int repeatedTimes = charAppearings.getOrDefault(actualChar, 0)+1;
            charAppearings.put(actualChar, repeatedTimes);
            
            if (repeatedTimes == 1) {
                max = Math.max(max, right - left + 1);
            } else {
                
                while (left < right && repeatedTimes > 1) {
                    char otherChar = s.charAt(left);
                    int otherCharRepeated = charAppearings.get(otherChar)-1;
                    charAppearings.put(otherChar, otherCharRepeated);
                    left++;
                    if (otherChar == actualChar) {
                        repeatedTimes = otherCharRepeated;
                    }
                    
                }
            }
        }
        
        return max;
    }
}
// @lc code=end
