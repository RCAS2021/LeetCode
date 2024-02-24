class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1

        if total % 2 == 1:
            if low % 2 == 1:
                return (total + 1) // 2
        return total // 2
