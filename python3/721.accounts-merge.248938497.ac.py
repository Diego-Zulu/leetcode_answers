#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (47.15%)
# Likes:    1218
# Dislikes: 275
# Total Accepted:    72.1K
# Total Submissions: 152.7K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#

# @lc code=start
class DSU:
    def __init__(self):
        self.a = [i for i in range(10001)]
    
    def find(self, x):
        if x != self.a[x]:
            self.a[x] = self.find(self.a[x])
        return self.a[x]
        
    def union(self, x, y):
        self.a[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        dsu = DSU()
        email_to_id, email_to_name = {}, {}
        ordered, i = [], 0
        for acc in accounts:
            name, first_e = acc[0:2]
            for e in acc[1::]:
                if e not in email_to_name:
                    email_to_name[e] = name
                    email_to_id[e] = i
                    heapq.heappush(ordered, e)
                    i += 1
                dsu.union(email_to_id[first_e], email_to_id[e])
        result, id_to_group = [], {}
        while len(ordered):
            e = heapq.heappop(ordered)
            _id = dsu.find(email_to_id[e])
            if _id not in id_to_group:
                group = [email_to_name[e]]
                result.append(group)
                id_to_group[_id] = group
            id_to_group[_id].append(e)
        return result
# @lc code=end
