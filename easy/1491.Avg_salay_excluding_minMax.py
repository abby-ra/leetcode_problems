class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        m = max(salary)
        n = min(salary)
        s,c = 0,0
        for i in salary:
            if i != n and i != m:
                s +=i
                c += 1

        return float(s)/c