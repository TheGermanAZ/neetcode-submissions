class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 2
        while i > 0:
            for num in nums:
                ans.append(num)
            i -= 1
        return ans