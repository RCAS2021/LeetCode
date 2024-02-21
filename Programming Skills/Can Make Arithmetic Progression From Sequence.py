class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        if len(arr) < 3:
            return True

        diff1 = arr[1]-arr[0]

        for i in range(2, len(arr)):           
            if arr[i] - arr[i-1] != diff1:
                return False
        return True
