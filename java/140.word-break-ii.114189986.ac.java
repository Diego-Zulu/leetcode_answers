/*
 * @lc app=leetcode id=140 lang=java
 *
 * [140] Word Break II
 *
 * https://leetcode.com/problems/word-break-ii/description/
 *
 * algorithms
 * Hard (30.58%)
 * Likes:    1731
 * Dislikes: 362
 * Total Accepted:    219.8K
 * Total Submissions: 717.5K
 * Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
 *
 * Given a non-empty string s and a dictionary wordDict containing a list of
 * non-empty words, add spaces in s to construct a sentence where each word is
 * a valid dictionary word. Return all such possible sentences.
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
 * Input:
 * s = "catsanddog"
 * wordDict = ["cat", "cats", "and", "sand", "dog"]
 * Output:
 * [
 * "cats and dog",
 * "cat sand dog"
 * ]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * s = "pineapplepenapple"
 * wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
 * Output:
 * [
 * "pine apple pen apple",
 * "pineapple pen apple",
 * "pine applepen apple"
 * ]
 * Explanation: Note that you are allowed to reuse a dictionary word.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input:
 * s = "catsandog"
 * wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output:
 * []
 * 
 */

// @lc code=start
public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        return DFS(s, wordDict, new HashMap<String, List<String>>());
    }
    
    private List<String> DFS(String s, List<String> wordDict, HashMap<String, List<String>> wordBreaksInWords) {
        
        if (wordBreaksInWords.containsKey(s))
            return wordBreaksInWords.get(s);
        
        List<String> res = new LinkedList<>();
        if (s.isEmpty()) {
            res.add("");
            return res;
        }
  
        for (String word : wordDict) {
            
            if (s.startsWith(word)) {
                List<String> subWords = DFS(s.substring(word.length()), wordDict, wordBreaksInWords);
                for (String sub : subWords) {
                    res.add(word + (sub.isEmpty() ? "" : " ") + sub);
                }
            }
        }
        
        wordBreaksInWords.put(s, res);
        return res;
    }
}
// @lc code=end
