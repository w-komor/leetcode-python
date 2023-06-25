# 1575. Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        memo = {}
        mod = 1000000007

        def solve(current, remainingFuel):
            if remainingFuel < 0:
                return 0
            if (current, remainingFuel) in memo:
                return memo[(current, remainingFuel)]
            
            ans = 0
            if current == finish:
                ans = 1
            for nextCity in range(n):
                if (nextCity != current):
                    cost = abs(locations[current] - locations[nextCity])
                    ans = (ans + solve(nextCity, remainingFuel - cost)) % mod
            
            memo[(current, remainingFuel)] = ans
            return ans

        return solve(start, fuel)