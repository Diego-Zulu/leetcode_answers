/*
 * @lc app=leetcode id=616 lang=java
 *
 * [616] Add Bold Tag in String
 *
 * https://leetcode.com/problems/add-bold-tag-in-string/description/
 *
 * algorithms
 * Medium (41.93%)
 * Likes:    462
 * Dislikes: 57
 * Total Accepted:    32.9K
 * Total Submissions: 78.4K
 * Testcase Example:  '"abcxyz123"\n["abc","123"]'
 *
 * Given a string s and a list of strings dict, you need to add a closed pair
 * of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If
 * two such substrings overlap, you need to wrap them together by only one pair
 * of closed bold tag. Also, if two substrings wrapped by bold tags are
 * consecutive, you need to combine them.
 * Example 1:
 * 
 * 
 * Input: 
 * s = "abcxyz123"
 * dict = ["abc","123"]
 * Output:
 * "<b>abc</b>xyz<b>123</b>"
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 
 * s = "aaabbcc"
 * dict = ["aaa","aab","bc"]
 * Output:
 * "<b>aaabbc</b>c"
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The given dict won't contain duplicates, and its length won't exceed
 * 100.
 * All the strings in input have length in range [1, 1000].
 * 
 * 
 * Note: This question is the same as 758:
 * https://leetcode.com/problems/bold-words-in-string/
 * 
 */

// @lc code=start
class Solution {
    public String addBoldTag(String s, String[] dict) {
        
        BitSet boldChars = new BitSet(s.length());
        
        for (String sub : dict) {
            int j = 0;
            int i = 0;
            for (; i<s.length(); i++) {
                
                if (j == sub.length()) {
                    boldChars.set(i-j, i);
                    i -= j;
                    j = 0;
                } else if (s.charAt(i) == sub.charAt(j)) {
                    j++;
                } else {
                    i -= j;
                    j = 0;
                }
            }
            if (j == sub.length()) {
                boldChars.set(i-j, i);
            }
        }
        
        StringBuilder withBolds = new StringBuilder();
        boolean open = false;
        for (int i=0; i<s.length(); i++) {
            if (!open && boldChars.get(i)) {
                open = true;
                withBolds.append("<b>");
            } else if (open && !boldChars.get(i)) {
                open = false;
                withBolds.append("</b>");
            }
            withBolds.append(s.charAt(i));
        }
        if (open) {
            withBolds.append("</b>");
        }
        return withBolds.toString();
    }
}
// @lc code=end
