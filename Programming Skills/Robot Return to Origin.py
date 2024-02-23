class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left_right, up_down = 0 , 0
        for i in moves:
            if i == "R":
                left_right += 1
            elif i == "L":
                left_right -= 1
            elif i == "U":
                up_down += 1
            elif i == "D":
                up_down -= 1
            else:
                print("Invalid Move")
        
        return left_right == 0 and up_down == 0