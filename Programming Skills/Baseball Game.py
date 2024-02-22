class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == "+":
                score.append(score[len(score) - 1] + score[len(score) - 2])
            elif i == "D":
                score.append(score[len(score) - 1] * 2)
            elif i == "C":
                score.pop()
            else:
                score.append(int(i))
        return sum(score)
