/*
 * @lc app=leetcode id=418 lang=java
 *
 * [418] Sentence Screen Fitting
 *
 * https://leetcode.com/problems/sentence-screen-fitting/description/
 *
 * algorithms
 * Medium (32.37%)
 * Likes:    424
 * Dislikes: 211
 * Total Accepted:    41.4K
 * Total Submissions: 127.9K
 * Testcase Example:  '["hello","world"]\n2\n8'
 *
 * Given a rows x cols screen and a sentence represented by a list of non-empty
 * words, find how many times the given sentence can be fitted on the screen.
 * 
 * 
 * Note:
 * 
 * A word cannot be split into two lines.
 * The order of words in the sentence must remain unchanged.
 * Two consecutive words in a line must be separated by a single space.
 * Total words in the sentence won't exceed 100.
 * Length of each word is greater than 0 and won't exceed 10.
 * 1 ≤ rows, cols ≤ 20,000.
 * 
 * 
 * 
 * 
 * Example 1: 
 * 
 * Input:
 * rows = 2, cols = 8, sentence = ["hello", "world"]
 * 
 * Output: 
 * 1
 * 
 * Explanation:
 * hello---
 * world---
 * 
 * The character '-' signifies an empty space on the screen.
 * 
 * 
 * 
 * 
 * Example 2: 
 * 
 * Input:
 * rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
 * 
 * Output: 
 * 2
 * 
 * Explanation:
 * a-bcd- 
 * e-a---
 * bcd-e-
 * 
 * The character '-' signifies an empty space on the screen.
 * 
 * 
 * 
 * 
 * Example 3: 
 * 
 * Input:
 * rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
 * 
 * Output: 
 * 1
 * 
 * Explanation:
 * I-had
 * apple
 * pie-I
 * had--
 * 
 * The character '-' signifies an empty space on the screen.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        
        int[] endingWord = new int[sentence.length];
        int[] timesEntered = new int[sentence.length];
        for (int i = 0; i < endingWord.length; i++)
            endingWord[i] = -1;
        
        int i = 0;
        int times = 0;
        for (int r = 0; r < rows; r++) {
            if (endingWord[i] > -1) {
                times += timesEntered[i];
                i = endingWord[i];
                continue;
            }
                
            int currRowSpace = cols;
            int staringWord = i;
            int startingTimes = times;
            int nextWordSize = sentence[i].length();
            while (nextWordSize <= currRowSpace) {
                currRowSpace -= nextWordSize + 1;
                if (++i == sentence.length) {
                    i = 0;
                    times++;
                }
                nextWordSize = sentence[i].length();
            }
            timesEntered[staringWord] = times - startingTimes;
            endingWord[staringWord] = i;
        }
        
        return times;
    }
}
// @lc code=end
