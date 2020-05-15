#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (45.31%)
# Likes:    2902
# Dislikes: 46
# Total Accepted:    298K
# Total Submissions: 628.5K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.connections = collections.defaultdict(Trie)
        self.end = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        next_node = self
        for c in word:
            next_node = next_node.connections[c]
        next_node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        next_node = self
        for w in word:
            if w not in next_node.connections:
                return False
            next_node = next_node.connections[w]
        return next_node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        next_node = self
        for w in prefix:
            if w not in next_node.connections:
                return False
            next_node = next_node.connections[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
