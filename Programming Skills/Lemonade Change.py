class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five += 1
            else:
                change = i - 5
                if change == 5:
                    five -= 1
                    ten += 1
                else:
                    five -= 1
                    if ten != 0:
                        ten -= 1
                    else:
                        five -= 2
                if five < 0 or ten < 0:
                    return False
        return True
