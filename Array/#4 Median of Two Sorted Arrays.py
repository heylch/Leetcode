class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1)+len(nums2)
        median = 0
        if length %2 !=0:
            median = self.findkth(nums1,nums2,int(length/2)+1)
        else:
            median = float(self.findkth(nums1,nums2,int(length/2))+self.findkth(nums1,nums2,int(length/2)+1))/2
        return median

    def findkth(self,nums1,nums2,k):
        result = 0
        if len(nums1)==0:
            result = nums2[k-1]
        elif len(nums2)==0:
            result = nums1[k-1]
        else:
            if k==1:
                result = min([nums1[0],nums2[0]])
            else:
                idx = int(k/2)
                idx1 = idx
                idx2 = idx
                if len(nums1) < idx:
                    idx1 = len(nums1)
                if len(nums2) <idx:
                    idx2 = len(nums2)
                if nums1[idx1-1] <= nums2[idx2-1]:
                    new_k = k-idx1
                    result = self.findkth(nums1[idx1:],nums2,new_k)
                else:
                    new_k = k-idx2
                    result = self.findkth(nums1,nums2[idx2:],new_k)
        return result