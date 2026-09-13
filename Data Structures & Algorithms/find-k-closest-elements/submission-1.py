class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = 0

        for i in range(len(arr)):
            if abs(arr[i] - x) < abs(arr[closest] - x):
                closest = i
        
        l = max(0, closest - k)
        r = l + k

        while r < len(arr) and abs(arr[r] - x) < abs(arr[l] - x):
            l += 1
            r += 1
        
        return arr[l:r]
        