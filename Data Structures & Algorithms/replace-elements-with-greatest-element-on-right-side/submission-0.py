class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        high = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = high
            high = max(temp, high)
            i -= 1
        return arr