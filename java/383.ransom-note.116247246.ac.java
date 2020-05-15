/*
 * @lc app=leetcode id=383 lang=java
 *
 * [383] Ransom Note
 *
 * https://leetcode.com/problems/ransom-note/description/
 *
 * algorithms
 * Easy (53.16%)
 * Likes:    573
 * Dislikes: 191
 * Total Accepted:    210.1K
 * Total Submissions: 395.6K
 * Testcase Example:  '"a"\n"b"'
 *
 * Given an arbitrary ransom note string and another string containing letters
 * from all the magazines, write a function that will return true if the ransom
 * note can be constructed from the magazines ; otherwise, it will return
 * false.
 * 
 * Each letter in the magazine string can only be used once in your ransom
 * note.
 * 
 * 
 * Example 1:
 * Input: ransomNote = "a", magazine = "b"
 * Output: false
 * Example 2:
 * Input: ransomNote = "aa", magazine = "ab"
 * Output: false
 * Example 3:
 * Input: ransomNote = "aa", magazine = "aab"
 * Output: true
 * 
 * 
 * Constraints:
 * 
 * 
 * You may assume that both strings contain only lowercase letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        int[] magazineLetters = new int['z' - 'a' + 1];
        
        for (int i=0; i<magazine.length(); i++) {
            magazineLetters[magazine.charAt(i) - 'a']++;
        }
        
        for (int i=0; i<ransomNote.length(); i++) {
            
            char letter = ransomNote.charAt(i);
            
            if (magazineLetters[letter - 'a'] == 0) return false;
            
            magazineLetters[letter - 'a']--;
        }
        
        return true;
    }
}
// @lc code=end
