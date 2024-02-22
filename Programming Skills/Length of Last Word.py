class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Splits the string into a list separating by spaces
        s = s.split(" ")
        # Creates new list to allocate not spaces
        res = []
        # Removes empty spaces from string list
        for ele in s:
            if ele.strip():
                res.append(ele)
        
        # Return length of last element in list
        return len(res[len(res)-1])
        