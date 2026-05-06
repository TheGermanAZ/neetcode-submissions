class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        rolling = 0
        for num in nums:
            if num == 1:
                rolling += 1
            else:
                count = max(count, rolling)
                rolling = 0
        count = max(count, rolling)
        return count