from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {
            0: 0
        }
        
        for rod in rods:
            copy_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                
                # Add rod to the taller stand
                copy_dp[diff + rod] = max(copy_dp.get(diff + rod, 0), taller + rod)
                
                # Add rod to the shorter stand
                new_diff = abs(shorter + rod - taller)
                new_taller = max(shorter + rod, taller)
                copy_dp[new_diff] = max(copy_dp.get(new_diff, 0), new_taller)
                
            dp = copy_dp
            
        return dp.get(0)