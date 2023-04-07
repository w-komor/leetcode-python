# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0] * len(spells)
        
        # Sort the potions array for efficient binary search
        potions.sort()
        
        # Helper function for binary search
        def binary_search(potions, target):
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        for i, spell in enumerate(spells):
            if spell == 0:  # If spell strength is 0, no successful pairs can be formed
                continue
                
            # Minimum potion strength needed to form a successful pair with the current spell
            min_potion_strength = -(-success // spell)  # Equivalent to ceil(success / spell)
            
            # Index of the first potion that is strong enough to form a successful pair
            index = binary_search(potions, min_potion_strength)
            
            # Count the number of potions that can form a successful pair with the current spell
            pairs[i] = len(potions) - index
        
        return pairs