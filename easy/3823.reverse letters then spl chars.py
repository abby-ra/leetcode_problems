class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        c = []
        for i in s:
            if i.isalpha():
                a.append(i)
            else:
                c.append(i)
            
        a = a[::-1]
        c = c[::-1]
        res = []
        b,d = 0,0
        for i in s:
            if i.isalpha():
                res.append(a[b])
                b+=1
            else:
                res.append(c[d])
                d+=1

        return ''.join(res)