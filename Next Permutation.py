class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        if len(nums)==2:
            nums[0],nums[1]=nums[1],nums[0]
            return
        idx=len(nums)-2
        while idx>=0 and nums[idx]>=nums[idx+1]:
            idx-=1

        nums[idx+1:len(nums)] = nums[idx+1:len(nums)][::-1]
        if idx==-1:
            return
        swap_idx=idx+1
        while swap_idx<len(nums) and nums[swap_idx]<=nums[idx]:
            swap_idx+=1
        nums[swap_idx],nums[idx]=nums[idx],nums[swap_idx]
        
            
        