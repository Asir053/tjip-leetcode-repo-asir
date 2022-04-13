class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        ans=[1]
        for idx in range(len(nums)-1):
            prod*=nums[idx]
            ans.append(prod)

        prod=1
        idx=0
        for idx in range(len(nums)-1,0,-1):
            prod*=nums[idx]
            ans[idx-1]*=prod
        return ans
            