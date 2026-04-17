class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'}': '{', ']': '[', ')': '('}

        ans = []

        for paren in s:
            if paren in valid:
                if ans and ans[-1] == valid[paren]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(paren)
        return len(ans) == 0