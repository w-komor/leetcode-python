# 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution(object):
    def zeroFilledSubarray(self, nums):
        zero_count = 0
        result = 0

        for num in nums:
            if num == 0:
                zero_count += 1
                result += zero_count
            else:
                zero_count = 0
        
        return result