# 1402. Reducing Dishes
# https://leetcode.com/problems/reducing-dishes

# 1. Sort the satisfaction array in descending order.
#. 2. Iterate through the sorted satisfaction array, maintaining a running sum of the satisfaction levels.
#. 3. Calculate the like-time coefficient at each step and update the maximum sum whenever we find a better value.
#. 4. If adding the current dish would result in a negative like-time coefficient,
#     we stop the iteration, as the chef can discard this dish and all subsequent dishes.

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Step 1: Sort the satisfaction array in descending order
        satisfaction.sort(reverse=True)
        
        # Initialize variables for running sum, maximum sum, and current like-time coefficient
        running_sum = 0
        max_sum = 0
        like_time_coefficient = 0
        
        # Step 2: Iterate through the sorted satisfaction array
        for s in satisfaction:
            # Step 3: Calculate the running sum
            running_sum += s
            
            # Step 4: Check if adding the current dish would result in a negative like-time coefficient
            if running_sum < 0:
                break
            
            # Update the like-time coefficient and maximum sum
            like_time_coefficient += running_sum
            max_sum = max(max_sum, like_time_coefficient)
        
        return max_sum