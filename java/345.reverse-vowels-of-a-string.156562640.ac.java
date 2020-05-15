/*
 * @lc app=leetcode id=345 lang=java
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (43.51%)
 * Likes:    607
 * Dislikes: 1057
 * Total Accepted:    208.3K
 * Total Submissions: 478.3K
 * Testcase Example:  '"hello"'
 *
 * Write a function that takes a string as input and reverse only the vowels of
 * a string.
 * 
 * Example 1:
 * 
 * 
 * Input: "hello"
 * Output: "holle"
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "leetcode"
 * Output: "leotcede"
 * 
 * 
 * Note:
 * The vowels does not include the letter "y".
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    
    private static final char[] VOWELS = {'a', 'e', 'i', 'o', 'u'};
    
    public String reverseVowels(String s) {
        
        char[] result = s.toCharArray();
        int left = 0;
        int right = result.length - 1;
        
        while (left < right) {
            
            while (!isVowel(result[left]) && left < right) left++;
            while (!isVowel(result[right]) && left < right) right--;
            
            char aux = result[left];
            result[left++] = result[right];
            result[right--] = aux;
        }
        
        
        return new String(result);
    }
    
    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        for (char v : VOWELS) {
            if (c == v) return true;
        }
        return false;
    }
}
// @lc code=end
