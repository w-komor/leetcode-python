# 2492. Minimum Score of a Path Between Two Cities
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        
        for city1, city2, distance in roads:
            adjacency_list[city1].append(city2)
            adjacency_list[city2].append(city1)
            
        min_distance = float('inf')
        visited_cities = set()
        queue = deque([1])
        
        while queue:
            current_city = queue.popleft()
            for neighboring_city in adjacency_list[current_city]:
                if neighboring_city not in visited_cities:
                    queue.append(neighboring_city)
                    visited_cities.add(neighboring_city)
                    
        for city1, city2, distance in roads:
            if city1 in visited_cities or city2 in visited_cities:
                min_distance = min(min_distance, distance)
                
        return min_distance