/*
 * @lc app=leetcode id=760 lang=java
 *
 * [760] Find Anagram Mappings
 *
 * https://leetcode.com/problems/find-anagram-mappings/description/
 *
 * algorithms
 * Easy (80.76%)
 * Likes:    335
 * Dislikes: 159
 * Total Accepted:    57.7K
 * Total Submissions: 71.5K
 * Testcase Example:  '[12,28,46,32,50]\n[50,12,32,46,28]'
 *
 * 
 * Given two lists Aand B, and B is an anagram of A. B is an anagram of A means
 * B is made by randomizing the order of the elements in A.
 * 
 * We want to find an index mapping P, from A to B. A mapping P[i] = j means
 * the ith element in A appears in B at index j.
 * 
 * These lists A and B may contain duplicates.  If there are multiple answers,
 * output any of them.
 * 
 * 
 * 
 * For example, given
 * 
 * A = [12, 28, 46, 32, 50]
 * B = [50, 12, 32, 46, 28]
 * 
 * 
 * We should return
 * 
 * [1, 4, 3, 2, 0]
 * 
 * as P[0] = 1 because the 0th element of A appears at B[1],
 * and P[1] = 4 because the 1st element of A appears at B[4],
 * and so on.
 * 
 * 
 * Note:
 * A, B have equal lengths in range [1, 100].
 * A[i], B[i] are integers in range [0, 10^5].
 * 
 */

// @lc code=start
class Solution {
    public int[] anagramMappings(int[] A, int[] B) {
        
        HashMap<Integer, Integer> numberToPos = new HashMap<>();
        int[] mappings = new int[A.length];
        
        for (int i=0; i<B.length; i++) {
            numberToPos.put(B[i], i);
        }
        
        for (int i=0; i<A.length; i++) {
            mappings[i] = numberToPos.get(A[i]);
        }
        
        return mappings;
    }
}
// @lc code=end
