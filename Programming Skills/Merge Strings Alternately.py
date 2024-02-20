class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        smaller_size = min(len(word1), len(word2))
        if len(word1) > len(word2):
            for i in range(smaller_size):
                merged.append(word1[i])
                merged.append(word2[i])
            merged.append(word1[smaller_size:])
        else:
            for i in range(smaller_size):
                merged.append(word1[i])
                merged.append(word2[i])
            merged.append(word2[smaller_size:])

        separator = ''
        merged = separator.join(merged)
        return merged
