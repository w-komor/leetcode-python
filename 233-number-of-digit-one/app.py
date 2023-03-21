# 233. Number of Digit One
# https://leetcode.com/problems/number-of-digit-one

class Solution(object):
    def countDigitOne(self, n):
        count = 0
        position = 1
        while position <= n:
            higher = n // (position * 10)
            current = (n // position) % 10
            lower = n - (n // position) * position
            if current == 0:
                count += higher * position
            elif current == 1:
                count += higher * position + lower + 1
            else:
                count += (higher + 1) * position
            position *= 10
        return count