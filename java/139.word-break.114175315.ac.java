/*
 * @lc app=leetcode id=139 lang=java
 *
 * [139] Word Break
 *
 * https://leetcode.com/problems/word-break/description/
 *
 * algorithms
 * Medium (39.04%)
 * Likes:    3876
 * Dislikes: 209
 * Total Accepted:    513K
 * Total Submissions: 1.3M
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * Given a non-empty string s and a dictionary wordDict containing a list of
 * non-empty words, determine if s can be segmented into a space-separated
 * sequence of one or more dictionary words.
 * 
 * Note:
 * 
 * 
 * The same word in the dictionary may be reused multiple times in the
 * segmentation.
 * You may assume the dictionary does not contain duplicate words.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "leetcode", wordDict = ["leet", "code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet
 * code".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "applepenapple", wordDict = ["apple", "pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple
 * pen apple".
 * Note that you are allowed to reuse a dictionary word.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output: false
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        Set<String> dict = buildDictFromWordList(wordDict);
        Set<Integer> posWithSegment = new HashSet<>();
        posWithSegment.add(0);
        
        for (int i=0; i<s.length(); i++) {
            if (!posWithSegment.contains(i)) continue;
            for (int j=i+1; j<=s.length(); j++) {
                String subWord = s.substring(i, j);
                if (dict.contains(subWord)) {
                    posWithSegment.add(j);
                }
            }
        }
        
        return posWithSegment.contains(s.length());
    }
    
    private Set<String> buildDictFromWordList(List<String> wordDict) {
        Set<String> dict = new HashSet<>();
        for (String word : wordDict) {
            dict.add(word);
        }
        return dict;
    }
}
// @lc code=end
