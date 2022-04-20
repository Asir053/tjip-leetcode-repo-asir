class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num1=nums[0]
        for idx in range(1,len(nums)):
            num1=num1^nums[idx]
        return num1
        