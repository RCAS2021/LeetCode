class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary[0] = 0
        salary[len(salary)-1] = 0

        return sum(salary)/(len(salary)-2)
