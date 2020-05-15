/*
 * @lc app=leetcode id=524 lang=java
 *
 * [524] Longest Word in Dictionary through Deleting
 *
 * https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
 *
 * algorithms
 * Medium (47.97%)
 * Likes:    499
 * Dislikes: 222
 * Total Accepted:    62.9K
 * Total Submissions: 131.2K
 * Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
 *
 * 
 * Given a string and a string dictionary, find the longest string in the
 * dictionary that can be formed by deleting some characters of the given
 * string. If there are more than one possible results, return the longest word
 * with the smallest lexicographical order. If there is no possible result,
 * return the empty string.
 * 
 * Example 1:
 * 
 * Input:
 * s = "abpcplea", d = ["ale","apple","monkey","plea"]
 * 
 * Output: 
 * "apple"
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * s = "abpcplea", d = ["a","b","c"]
 * 
 * Output: 
 * "a"
 * 
 * 
 * 
 * Note:
 * 
 * All the strings in the input will only contain lower-case letters.
 * The size of the dictionary won't exceed 1,000.
 * The length of all the strings in the input won't exceed 1,000.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String findLongestWord(String s, List<String> d) {
        
        Collections.sort(d);
        String max = "";
        for (String ds : d) {
            
            if (max.length() < ds.length() && ds.length() <= s.length() 
                && canFormWordWithOther(ds, s)) {
                max = ds;
            }
        }
        return max;
    }
    
    private boolean canFormWordWithOther(String word, String other) {
        
        int j = 0;
        for (int i=0; i<other.length() && j<word.length(); i++) {

            if (other.charAt(i) == word.charAt(j)) {
                j++;
            }
        }
        return j == word.length();
    }
}
// @lc code=end
