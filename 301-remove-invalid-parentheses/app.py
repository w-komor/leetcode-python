# 301. Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/

from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        result = []
        found = False

        while queue:
            current_string = queue.popleft()

            if is_valid(current_string):
                result.append(current_string)
                found = True

            if found:
                continue

            # Enqueue all combinations of current string with 1 char deleted
            for i in range(len(current_string)):
                if current_string[i] in ('(', ')'):
                    new_string = current_string[:i] + current_string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

        return result