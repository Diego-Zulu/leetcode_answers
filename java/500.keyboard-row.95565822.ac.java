/*
 * @lc app=leetcode id=500 lang=java
 *
 * [500] Keyboard Row
 *
 * https://leetcode.com/problems/keyboard-row/description/
 *
 * algorithms
 * Easy (64.19%)
 * Likes:    511
 * Dislikes: 626
 * Total Accepted:    107.9K
 * Total Submissions: 168.1K
 * Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
 *
 * Given a List of words, return the words that can be typed using letters of
 * alphabet on only one row's of American keyboard like the image
 * below.
 * 
 * 
 * 
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: ["Hello", "Alaska", "Dad", "Peace"]
 * Output: ["Alaska", "Dad"]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * You may use one character in the keyboard more than once.
 * You may assume the input string will only contain letters of alphabet.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public String[] findWords(String[] words) {
        
        HashMap<Character, Integer> charToLine = initializeCharToLineMap();
        LinkedList<String> result = new LinkedList<>();
        
        for (int i=0; i<words.length; i++) {
            
            boolean isAllSameLine = true;
            int startingLine = charToLine.get(Character.toLowerCase(words[i].charAt(0)));
            
            for (int j=1; j<words[i].length(); j++) {
                
                if (startingLine != charToLine.get(Character.toLowerCase(words[i].charAt(j))) ) {
                    isAllSameLine = false;
                    break;
                }
            }
            
            if (isAllSameLine) {
                result.add(words[i]);
            }
        }
        
        return result.toArray(new String[0]);
    }
    
    public HashMap<Character, Integer> initializeCharToLineMap() {
        
        HashMap<Character, Integer> charToLine = new HashMap<>();
        charToLine.put('a', 2);
        charToLine.put('b', 3);
        charToLine.put('c', 3);
        charToLine.put('d', 2);
        charToLine.put('e', 1);
        charToLine.put('f', 2);
        charToLine.put('g', 2);
        charToLine.put('h', 2);
        charToLine.put('i', 1);
        charToLine.put('j', 2);
        charToLine.put('k', 2);
        charToLine.put('l', 2);
        charToLine.put('m', 3);
        charToLine.put('n', 3);
        charToLine.put('o', 1);
        charToLine.put('p', 1);
        charToLine.put('q', 1);
        charToLine.put('r', 1);
        charToLine.put('s', 2);
        charToLine.put('t', 1);
        charToLine.put('u', 1);
        charToLine.put('v', 3);
        charToLine.put('w', 1);
        charToLine.put('x', 3);
        charToLine.put('y', 1);
        charToLine.put('z', 3);
        
        return charToLine;
    }
}
// @lc code=end
