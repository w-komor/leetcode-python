# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

# it's enough to do DFS from city zero. All found routes have to be reversed.

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        for a, b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False))

        def dfs(city, visited):
            visited.add(city)
            count = 0
            for neighbor, to_capital in adj[city]:
                if neighbor not in visited:
                    if to_capital:
                        count += 1
                    count += dfs(neighbor, visited)
            return count

        visited = set()
        return dfs(0, visited)