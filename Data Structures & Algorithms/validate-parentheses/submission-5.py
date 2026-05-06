class Solution:
    def isValid(self, s: str) -> bool:
        paren = {']': '[', ')': '(', '}': '{'}
        stack = []

        for char in s:
            if char in paren:
                if not stack or stack[-1] != paren[char]: return False
                if stack[-1] == paren[char]:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0