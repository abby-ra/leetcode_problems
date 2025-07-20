class Solution:
    def specialArray(self, a):
        n = len(a)
        a.sort()

        for x in range(n + 1):
            cnt = 0
            for num in a:
                if num >= x:
                    cnt += 1
            if cnt == x:
                return x
        return - 1