class Solution(object):  
    def merge(self, nums1, m, nums2, n):
        for i in range(0, n):
            nums1[m] = nums2[i]
            m += 1
        for i in range(0, len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
        return nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        