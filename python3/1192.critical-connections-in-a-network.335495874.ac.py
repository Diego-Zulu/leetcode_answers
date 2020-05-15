#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (48.71%)
# Likes:    900
# Dislikes: 70
# Total Accepted:    46.1K
# Total Submissions: 94.6K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
# 
# 
#

# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dist = [float('inf')] * n
        lowest = [float('inf')] * n
        visited = [False] * n

        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        critical = []
        next_dist = 0
        
        def find_critical_connections(parent, next_node):
            nonlocal next_dist
            if visited[next_node]:
                return
            visited[next_node] = True
            dist[next_node] = next_dist
            lowest[next_node] = next_dist
            next_dist += 1
            
            for conn in graph[next_node]:
                if conn == parent:
                    continue
                if not visited[conn]:
                    find_critical_connections(next_node, conn)
                lowest[next_node] = min(lowest[next_node], lowest[conn])
                if lowest[conn] > dist[next_node]:
                    critical.append([next_node, conn])
            
        find_critical_connections(0, 0)
        return critical
        
# @lc code=end
