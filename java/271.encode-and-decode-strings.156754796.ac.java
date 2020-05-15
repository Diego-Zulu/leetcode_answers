/*
 * @lc app=leetcode id=271 lang=java
 *
 * [271] Encode and Decode Strings
 *
 * https://leetcode.com/problems/encode-and-decode-strings/description/
 *
 * algorithms
 * Medium (30.76%)
 * Likes:    403
 * Dislikes: 145
 * Total Accepted:    56.2K
 * Total Submissions: 182.7K
 * Testcase Example:  '["Hello","World"]'
 *
 * Design an algorithm to encode a list of strings to a string. The encoded
 * string is then sent over the network and is decoded back to the original
 * list of strings.
 * 
 * Machine 1 (sender) has the function:
 * 
 * 
 * string encode(vector<string> strs) {
 * ⁠ // ... your code
 * ⁠ return encoded_string;
 * }
 * Machine 2 (receiver) has the function:
 * 
 * 
 * vector<string> decode(string s) {
 * ⁠ //... your code
 * ⁠ return strs;
 * }
 * 
 * 
 * So Machine 1 does:
 * 
 * 
 * string encoded_string = encode(strs);
 * 
 * 
 * and Machine 2 does:
 * 
 * 
 * vector<string> strs2 = decode(encoded_string);
 * 
 * 
 * strs2 in Machine 2 should be the same as strs in Machine 1.
 * 
 * Implement the encode and decode methods.
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The string may contain any possible characters out of 256 valid ascii
 * characters. Your algorithm should be generalized enough to work on any
 * possible characters.
 * Do not use class member/global/static variables to store states. Your encode
 * and decode algorithms should be stateless.
 * Do not rely on any library method such as eval or serialize methods. You
 * should implement your own encode/decode algorithm.
 * 
 * 
 */

// @lc code=start
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            encoded.append(s.length());
            encoded.append(".");
            encoded.append(s);
        }
        return encoded.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        
        List<String> decoded = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            StringBuilder stringLength = new StringBuilder();
            while (s.charAt(i) != '.') {
                stringLength.append(s.charAt(i++));
            }
            int parsedLength = Integer.parseInt(stringLength.toString());
            i++;
            decoded.add(s.substring(i,i + parsedLength));
            i += parsedLength;
        }
        
        return decoded;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
// @lc code=end
