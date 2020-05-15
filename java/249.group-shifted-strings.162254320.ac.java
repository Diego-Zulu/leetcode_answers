/*
 * @lc app=leetcode id=249 lang=java
 *
 * [249] Group Shifted Strings
 *
 * https://leetcode.com/problems/group-shifted-strings/description/
 *
 * algorithms
 * Medium (52.86%)
 * Likes:    420
 * Dislikes: 77
 * Total Accepted:    65.4K
 * Total Submissions: 123.6K
 * Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
 *
 * Given a string, we can "shift" each of its letter to its successive letter,
 * for example: "abc" -> "bcd". We can keep "shifting" which forms the
 * sequence:
 * 
 * 
 * "abc" -> "bcd" -> ... -> "xyz"
 * 
 * Given a list of strings which contains only lowercase alphabets, group all
 * strings that belong to the same shifting sequence.
 * 
 * Example:
 * 
 * 
 * Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
 * Output: 
 * [
 * ⁠ ["abc","bcd","xyz"],
 * ⁠ ["az","ba"],
 * ⁠ ["acef"],
 * ⁠ ["a","z"]
 * ]
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        
        HashMap<String, List<String>> groupWords = new HashMap<>();
        
        for (String word : strings) {
            
            int minVariation = findVariation(word);
            StringBuilder wordGroupBuilder = new StringBuilder(word.length());
            for (int i=0; i<word.length(); i++) {

                wordGroupBuilder.append(shiftedChar(word.charAt(i), minVariation));
            }
            String wordGroup = wordGroupBuilder.toString();
            List<String> wordsInGroup = groupWords.getOrDefault(wordGroup, new LinkedList<>());
            wordsInGroup.add(word);
            groupWords.putIfAbsent(wordGroup, wordsInGroup);
        }
        
        return new LinkedList<>(groupWords.values());
    }
    
    private char shiftedChar(char c, int minVariation) {
        
        int charCode = c - minVariation;
        
        if (charCode < 'a') {
            charCode = 'z' + (charCode - 'a' + 1);
        } else if (charCode > 'z') {
            charCode %= ('z' + 1);
        }
        
        return (char)charCode;
    }
    
    private int findVariation(String word) {
        
        return word.charAt(0) - 'a';
    }
    
    
}
// @lc code=end
