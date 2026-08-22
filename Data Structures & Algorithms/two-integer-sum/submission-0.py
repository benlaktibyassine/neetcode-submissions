class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            b= target - nums[i]
            if b in s:
                return [s[b],i]
            else :
                s[nums[i]]=i
        