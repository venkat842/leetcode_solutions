class Solution:
    def average(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        avg = sum(salary)/len(salary)
        return avg