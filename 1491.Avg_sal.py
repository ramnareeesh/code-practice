class Solution:
    def average(self, salary: list[int]) -> float:
        ma = max(salary)
        mi = min(salary)
        sum = 0
        count = 0
        for i in salary:
            if i != ma and i!= mi:
                sum += i
            else:
                count += 1
        return sum/(len(salary) - count)