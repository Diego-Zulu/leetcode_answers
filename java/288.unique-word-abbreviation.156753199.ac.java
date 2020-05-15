/*
 * @lc app=leetcode id=288 lang=java
 *
 * [288] Unique Word Abbreviation
 *
 * https://leetcode.com/problems/unique-word-abbreviation/description/
 *
 * algorithms
 * Medium (21.49%)
 * Likes:    95
 * Dislikes: 1236
 * Total Accepted:    49.4K
 * Total Submissions: 229.6K
 * Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n' +
  '[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
 *
 * An abbreviation of a word follows the form <first letter><number><last
 * letter>. Below are some examples of word abbreviations:
 * 
 * 
 * a) it                      --> it    (no abbreviation)
 * 
 * ⁠    1
 * ⁠    ↓
 * b) d|o|g                   --> d1g
 * 
 * ⁠             1    1  1
 * ⁠    1---5----0----5--8
 * ⁠    ↓   ↓    ↓    ↓  ↓    
 * c) i|nternationalizatio|n  --> i18n
 * 
 * ⁠             1
 * ⁠    1---5----0
 * ↓   ↓    ↓
 * d) l|ocalizatio|n          --> l10n
 * 
 * 
 * Assume you have a dictionary and given a word, find whether its abbreviation
 * is unique in the dictionary. A word's abbreviation is unique if no other
 * word from the dictionary has the same abbreviation.
 * 
 * Example:
 * 
 * 
 * Given dictionary = [ "deer", "door", "cake", "card" ]
 * 
 * isUnique("dear") -> false
 * isUnique("cart") -> true
 * isUnique("cane") -> false
 * isUnique("make") -> true
 * 
 * 
 */

// @lc code=start
class ValidWordAbbr {
    
    HashMap<String, String> abbreviations;

    public ValidWordAbbr(String[] dictionary) {
        abbreviations = new HashMap<>();
        for (String s : dictionary) {
            String abbr = abbreviateWord(s);
            if (abbr != null) {
                if (!abbreviations.containsKey(abbr)) {
                    abbreviations.put(abbr, s);   
                } else {
                    abbreviations.put(abbr, ""); 
                }
            }
        }
    }
    
    public boolean isUnique(String word) {
        
        String abbr = abbreviateWord(word);
        if (abbreviations.containsKey(abbr)) {
            return abbreviations.get(abbr).equals(word);
        }
        return true;
    }
    
    private String abbreviateWord(String fullWord) {
        
        if (fullWord.length() < 3) return null;
        
        StringBuilder abbr = new StringBuilder();
        abbr.append(fullWord.charAt(0));
        abbr.append(fullWord.length() - 2);
        abbr.append(fullWord.charAt(fullWord.length() - 1));
        
        return abbr.toString();
    }
}

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
 * boolean param_1 = obj.isUnique(word);
 */
// @lc code=end
