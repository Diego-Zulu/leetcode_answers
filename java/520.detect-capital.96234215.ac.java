/*
 * @lc app=leetcode id=520 lang=java
 *
 * [520] Detect Capital
 *
 * https://leetcode.com/problems/detect-capital/description/
 *
 * algorithms
 * Easy (53.12%)
 * Likes:    435
 * Dislikes: 237
 * Total Accepted:    107.2K
 * Total Submissions: 201.7K
 * Testcase Example:  '"USA"'
 *
 * Given a word, you need to judge whether the usage of capitals in it is right
 * or not.
 * 
 * We define the usage of capitals in a word to be right when one of the
 * following cases holds:
 * 
 * 
 * All letters in this word are capitals, like "USA".
 * All letters in this word are not capitals, like "leetcode".
 * Only the first letter in this word is capital, like "Google".
 * 
 * Otherwise, we define that this word doesn't use capitals in a right way.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "USA"
 * Output: True
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "FlaG"
 * Output: False
 * 
 * 
 * 
 * 
 * Note: The input will be a non-empty word consisting of uppercase and
 * lowercase latin letters.
 * 
 */

// @lc code=start
public class Solution {
    public boolean detectCapitalUse(String word) {
        
        WordPossibilities pos = WordPossibilities.WHATEVER;
        
        for (int i=0; i<word.length(); i++) {
            
            switch (pos) {
                
                case WHATEVER:
                    if (word.charAt(i) - 'a' < 0) {
                        pos = WordPossibilities.ALLUPP_OR_UPLOW;
                    } else {
                        pos = WordPossibilities.ALL_LOWERCASE;
                    }
                    break;
                case ALL_LOWERCASE:
                    if (word.charAt(i) - 'a' < 0) {
                        return false;
                    }
                    break;
                case ALLUPP_OR_UPLOW:
                    if (word.charAt(i) - 'a' < 0) {
                        pos = WordPossibilities.ALL_UPPERCASE;
                    } else {
                        pos = WordPossibilities.UP_LOW;
                    }
                    break;
                case ALL_UPPERCASE:
                    if (word.charAt(i) - 'a' >= 0) {
                        return false;
                    }
                    break;
                case UP_LOW:
                    if (word.charAt(i) - 'a' < 0) {
                        return false;
                    }
            }
        }
        
        return true;
    }
    
    public enum WordPossibilities {
        
        WHATEVER, ALL_LOWERCASE, ALLUPP_OR_UPLOW, ALL_UPPERCASE, UP_LOW
    } 
}
// @lc code=end
