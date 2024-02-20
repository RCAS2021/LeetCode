# Takes too long
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        test = True
        for char in ransomNote:
            if char not in magazine or ransomNote.count(char) > magazine.count(char):
                test = False
                break
        return test

# Best, instead of counting, replaces one character in magazine with space
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, "", 1)
        return True

# Same as above, uses list method to remove character from list, takes more time
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine.remove(char)               
        return True

# Using dictionary
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}

        for i in magazine:
            currentCount = letters.get(i, 0)
            letters[i] = currentCount + 1
        
        for i in ransomNote:
            currentCount = letters.get(i, 0)
            if (currentCount == 0):
                return False

            letters[i] = currentCount - 1

        return True