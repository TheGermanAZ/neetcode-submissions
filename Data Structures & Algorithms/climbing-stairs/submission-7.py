class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n, memo={}):
            if n <= 2: return n
            if n in memo:
                return memo[n]
            memo[n] = climb(n-1, memo) + climb(n-2, memo)
            return memo[n]
        return climb(n)