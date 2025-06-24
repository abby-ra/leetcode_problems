class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count =0
        while num >=1:
            if num%2 == 0:
                num/=2
                count+=1
            elif num%2 !=0:
                num-=1
                count+=1
        return count
        