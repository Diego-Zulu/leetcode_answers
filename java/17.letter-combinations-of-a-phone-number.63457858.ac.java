/*
 * @lc app=leetcode id=17 lang=java
 *
 * [17] Letter Combinations of a Phone Number
 *
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (45.71%)
 * Likes:    3540
 * Dislikes: 391
 * Total Accepted:    572.7K
 * Total Submissions: 1.3M
 * Testcase Example:  '"23"'
 *
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 * 
 * A mapping of digit to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * 
 * 
 * Note:
 * 
 * Although the above answer is in lexicographical order, your answer could be
 * in any order you want.
 * 
 */

// @lc code=start
public class Solution {
    public List<String> letterCombinations(String digits) {
        
        LinkedList<String> preAnswer = new LinkedList<>();
        String[] digitToLetter = {" ", ".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        int n = digits.length();
        if (n == 0) return preAnswer;
        preAnswer.add("");
        
        for (int i = 0; i< n; i++) {
            
            int digitValue = digits.charAt(i) - '0';
            while (preAnswer.peek().length() == i) {
                
                String actualWord = preAnswer.remove();
                int a = digitToLetter[digitValue].length();
                for (int j = 0; j<a; j++) {
                    preAnswer.add(actualWord + digitToLetter[digitValue].charAt(j));
                }
            }
        }
        
        return preAnswer;
    }
}
// @lc code=end
