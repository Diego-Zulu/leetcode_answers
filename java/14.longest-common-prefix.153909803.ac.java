/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (35.00%)
 * Likes:    2313
 * Dislikes: 1771
 * Total Accepted:    706.2K
 * Total Submissions: 2M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        String max = null;
        String min = null;
        
        for (int i=0; i<strs.length; i++) {
            
            String aux = strs[i];
            
            if (max == null || aux.compareTo(max) > 0) {
                if (min == null) {
                    min = max;
                }
                max = aux;
            } else if (min == null || aux.compareTo(min) < 0) {
                if (max == null) {
                    max = min;
                }
                min = aux;
            }
        }
        
        if (max == null) {
            if (min == null) {
                return "";
            }
            return min;
        } else if (min == null) {
            return max;
        } else {
            StringBuilder sbr = new StringBuilder();
            int minLength = Math.min(max.length(), min.length());
            for (int i=0; i < minLength; i++) {
                
                if (max.charAt(i) == min.charAt(i)) {
                    sbr.append(max.charAt(i));
                } else {
                    break;
                }
            }
            
            return sbr.toString();
        }
    }
}
// @lc code=end
