# Converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        temp_list = list(temp)
        if(temp_list == temp_list[::-1]):
            return True
        return False

# Without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        r = 0
        while x > r:
            r = (r*10) + (x % 10)
            x //= 10
        return x == r // 10 or r == x