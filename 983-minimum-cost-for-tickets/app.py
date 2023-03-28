# 983. Minimum Cost for Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        dp = [0] * (days[-1] + 1)
        
        for i in range(1, days[-1] + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                cost_1_day = dp[max(0, i - 1)] + costs[0]
                cost_7_day = dp[max(0, i - 7)] + costs[1]
                cost_30_day = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(cost_1_day, cost_7_day, cost_30_day)
        
        return dp[-1]
