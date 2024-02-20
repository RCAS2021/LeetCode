# Without replacing 
class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_list = list(s)
        number = 0

        for i in range(len(s_list) - 1):
            if (conversion[s_list[i]] < conversion[s_list[i+1]]):
                number -= conversion[s[i]]
            else:
                number += conversion[s[i]]
        return number + conversion[s[-1]]

# Replacing
class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            number += conversion[char]
        return number