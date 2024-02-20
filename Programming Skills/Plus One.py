class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large = int("".join(str(e) for e in digits)) + 1
        digits = []
        for char in str(large):
            digits.append(int(char))
            
        return digits