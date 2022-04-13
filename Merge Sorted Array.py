class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1,idx2,k=0,0,0
        nums1_init=nums1.copy()
        while idx1<m and idx2<n:
            if nums1_init[idx1]>nums2[idx2]:
                nums1[k]=nums2[idx2]
                idx2+=1
            else:
                nums1[k]=nums1_init[idx1]
                idx1+=1
            k+=1

        while idx1<m:
            nums1[k]=nums1_init[idx1]
            idx1+=1
            k+=1
            
        while idx2<n:
            nums1[k]=nums2[idx2]
            idx2+=1
            k+=1
 
            
            
        