class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in has:
                return [has[ans], i]
            has[num] = i
        return []
