from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        
        for i in range(0,l):
            for j in range(0,l):
                if nums[i] + nums[j] == target and i!=j:
                    OTP = [i,j]
        return OTP

        
            
