/*
 * @lc app=leetcode id=737 lang=java
 *
 * [737] Sentence Similarity II
 *
 * https://leetcode.com/problems/sentence-similarity-ii/description/
 *
 * algorithms
 * Medium (45.36%)
 * Likes:    461
 * Dislikes: 30
 * Total Accepted:    38.6K
 * Total Submissions: 85K
 * Testcase Example:  '["great","acting","skills"]\n' +
  '["fine","drama","talent"]\n' +
  '[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
 *
 * Given two sentences words1, words2 (each represented as an array of
 * strings), and a list of similar word pairs pairs, determine if two sentences
 * are similar.
 * 
 * For example, words1 = ["great", "acting", "skills"] and words2 = ["fine",
 * "drama", "talent"] are similar, if the similar word pairs are pairs =
 * [["great", "good"], ["fine", "good"], ["acting","drama"],
 * ["skills","talent"]].
 * 
 * Note that the similarity relation is transitive. For example, if "great" and
 * "good" are similar, and "fine" and "good" are similar, then "great" and
 * "fine" are similar.
 * 
 * Similarity is also symmetric. For example, "great" and "fine" being similar
 * is the same as "fine" and "great" being similar.
 * 
 * Also, a word is always similar with itself. For example, the sentences
 * words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though
 * there are no specified similar word pairs.
 * 
 * Finally, sentences can only be similar if they have the same number of
 * words. So a sentence like words1 = ["great"] can never be similar to words2
 * = ["doubleplus","good"].
 * 
 * Note:
 * 
 * 
 * The length of words1 and words2 will not exceed 1000.
 * The length of pairs will not exceed 2000.
 * The length of each pairs[i] will be 2.
 * The length of each words[i] and pairs[i][j] will be in the range [1,
 * 20].
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, String[][] pairs) {
        
        if (words1.length != words2.length) return false;

        HashMap<String, Integer> wordToNumber = new HashMap<>();
        int lastNumberAssigned = 0;

        for (int i=0; i<pairs.length; i++) {
            if (!wordToNumber.containsKey(pairs[i][0])) {
                wordToNumber.put(pairs[i][0], ++lastNumberAssigned);
            }
            if (!wordToNumber.containsKey(pairs[i][1])) {
                wordToNumber.put(pairs[i][1], ++lastNumberAssigned);
            }
        }

        int[] parents = new int[lastNumberAssigned + 1];
        for (int i=0; i<parents.length; i++) {
            parents[i] = i;
        }

        for (int i=0; i<pairs.length; i++) {
            union(parents, wordToNumber.get(pairs[i][0]), wordToNumber.get(pairs[i][1]));
        }

        for (int i=0; i<words1.length; i++) {

            Integer firstWordNumb = wordToNumber.get(words1[i]);
            Integer secondWordNumb = wordToNumber.get(words2[i]);
            if ((firstWordNumb == null || secondWordNumb == null) && !words1[i].equals(words2[i]))
                return false;
            if (firstWordNumb != null && secondWordNumb != null && find(parents, wordToNumber.get(words1[i])) != find(parents, wordToNumber.get(words2[i])))
                return false;
        }
        return true;
    }
    
    private void union(int[] parents, int p, int s) {
        parents[find(parents, p)] = find(parents, s);
    }
    
    private int find(int[] parents, int p) {
        
        if (parents[p] == p) return p;
        return find(parents, parents[p]);
    }
}
// @lc code=end
