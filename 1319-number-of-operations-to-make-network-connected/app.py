# 1319. Number of Operations to Make Network Connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

# If there are k connected components in the network, we need k-1 cables to connect all of them.
# We can use Depth First Search (DFS) to traverse the graph and find the connected components.
# Additionally, we need to make sure that there are enough cables to connect all the components.

from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        visited = [False] * n

        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in adj[node]:
                dfs(neighbor)
        
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components - 1