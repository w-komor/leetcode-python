# 268. Missing Number
# https://leetcode.com/problems/missing-number

# XOR is commutative, so we can use XOR to find the missing number.
# XOR(XOR(nums), XOR(0, 1, 2, ..., n)) = missing number

class Solution(object):
    def missingNumber(self, nums):
        result = 0
        for index, value in enumerate(nums):
            result ^= index + 1
            result ^= value
        return result
