/*
 * @lc app=leetcode id=127 lang=java
 *
 * [127] Word Ladder
 *
 * https://leetcode.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (28.44%)
 * Likes:    2781
 * Dislikes: 1097
 * Total Accepted:    396.2K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * Given two words (beginWord and endWord), and a dictionary's word list, find
 * the length of shortest transformation sequence from beginWord to endWord,
 * such that:
 * 
 * 
 * Only one letter can be changed at a time.
 * Each transformed word must exist in the word list.
 * 
 * 
 * Note:
 * 
 * 
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * Output: 5
 * 
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
 * "dog" -> "cog",
 * return its length 5.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * Output: 0
 * 
 * Explanation: The endWord "cog" is not in wordList, therefore no possible
 * transformation.
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
        Set<String> reached = new HashSet<>();   
        Set<String> dict = new HashSet<>(wordList);
        reached.add(beginWord); 
        int distance = 1;
        
        while (!reached.contains(endWord)) {
            
            Set<String> reachedNow = new HashSet<>();
            for (String word : reached) {
                
                char[] wordInChars = word.toCharArray();
                for (int i=0; i<wordInChars.length; i++) {
                    char charAtPos = wordInChars[i];
                    
                    for (char ch='a'; ch<='z'; ch++) {
                        
                        wordInChars[i] = ch;
                        String newWord = new String(wordInChars);
                        
                        if (dict.contains(newWord)) {
                            dict.remove(newWord);
                            reachedNow.add(newWord);
                        }
                    }
                    wordInChars[i] = charAtPos;
                }
            }
            if (reachedNow.isEmpty()) return 0;
            distance++;
            reached = reachedNow;
        }
        
        return distance;
    }
}
// @lc code=end
