class Solution(object):
    def intersect(self, nums1, nums2):
        r = []
        for i in nums1:
            if i in nums2:
                r.append(i)
                nums2.remove(i)
        return r
