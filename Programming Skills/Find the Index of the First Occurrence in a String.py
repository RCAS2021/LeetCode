class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)

# Using function find
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
