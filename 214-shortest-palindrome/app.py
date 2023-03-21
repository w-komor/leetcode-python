# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome

# KMP (Knuth–Morris–Pratt) string searching algorithm

class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s
        
        def preprocess(s):
            i, j = 1, 0
            b = [0] * (len(s) + 1)
            while i < len(s):
                if s[i] == s[j]:
                    j += 1
                    b[i + 1] = j
                    i += 1
                elif j == 0:
                    i += 1
                else:
                    j = b[j]
            return b
        
        t = s + "#" + s[::-1]
        b = preprocess(t)
        return s[b[-1]:][::-1] + s